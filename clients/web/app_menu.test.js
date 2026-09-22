import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import vm from "node:vm";

function loadMenuHandler() {
  const source = fs.readFileSync(new URL("./app.js", import.meta.url), "utf8");
  const parseStart = source.indexOf("function parseMenuItems");
  const parseEnd = source.indexOf("function canOpenActionsPopup", parseStart);
  const handlerStart = source.indexOf("function handlePacket");
  const handlerEnd = source.indexOf("function installAudioUnlock", handlerStart);
  const state = {
    currentMenu: {
      menuId: null,
      items: [],
      selection: 0,
      multiletterEnabled: true,
      escapeBehavior: "keybind",
      gridEnabled: false,
      gridWidth: 1,
    },
  };
  const context = {
    console,
    store: {
      state,
      setMenu(patch) {
        Object.assign(state.currentMenu, patch);
      },
    },
    elements: { menuList: { focus() {} } },
    updateActionsButtonVisibility() {},
    playMenuSelectionSound() {},
    requestAnimationFrame(callback) { callback(); },
    openActionsDialogForMenu() {},
    handleAuthorizeSuccess() {},
  };
  context.globalThis = context;
  vm.runInNewContext(
    `let pendingActionsMenuRequest = false;\n` +
      `let focusMenuOnNextMenuPacket = false;\n` +
      `${source.slice(parseStart, parseEnd)}\n` +
      `${source.slice(handlerStart, handlerEnd)}\n` +
      `globalThis.handlePacket = handlePacket;`,
    context,
  );
  return { context, state };
}

test("menu packet updates preserve same-menu settings and selection identity", () => {
  const { context, state } = loadMenuHandler();

  context.handlePacket({
    type: "menu",
    menu_id: "game_menu",
    items: [{ text: "One", id: "one" }, { text: "Two", id: "two" }],
    selection_id: "two",
    multiletter_enabled: false,
    escape_behavior: "escape_event",
    grid_enabled: true,
    grid_width: 3,
  });
  context.handlePacket({
    type: "menu",
    menu_id: "game_menu",
    items: [{ text: "Two", id: "two" }, { text: "Three", id: "three" }],
  });

  assert.equal(state.currentMenu.selection, 0);
  assert.equal(state.currentMenu.multiletterEnabled, false);
  assert.equal(state.currentMenu.escapeBehavior, "escape_event");
  assert.equal(state.currentMenu.gridEnabled, true);
  assert.equal(state.currentMenu.gridWidth, 3);
});

test("explicit settings and new menus reset partial-update defaults", () => {
  const { context, state } = loadMenuHandler();

  context.handlePacket({
    type: "menu",
    menu_id: "game_menu",
    items: [{ text: "One", id: "one" }],
    multiletter_enabled: false,
    escape_behavior: "escape_event",
    grid_enabled: true,
    grid_width: 3,
  });
  context.handlePacket({
    type: "menu",
    menu_id: "game_menu",
    items: [{ text: "One", id: "one" }],
    multiletter_enabled: false,
    escape_behavior: "keybind",
    grid_enabled: false,
    grid_width: 1,
  });
  assert.equal(state.currentMenu.multiletterEnabled, false);
  assert.equal(state.currentMenu.escapeBehavior, "keybind");
  assert.equal(state.currentMenu.gridEnabled, false);
  assert.equal(state.currentMenu.gridWidth, 1);

  context.handlePacket({
    type: "menu",
    menu_id: "main_menu",
    items: [{ text: "Main", id: "main" }],
  });
  assert.equal(state.currentMenu.multiletterEnabled, true);
  assert.equal(state.currentMenu.escapeBehavior, "keybind");
  assert.equal(state.currentMenu.gridEnabled, false);
  assert.equal(state.currentMenu.gridWidth, 1);
});
