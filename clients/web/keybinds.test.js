import test from "node:test";
import assert from "node:assert/strict";
import { installKeybinds } from "./keybinds.js";

function installForTarget(target, { multiletterEnabled = true } = {}) {
  let handler;
  globalThis.document = {
    activeElement: target,
    addEventListener(_type, callback) {
      handler = callback;
    },
  };

  const menuElement = { tagName: "UL" };
  const menu = {
    menuId: "game_menu",
    items: [{ id: "play", text: "Play" }],
    selection: 0,
    multiletterEnabled,
    escapeBehavior: "keybind",
    gridEnabled: false,
    gridWidth: 1,
  };
  const sent = [];
  const menuView = {
    getElement: () => menuElement,
    activateSelection() {},
    handleTypeNavigation() {
      throw new Error("Space must not trigger menu search");
    },
    moveSelection() {},
    setSelection() {},
  };

  installKeybinds({
    store: { state: { currentMenu: menu, connection: { authenticated: true } } },
    menuView,
    sendMenuSelection() {},
    sendEscape() {},
    sendKeybind: (payload) => sent.push(payload),
    isModalOpen: () => false,
  });
  return { handler, menuElement, sent };
}

function keyEvent(key) {
  return {
    key,
    altKey: false,
    ctrlKey: false,
    shiftKey: false,
    metaKey: false,
    preventDefault() {},
  };
}

test("Space forwards as a server keybind when multiletter navigation is enabled", () => {
  const { handler, menuElement, sent } = installForTarget(null);
  document.activeElement = menuElement;

  handler(keyEvent(" "));

  assert.equal(sent.length, 1);
  assert.equal(sent[0].key, "space");
});

test("F5 forwards as a server keybind from the focused menu", () => {
  const { handler, menuElement, sent } = installForTarget(null);
  document.activeElement = menuElement;

  handler(keyEvent("F5"));

  assert.equal(sent.length, 1);
  assert.equal(sent[0].key, "f5");
});

test("Escape and Backspace in editable controls stay local", () => {
  const input = { tagName: "INPUT", readOnly: false, disabled: false };
  const { handler, sent } = installForTarget(input);

  handler(keyEvent("Escape"));
  handler(keyEvent("Backspace"));

  assert.deepEqual(sent, []);
});
