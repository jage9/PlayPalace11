import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import vm from "node:vm";

function makeNode() {
  return {
    children: [],
    appendChild(child) {
      this.children.push(child);
    },
    addEventListener() {},
    querySelector() {
      return null;
    },
    focus() {
      this.focused = true;
    },
    className: "",
    textContent: "",
    type: "",
  };
}

function loadActionsFunctions() {
  const source = fs.readFileSync(new URL("./app.js", import.meta.url), "utf8");
  const start = source.indexOf("function canOpenActionsPopup()");
  const end = source.indexOf("function handleAuthorizeSuccess", start);
  const sent = [];
  const actionsList = makeNode();
  const actionsDialog = {
    open: false,
    showModal() {
      this.open = true;
    },
    close() {
      this.open = false;
    },
  };
  const menuList = makeNode();
  const context = {
    console,
    document: { createElement: () => makeNode() },
    requestAnimationFrame: (callback) => callback(),
    store: {
      state: {
        connection: { authenticated: true },
        currentMenu: {
          menuId: "turn_menu",
          items: [{ id: "play", text: "Play" }],
          selection: 0,
        },
      },
    },
    elements: {
      actionsList,
      actionsDialog,
      actionsCancel: makeNode(),
      actionsBtn: makeNode(),
      gameShell: { hidden: false },
      menuList,
    },
    network: { send: (packet) => sent.push(packet) },
    menuView: { setSelection() {}, activateSelection() {} },
    pendingActionsMenuRequest: false,
  };
  context.globalThis = context;
  vm.runInNewContext(
    `let pendingActionsMenuRequest = false;\nlet activeActionsMenu = null;\n${source.slice(start, end)}`,
    context,
  );
  return { context, sent, actionsDialog, menuList };
}

test("Actions button requests the server F5 keybind", () => {
  const { context, sent } = loadActionsFunctions();

  context.requestActionsDialog();

  assert.deepEqual(JSON.parse(JSON.stringify(sent)), [{
    type: "keybind",
    key: "f5",
    control: false,
    alt: false,
    shift: false,
    menu_id: "turn_menu",
    menu_index: 1,
    menu_item_id: "play",
  }]);
});

test("Actions dialog cancel sends go_back and restores menu focus", () => {
  const { context, sent, actionsDialog, menuList } = loadActionsFunctions();
  context.openActionsDialogForMenu({
    menuId: "actions_menu",
    items: [{ id: "play", text: "Play" }, { id: "go_back", text: "Back" }],
  });
  sent.length = 0;
  const event = { prevented: false, preventDefault() { this.prevented = true; } };

  context.handleActionsDialogCancel(event);

  assert.equal(event.prevented, true);
  assert.deepEqual(JSON.parse(JSON.stringify(sent)), [{
    type: "menu",
    menu_id: "actions_menu",
    selection_id: "go_back",
  }]);
  assert.equal(actionsDialog.open, false);
  assert.equal(menuList.focused, true);
});
