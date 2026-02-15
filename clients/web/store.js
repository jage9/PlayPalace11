export function createStore() {
  const state = {
    connection: {
      status: "disconnected",
      authenticated: false,
      serverUrl: "",
      username: "",
      lastError: "",
    },
    currentMenu: {
      menuId: null,
      items: [],
      selection: 0,
      multiletterEnabled: true,
      escapeBehavior: "keybind",
      gridEnabled: false,
      gridWidth: 1,
    },
    historyBuffers: {
      all: [],
      misc: [],
      activity: [],
      table: [],
      chats: [],
    },
    historyBuffer: "all",
    audioUnlocked: false,
    pendingInput: null,
    serverOptions: {
      games: [],
      languages: {},
    },
  };

  const listeners = new Set();

  function notify() {
    for (const listener of listeners) {
      listener(state);
    }
  }

  return {
    state,
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
    setConnection(patch) {
      Object.assign(state.connection, patch);
      notify();
    },
    setMenu(menuPatch) {
      Object.assign(state.currentMenu, menuPatch);
      notify();
    },
    addHistory(buffer, text) {
      if (!state.historyBuffers[buffer]) {
        state.historyBuffers[buffer] = [];
      }
      state.historyBuffers[buffer].push(text);
      if (buffer !== "all") {
        state.historyBuffers.all.push(text);
      }
      notify();
    },
    clearUi() {
      state.currentMenu = {
        menuId: null,
        items: [],
        selection: 0,
        multiletterEnabled: true,
        escapeBehavior: "keybind",
        gridEnabled: false,
        gridWidth: 1,
      };
      notify();
    },
    setHistoryBuffer(buffer) {
      state.historyBuffer = buffer;
      notify();
    },
    setAudioUnlocked(unlocked) {
      state.audioUnlocked = unlocked;
      notify();
    },
    setPendingInput(inputState) {
      state.pendingInput = inputState;
      notify();
    },
    setServerOptions(patch) {
      Object.assign(state.serverOptions, patch);
      notify();
    },
  };
}
