import test from "node:test";
import assert from "node:assert/strict";
import { createStore } from "./store.js";

class FakeNode {
  constructor(tagName) {
    this.tagName = tagName.toUpperCase();
    this.children = [];
    this.dataset = {};
    this.attributes = {};
    this.classList = { toggle() {} };
    this.listeners = {};
    this.parentNode = null;
    this._textContent = "";
  }

  get textContent() {
    return this._textContent;
  }

  set textContent(value) {
    this._textContent = String(value);
    this.children = [];
  }

  get innerHTML() {
    return "";
  }

  set innerHTML(_value) {
    for (const child of this.children) {
      child.parentNode = null;
    }
    this.children = [];
  }

  get firstChild() {
    return this.children[0] || null;
  }

  appendChild(child) {
    if (child.parentNode) {
      child.parentNode.children = child.parentNode.children.filter((item) => item !== child);
    }
    child.parentNode = this;
    this.children.push(child);
    return child;
  }

  insertBefore(child, reference) {
    if (child.parentNode && globalThis.document.activeElement && child.contains(globalThis.document.activeElement)) {
      globalThis.document.activeElement = null;
    }
    if (child.parentNode) {
      child.parentNode.children = child.parentNode.children.filter((item) => item !== child);
    }
    child.parentNode = this;
    const index = reference ? this.children.indexOf(reference) : -1;
    if (index < 0) {
      this.children.push(child);
    } else {
      this.children.splice(index, 0, child);
    }
    return child;
  }

  addEventListener(type, callback) {
    this.listeners[type] = callback;
  }

  setAttribute(name, value) {
    this.attributes[name] = String(value);
  }

  removeAttribute(name) {
    delete this.attributes[name];
  }

  querySelector(selector) {
    if (selector === "button") {
      return this.children.find((child) => child.tagName === "BUTTON") || null;
    }
    return null;
  }

  remove() {
    if (this.parentNode) {
      this.parentNode.children = this.parentNode.children.filter((item) => item !== this);
      this.parentNode = null;
    }
  }

  contains(node) {
    return this === node || this.children.some((child) => child.contains(node));
  }

  focus() {
    globalThis.document.activeElement = this;
  }
}

test("same-menu updates reuse stable rows and new menus replace them", async () => {
  globalThis.window = { matchMedia: () => ({ matches: false }) };
  globalThis.document = { createElement: (tag) => new FakeNode(tag) };
  const { createMenuView } = await import("./ui/menus.js");
  const store = createStore();
  const list = new FakeNode("ul");
  const activated = [];
  createMenuView({ store, listEl: list, onActivate: (_item, index) => activated.push(index) });

  store.setMenu({
    menuId: "game_menu",
    items: [
      { id: "card_a", text: "A", sound: "a.ogg" },
      { id: "card_b", text: "B", sound: "b.ogg" },
    ],
    selection: 1,
  });
  const selectedRow = list.children[1];
  const selectedOptionId = list.attributes["aria-activedescendant"];

  store.setMenu({
    menuId: "game_menu",
    items: [
      { id: "control", text: "Control", sound: "c.ogg" },
      { id: "card_b", text: "B updated", sound: "new.ogg" },
      { id: "card_c", text: "C", sound: "c.ogg" },
    ],
    selection: 1,
  });
  assert.equal(list.children[1], selectedRow);
  assert.equal(list.children[1].id, selectedOptionId);
  assert.equal(list.attributes["aria-activedescendant"], selectedOptionId);
  assert.equal(list.children[1].textContent, "B updated");
  list.children[2].listeners.dblclick();
  assert.deepEqual(activated, [2]);

  store.setMenu({
    menuId: "game_menu",
    items: [
      { id: "card_b", text: "B updated", sound: "new.ogg" },
      { id: "card_c", text: "C", sound: "c.ogg" },
    ],
    selection: 0,
  });
  assert.equal(list.children[0], selectedRow);
  assert.equal(list.attributes["aria-activedescendant"], selectedOptionId);
  selectedRow.listeners.dblclick();
  assert.deepEqual(activated, [2, 0]);

  store.setMenu({ menuId: "main_menu", items: [{ id: "main", text: "Main" }], selection: 0 });
  assert.notEqual(list.children[0], selectedRow);
  assert.notEqual(list.attributes["aria-activedescendant"], selectedOptionId);
});

test("coarse-pointer updates restore focus when a surviving row moves", async () => {
  globalThis.window = { matchMedia: () => ({ matches: true }) };
  globalThis.document = { createElement: (tag) => new FakeNode(tag), activeElement: null };
  const { createMenuView } = await import("./ui/menus.js");
  const store = createStore();
  const list = new FakeNode("ul");
  createMenuView({ store, listEl: list, onActivate() {} });
  store.setMenu({
    menuId: "game_menu",
    items: [{ id: "card_a", text: "A" }, { id: "card_b", text: "B" }],
    selection: 0,
  });
  const focusedButton = list.children[0].querySelector("button");
  focusedButton.focus();

  store.setMenu({
    menuId: "game_menu",
    items: [
      { id: "control", text: "Control" },
      { id: "card_a", text: "A" },
      { id: "card_b", text: "B" },
    ],
    selection: 1,
  });

  assert.equal(list.children[1].querySelector("button"), focusedButton);
  assert.equal(globalThis.document.activeElement, focusedButton);

  // Moving the focused row itself can drop native browser focus.
  store.setMenu({
    menuId: "game_menu",
    items: [
      { id: "card_a", text: "A" },
      { id: "control", text: "Control" },
      { id: "card_b", text: "B" },
    ],
    selection: 0,
  });
  assert.equal(list.children[0].querySelector("button"), focusedButton);
  assert.equal(globalThis.document.activeElement, focusedButton);

  const chatInput = new FakeNode("input");
  chatInput.focus();
  store.setMenu({
    menuId: "game_menu",
    items: [{ id: "card_b", text: "B" }, { id: "card_a", text: "A" }],
    selection: 1,
  });
  assert.equal(globalThis.document.activeElement, chatInput);
});
