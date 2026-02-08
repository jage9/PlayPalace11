import { createStore } from "./store.js";
import { createA11y } from "./a11y.js";
import { createAudioEngine } from "./audio.js";
import { createHistoryView } from "./ui/history.js";
import { createMenuView } from "./ui/menus.js";
import { createChat } from "./ui/chat.js";
import { installKeybinds } from "./keybinds.js";
import { createNetworkClient, loadPacketValidator } from "./network.js";

const REMEMBERED_USERNAME_KEY = "playpalace.web.remembered_username";
const MUSIC_VOLUME_KEY = "playpalace.web.music_volume";
const AMBIENCE_VOLUME_KEY = "playpalace.web.ambience_volume";
const DEFAULT_MUSIC_VOLUME = 20;
const DEFAULT_AMBIENCE_VOLUME = 100;
const DEFAULT_APP_VERSION = "2026.02.08.1";
const DEFAULT_WEB_CLIENT_CONFIG = {
  serverUrl: "",
  serverPort: null,
  soundBaseUrl: "./sounds",
};
const WEB_CLIENT_CONFIG = {
  ...DEFAULT_WEB_CLIENT_CONFIG,
  ...(window.WEB_CLIENT_CONFIG || {}),
};
const APP_VERSION = String(
  window.PLAYPALACE_WEB_VERSION || DEFAULT_APP_VERSION
).trim();

function getDefaultServerUrl() {
  if (WEB_CLIENT_CONFIG.serverUrl) {
    try {
      const configured = new URL(WEB_CLIENT_CONFIG.serverUrl);
      if (!configured.port && WEB_CLIENT_CONFIG.serverPort) {
        configured.port = String(WEB_CLIENT_CONFIG.serverPort);
      }
      return configured.toString().replace(/\/$/, "");
    } catch {
      return WEB_CLIENT_CONFIG.serverUrl;
    }
  }

  const host = window.location.hostname;
  const isLocalHost = host === "localhost" || host === "127.0.0.1" || host === "::1";
  if (isLocalHost) {
    const localPort = WEB_CLIENT_CONFIG.serverPort || 8000;
    return `ws://127.0.0.1:${localPort}`;
  }

  const isHttps = window.location.protocol === "https:";
  const wsScheme = isHttps ? "wss" : "ws";
  const port = WEB_CLIENT_CONFIG.serverPort
    ? String(WEB_CLIENT_CONFIG.serverPort)
    : window.location.port;
  const isDefaultPort = (!isHttps && port === "80") || (isHttps && port === "443");
  const portSuffix = port && !isDefaultPort ? `:${port}` : "";
  return `${wsScheme}://${host}${portSuffix}`;
}

function normalizeUsername(username) {
  return String(username || "").trim().toLowerCase();
}

function clampPercent(value, fallback) {
  const parsed = Number(value);
  if (!Number.isFinite(parsed)) {
    return fallback;
  }
  return Math.max(0, Math.min(100, Math.round(parsed)));
}

function loadStoredPercent(key, fallback) {
  try {
    return clampPercent(localStorage.getItem(key), fallback);
  } catch {
    return fallback;
  }
}

function saveStoredPercent(key, value) {
  try {
    localStorage.setItem(key, String(clampPercent(value, 0)));
  } catch {
    // Ignore persistence failures.
  }
}

const elements = {
  loginDialog: document.getElementById("login-dialog"),
  gameShell: document.getElementById("game-shell"),
  connectForm: document.getElementById("connect-form"),
  username: document.getElementById("username"),
  password: document.getElementById("password"),
  rememberMe: document.getElementById("remember-me"),
  openLoginBtn: document.getElementById("open-login-btn"),
  disconnectBtn: document.getElementById("disconnect-btn"),
  status: document.getElementById("status"),

  menuList: document.getElementById("menu-list"),
  inlineInput: document.getElementById("inline-input"),
  inlineInputPrompt: document.getElementById("inline-input-prompt"),
  inlineInputValue: document.getElementById("inline-input-value"),
  inlineInputSubmit: document.getElementById("inline-input-submit"),
  inlineInputCancel: document.getElementById("inline-input-cancel"),

  history: document.getElementById("history"),
  historyBuffer: document.getElementById("history-buffer"),

  chatForm: document.getElementById("chat-form"),
  chatInput: document.getElementById("chat-input"),

  politeLive: document.getElementById("live-polite"),
  assertiveLive: document.getElementById("live-assertive"),

  inputDialog: document.getElementById("input-dialog"),
  inputDialogForm: document.getElementById("input-dialog-form"),
  inputPrompt: document.getElementById("input-prompt"),
  inputValue: document.getElementById("input-value"),
  inputCancel: document.getElementById("input-cancel"),
  inputSubmit: document.getElementById("input-submit"),
  appVersion: document.getElementById("app-version"),
};

const store = createStore();
const a11y = createA11y({
  politeEl: elements.politeLive,
  assertiveEl: elements.assertiveLive,
});
const audio = createAudioEngine({
  soundBaseUrl: WEB_CLIENT_CONFIG.soundBaseUrl || "./sounds",
});
audio.setMusicVolumePercent(loadStoredPercent(MUSIC_VOLUME_KEY, DEFAULT_MUSIC_VOLUME));
audio.setAmbienceVolumePercent(loadStoredPercent(AMBIENCE_VOLUME_KEY, DEFAULT_AMBIENCE_VOLUME));

const historyView = createHistoryView({
  store,
  historyEl: elements.history,
  bufferSelectEl: elements.historyBuffer,
  a11y,
});

const menuView = createMenuView({
  store,
  listEl: elements.menuList,
  onSelectionSound: (item) => {
    if (item?.sound) {
      audio.playSound({ name: item.sound, volume: 100 });
      return;
    }
    audio.playSound({ name: "menuclick.ogg", volume: 50 });
  },
  onBoundaryRepeat: (text) => {
    if (text) {
      a11y.announce(text, { assertive: true });
    }
  },
  onActivateSound: () => {
    audio.playSound({ name: "menuenter.ogg", volume: 50 });
  },
  onActivate: (_, selectionIndex) => {
    sendMenuSelection(selectionIndex);
  },
});
let pendingInlineInput = null;
let focusMenuOnNextMenuPacket = false;

let network = null;

function setStatus(text, isError = false) {
  elements.status.textContent = text;
  elements.status.classList.toggle("error", isError);
}

function renderVersion() {
  if (!elements.appVersion) {
    return;
  }
  elements.appVersion.textContent = `Web client version ${APP_VERSION}`;
}

function setConnectedUi(connected) {
  elements.gameShell.hidden = !connected;
  elements.disconnectBtn.disabled = !connected;
  elements.openLoginBtn.disabled = connected;
}

function loadRememberedUsername() {
  try {
    const raw = localStorage.getItem(REMEMBERED_USERNAME_KEY);
    if (!raw) {
      return "";
    }
    return normalizeUsername(raw);
  } catch {
    return "";
  }
}

function saveRememberedUsername(username) {
  const safeUsername = normalizeUsername(username);
  if (!safeUsername) {
    return;
  }
  localStorage.setItem(REMEMBERED_USERNAME_KEY, safeUsername);
}

function clearRememberedUsername() {
  localStorage.removeItem(REMEMBERED_USERNAME_KEY);
}

function applyRememberedUsernameToLoginForm() {
  const rememberedUsername = loadRememberedUsername();
  elements.username.value = rememberedUsername;
  elements.rememberMe.checked = Boolean(rememberedUsername);
}

function parseMenuItems(itemsRaw) {
  const items = [];
  for (const item of itemsRaw || []) {
    if (typeof item === "string") {
      items.push({ text: item, id: null, sound: null });
    } else {
      items.push({ text: item?.text || "", id: item?.id ?? null, sound: item?.sound ?? null });
    }
  }
  return items;
}

function sendMenuSelection(selectionIndex) {
  const menu = store.state.currentMenu;
  const item = menu.items[selectionIndex];
  if (!item) {
    return;
  }
  const packet = {
    type: "menu",
    menu_id: menu.menuId,
    selection: selectionIndex + 1,
  };
  if (item.id !== null && item.id !== undefined) {
    packet.selection_id = item.id;
  }
  network.send(packet);
}

function sendEscape() {
  network.send({
    type: "escape",
    menu_id: store.state.currentMenu.menuId,
  });
}

function sendKeybind(payload) {
  network.send({ type: "keybind", ...payload });
}

function sendListOnline() {
  network.send({ type: "list_online" });
}

function sendListOnlineWithGames() {
  if (store.state.currentMenu.menuId === "online_users") {
    return;
  }
  network.send({ type: "list_online_with_games" });
}

function adjustAmbienceVolume(deltaPercent) {
  const current = audio.getAmbienceVolumePercent();
  const next = clampPercent(current + deltaPercent, current);
  audio.setAmbienceVolumePercent(next);
  saveStoredPercent(AMBIENCE_VOLUME_KEY, next);
  a11y.announce(`Ambience: ${next}%`, { assertive: true });
}

function adjustMusicVolume(deltaPercent) {
  const current = audio.getMusicVolumePercent();
  const next = clampPercent(current + deltaPercent, current);
  audio.setMusicVolumePercent(next);
  saveStoredPercent(MUSIC_VOLUME_KEY, next);
  a11y.announce(`Music: ${next}%`, { assertive: true });
}

function closeInlineInput({ returnFocus = true } = {}) {
  pendingInlineInput = null;
  elements.inlineInput.hidden = true;
  elements.inlineInputPrompt.textContent = "";
  elements.inlineInputValue.value = "";
  elements.inlineInputValue.readOnly = false;
  if (returnFocus && store.state.connection.authenticated) {
    elements.menuList.focus();
  }
}

function submitInlineInput(text) {
  if (!pendingInlineInput) {
    return;
  }
  network.send({
    type: "editbox",
    input_id: pendingInlineInput.input_id,
    text,
  });
  focusMenuOnNextMenuPacket = true;
  closeInlineInput({ returnFocus: false });
}

function showInlineInput(packet) {
  pendingInlineInput = packet;
  const promptText = packet.prompt || "Enter value";
  elements.inlineInputPrompt.textContent = promptText;
  elements.inlineInputValue.value = packet.default_value || "";
  elements.inlineInputValue.readOnly = Boolean(packet.read_only);
  elements.inlineInputValue.setAttribute("aria-label", promptText);
  elements.inlineInput.hidden = false;
  requestAnimationFrame(() => {
    elements.inlineInputValue.focus();
    elements.inlineInputValue.select();
  });
}

function openLoginDialog() {
  if (!elements.loginDialog.open) {
    elements.loginDialog.showModal();
  }
  applyRememberedUsernameToLoginForm();
  elements.password.value = "";
  elements.username.focus();
}

function closeLoginDialog() {
  if (elements.loginDialog.open) {
    elements.loginDialog.close();
  }
}

function installInGameTabTrap() {
  document.addEventListener("keydown", (event) => {
    if (event.key !== "Tab") {
      return;
    }
    if (!store.state.connection.authenticated) {
      return;
    }
    if (elements.loginDialog.open || elements.inputDialog.open) {
      return;
    }

    const targets = pendingInlineInput
      ? [elements.menuList, elements.history, elements.chatInput, elements.inlineInputValue]
      : [elements.menuList, elements.history, elements.chatInput];
    const activeIndex = targets.indexOf(document.activeElement);
    if (activeIndex === -1) {
      return;
    }
    event.preventDefault();
    const delta = event.shiftKey ? -1 : 1;
    const nextIndex = (activeIndex + delta + targets.length) % targets.length;
    targets[nextIndex].focus();
  });
}

function installFocusHotkeys() {
  document.addEventListener("keydown", (event) => {
    if (!event.altKey || event.ctrlKey || event.shiftKey || event.metaKey) {
      return;
    }
    if (!store.state.connection.authenticated) {
      return;
    }
    if (elements.loginDialog.open || elements.inputDialog.open) {
      return;
    }

    const key = event.key.toLowerCase();
    if (key === "m") {
      event.preventDefault();
      elements.menuList.focus();
      return;
    }
    if (key === "c") {
      event.preventDefault();
      elements.chatInput.focus();
      return;
    }
    if (key === "h") {
      event.preventDefault();
      elements.history.focus();
    }
  });
}

function installDialogTabTrap(dialogEl, focusTargets) {
  dialogEl.addEventListener("keydown", (event) => {
    if (event.key !== "Tab" || !dialogEl.open) {
      return;
    }

    const targets = focusTargets.filter((el) => el && !el.disabled);
    if (!targets.length) {
      return;
    }

    const currentIndex = targets.indexOf(document.activeElement);
    event.preventDefault();

    if (currentIndex === -1) {
      targets[0].focus();
      return;
    }

    const delta = event.shiftKey ? -1 : 1;
    const nextIndex = (currentIndex + delta + targets.length) % targets.length;
    targets[nextIndex].focus();
  });
}

function handlePacket(packet) {
  switch (packet.type) {
    case "authorize_success": {
      store.setConnection({ authenticated: true, status: "authenticated", lastError: "" });
      if (elements.rememberMe.checked) {
        saveRememberedUsername(packet.username || elements.username.value);
      } else {
        clearRememberedUsername();
      }
      setStatus(`Connected as ${packet.username} (${packet.version})`);
      closeLoginDialog();
      setConnectedUi(true);
      historyView.addEntry(`Connected as ${packet.username} (server ${packet.version})`, {
        buffer: "activity",
      });
      elements.menuList.focus();
      break;
    }
    case "menu": {
      const items = parseMenuItems(packet.items);
      let selection = items.length > 0 ? 0 : 0;

      if (packet.selection_id) {
        const byId = items.findIndex((item) => item.id === packet.selection_id);
        if (byId >= 0) {
          selection = byId;
        }
      } else if (typeof packet.position === "number") {
        selection = Math.max(0, Math.min(items.length - 1, packet.position));
      }

      store.setMenu({
        menuId: packet.menu_id,
        items,
        selection,
        multiletterEnabled: packet.multiletter_enabled ?? true,
        escapeBehavior: packet.escape_behavior ?? "keybind",
        gridEnabled: packet.grid_enabled ?? false,
        gridWidth: packet.grid_width ?? 1,
      });
      if (focusMenuOnNextMenuPacket) {
        focusMenuOnNextMenuPacket = false;
        requestAnimationFrame(() => {
          elements.menuList.focus();
        });
      }
      break;
    }
    case "speak": {
      const text = packet.text || "";
      if (!text) {
        return;
      }
      historyView.addEntry(text, {
        buffer: packet.buffer || "misc",
        announce: !packet.muted,
      });
      break;
    }
    case "chat": {
      const prefix = packet.convo === "global" ? `${packet.sender} globally` : packet.sender;
      const line = `${prefix}: ${packet.message}`;
      historyView.addEntry(line, { buffer: "chats", announce: true });
      audio.playSound({ name: packet.convo === "global" ? "chat.ogg" : "chatlocal.ogg" });
      break;
    }
    case "play_sound": {
      audio.playSound(packet);
      break;
    }
    case "play_music": {
      audio.playMusic(packet);
      break;
    }
    case "stop_music": {
      audio.stopMusic();
      break;
    }
    case "play_ambience": {
      audio.playAmbience(packet);
      break;
    }
    case "stop_ambience": {
      audio.stopAmbience();
      break;
    }
    case "request_input": {
      showInlineInput(packet);
      break;
    }
    case "clear_ui": {
      closeInlineInput({ returnFocus: false });
      store.clearUi();
      break;
    }
    case "disconnect": {
      store.setConnection({ authenticated: false, status: "disconnected" });
      setStatus("Disconnected", true);
      audio.stopAll();
      closeInlineInput({ returnFocus: false });
      setConnectedUi(false);
      openLoginDialog();
      historyView.addEntry("Disconnected by server.", {
        buffer: "activity",
        assertive: true,
      });
      break;
    }
    case "update_options_lists": {
      store.setServerOptions({
        games: packet.games || [],
        languages: packet.languages || {},
      });
      break;
    }
    default: {
      break;
    }
  }
}

function installAudioUnlock() {
  const unlockOnce = async () => {
    if (store.state.audioUnlocked) {
      return;
    }
    const unlocked = await audio.unlock();
    if (unlocked) {
      store.setAudioUnlocked(true);
    }
  };

  const events = ["pointerdown", "keydown"];
  for (const eventName of events) {
    window.addEventListener(eventName, unlockOnce, { once: true, passive: true });
  }
}

async function bootstrap() {
  renderVersion();
  const validator = await loadPacketValidator();

  network = createNetworkClient({
    validator,
    onStatus: (status) => {
      if (status === "connecting") {
        setStatus("Connecting...");
        setConnectedUi(false);
      } else if (status === "connected") {
        setStatus("Connected. Authorizing...");
      } else if (status === "disconnected") {
        setStatus("Disconnected");
        audio.stopAll();
        closeInlineInput({ returnFocus: false });
        setConnectedUi(false);
        openLoginDialog();
      } else if (status === "error") {
        setStatus("Connection error", true);
        audio.stopAll();
        closeInlineInput({ returnFocus: false });
        setConnectedUi(false);
        openLoginDialog();
      }
    },
    onPacket: handlePacket,
    onError: (message) => {
      historyView.addEntry(message, { buffer: "activity", announce: true, assertive: true });
      setStatus(message, true);
    },
  });

  createChat({
    chatFormEl: elements.chatForm,
    chatInputEl: elements.chatInput,
    onSend: ({ convo, message }) => {
      network.send({
        type: "chat",
        convo,
        message,
        language: "English",
      });
    },
  });

  installKeybinds({
    store,
    menuView,
    sendMenuSelection,
    sendEscape,
    sendKeybind,
    sendListOnline,
    sendListOnlineWithGames,
    onPreviousBuffer: () => historyView.previousBuffer(),
    onNextBuffer: () => historyView.nextBuffer(),
    onFirstBuffer: () => historyView.firstBuffer(),
    onLastBuffer: () => historyView.lastBuffer(),
    onOlderMessage: () => historyView.olderMessage(),
    onNewerMessage: () => historyView.newerMessage(),
    onOldestMessage: () => historyView.oldestMessage(),
    onNewestMessage: () => historyView.newestMessage(),
    onToggleBufferMute: () => historyView.toggleCurrentBufferMute(),
    onAmbienceDown: () => adjustAmbienceVolume(-10),
    onAmbienceUp: () => adjustAmbienceVolume(10),
    onMusicDown: () => adjustMusicVolume(-10),
    onMusicUp: () => adjustMusicVolume(10),
    isModalOpen: () => elements.loginDialog.open || elements.inputDialog.open,
  });

  elements.connectForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (store.state.connection.status === "connecting") {
      return;
    }
    const serverUrl = getDefaultServerUrl();
    const username = normalizeUsername(elements.username.value);
    const password = elements.password.value;

    if (!username) {
      setStatus("Username is required.", true);
      return;
    }

    elements.username.value = username;
    elements.loginDialog.returnValue = "connect";
    store.setConnection({ serverUrl, username, status: "connecting", authenticated: false });
    network.connect({ serverUrl, username, password });
  });

  elements.disconnectBtn.addEventListener("click", () => {
    network.disconnect();
    store.setConnection({ status: "disconnected", authenticated: false });
    setStatus("Disconnected");
    audio.stopAll();
    closeInlineInput({ returnFocus: false });
    setConnectedUi(false);
    openLoginDialog();
  });

  elements.openLoginBtn.addEventListener("click", () => {
    openLoginDialog();
  });

  elements.menuList.addEventListener("click", () => {
    elements.menuList.focus();
  });
  elements.inlineInputSubmit.addEventListener("click", () => {
    submitInlineInput(elements.inlineInputValue.value);
  });
  elements.inlineInputCancel.addEventListener("click", () => {
    submitInlineInput("");
  });
  elements.inlineInputValue.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      event.preventDefault();
      event.stopPropagation();
      submitInlineInput("");
      return;
    }
    if (event.key === "Enter" && !event.shiftKey && !event.ctrlKey && !event.altKey) {
      event.preventDefault();
      event.stopPropagation();
      submitInlineInput(elements.inlineInputValue.value);
      return;
    }
    const keyCode = event.key.length === 1 ? event.key.charCodeAt(0) : 0;
    const shouldPlayTyping = (
      !elements.inlineInputValue.readOnly
      && keyCode >= 32
      && keyCode <= 126
      && !event.ctrlKey
      && !event.altKey
      && !event.metaKey
    );
    if (shouldPlayTyping) {
      const soundNum = Math.floor(Math.random() * 4) + 1;
      audio.playSound({ name: `typing${soundNum}.ogg`, volume: 50 });
    }
  });
  elements.loginDialog.addEventListener("cancel", (event) => {
    event.preventDefault();
  });

  installAudioUnlock();
  installInGameTabTrap();
  installFocusHotkeys();
  installDialogTabTrap(elements.inputDialog, [
    elements.inputValue,
    elements.inputCancel,
    elements.inputSubmit,
  ]);
  setConnectedUi(false);
  openLoginDialog();
}

void bootstrap();
