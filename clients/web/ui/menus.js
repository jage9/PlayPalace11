export function createMenuView({
  store,
  listEl,
  onActivate,
  onSelectionSound,
  onActivateSound,
  onBoundaryRepeat,
}) {
  let renderVersion = 0;
  let lastStructureSnapshot = "";
  let lastSelection = -1;
  const isCoarsePointer = window.matchMedia("(pointer: coarse)").matches;
  const useActiveDescendant = !isCoarsePointer;
  let searchBuffer = "";
  let lastTypeTime = 0;
  const typeTimeoutSeconds = 0.15;

  function menuStructureSnapshot(menu) {
    const itemsSnapshot = (menu.items || [])
      .map((item) => `${item?.id ?? ""}|${item?.text ?? ""}|${item?.sound ?? ""}`)
      .join("||");
    return [
      menu.menuId ?? "",
      menu.multiletterEnabled ? "1" : "0",
      menu.escapeBehavior ?? "",
      menu.gridEnabled ? "1" : "0",
      menu.gridWidth ?? 1,
      itemsSnapshot,
    ].join("::");
  }

  function currentOptionId(key) {
    return `menu-option-${renderVersion}-${encodeURIComponent(key)}`;
  }

  function getItemKeys(items) {
    const idCounts = new Map();
    for (const item of items) {
      if (item?.id !== null && item?.id !== undefined) {
        const id = String(item.id);
        idCounts.set(id, (idCounts.get(id) || 0) + 1);
      }
    }
    return items.map((item, index) => {
      const id = item?.id;
      if (id !== null && id !== undefined && idCounts.get(String(id)) === 1) {
        return `id:${id}`;
      }
      return `index:${index}`;
    });
  }

  function setSelection(next) {
    const count = store.state.currentMenu.items.length;
    if (!count) {
      store.setMenu({ selection: 0 });
      return;
    }
    const bounded = Math.max(0, Math.min(count - 1, next));
    if (bounded === store.state.currentMenu.selection) {
      return;
    }
    store.setMenu({ selection: bounded });
    if (onSelectionSound) {
      onSelectionSound(store.state.currentMenu.items[bounded], bounded);
    }
  }

  function moveSelection(delta) {
    const menu = store.state.currentMenu;
    const count = menu.items.length;
    if (!count) {
      return;
    }
    const current = menu.selection;
    const bounded = Math.max(0, Math.min(count - 1, current + delta));
    if (bounded === current) {
      if (onSelectionSound) {
        onSelectionSound(menu.items[current], current);
      }
      const currentItem = menu.items[current];
      if (currentItem && onBoundaryRepeat) {
        onBoundaryRepeat(currentItem.text);
      }
      return;
    }
    setSelection(bounded);
  }

  function handleTypeNavigation(char) {
    const menu = store.state.currentMenu;
    const count = menu.items.length;
    if (!count || !char) {
      return;
    }

    const now = performance.now() / 1000;
    if (now - lastTypeTime > typeTimeoutSeconds) {
      searchBuffer = "";
    }
    searchBuffer += char.toLowerCase();
    lastTypeTime = now;

    const current = menu.selection;
    const currentItem = menu.items[current];
    const currentText = String(currentItem?.text || "").toLowerCase();

    // Match desktop behavior: if extended buffer already matches current item, stay on it.
    if (searchBuffer.length > 1 && currentText.startsWith(searchBuffer)) {
      return;
    }

    const start = current >= 0 ? current : 0;
    for (let offset = 1; offset <= count; offset += 1) {
      const i = (start + offset) % count;
      const text = String(menu.items[i]?.text || "").toLowerCase();
      if (text.startsWith(searchBuffer)) {
        setSelection(i);
        return;
      }
    }
  }

  function activateSelection() {
    const menu = store.state.currentMenu;
    if (!menu.items.length) {
      return;
    }
    const item = menu.items[menu.selection];
    if (!item) {
      return;
    }
    if (onActivateSound) {
      onActivateSound();
    }
    onActivate(item, menu.selection);
  }

  function applySelection(selectionIndex) {
    const menu = store.state.currentMenu;
    const boundedSelection = Math.max(0, Math.min(menu.items.length - 1, selectionIndex));
    const children = listEl.children;
    for (let i = 0; i < children.length; i += 1) {
      const li = children[i];
      const active = i === boundedSelection;
      if (!isCoarsePointer) {
        li.setAttribute("aria-selected", active ? "true" : "false");
      }
      li.classList.toggle("active", active);
    }
    if (useActiveDescendant && menu.items.length > 0 && children[boundedSelection]) {
      listEl.setAttribute("aria-activedescendant", children[boundedSelection].id);
    } else {
      listEl.removeAttribute("aria-activedescendant");
    }
    lastSelection = boundedSelection;
  }

  function createItemNode(item, key) {
    const li = document.createElement("li");
    li.id = currentOptionId(key);
    li.className = "menu-item";
    if (isCoarsePointer) {
      li.setAttribute("role", "presentation");
    } else {
      li.setAttribute("role", "option");
    }
    li.dataset.menuItemKey = key;
    if (isCoarsePointer) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "menu-item-touch";
      button.textContent = item.text;
      button.addEventListener("click", () => {
        const currentIndex = Number(li.dataset.index);
        setSelection(currentIndex);
        activateSelection();
      });
      li.appendChild(button);
    } else {
      li.textContent = item.text;
      li.addEventListener("click", () => {
        const currentIndex = Number(li.dataset.index);
        const wasSelected = currentIndex === store.state.currentMenu.selection;
        setSelection(currentIndex);
        if (wasSelected) {
          activateSelection();
        }
      });
      li.addEventListener("dblclick", () => {
        const currentIndex = Number(li.dataset.index);
        setSelection(currentIndex);
        activateSelection();
      });
    }
    return li;
  }

  function updateItemNode(li, item, index, key) {
    li.dataset.index = String(index);
    li.dataset.menuItemKey = key;
    if (isCoarsePointer) {
      const button = li.querySelector("button");
      if (button && button.textContent !== item.text) {
        button.textContent = item.text;
      }
    } else if (li.firstChild) {
      if (li.firstChild.nodeValue !== item.text) {
        li.firstChild.nodeValue = item.text;
      }
    } else if (li.textContent !== item.text) {
      li.textContent = item.text;
    }
  }

  function reconcileItems() {
    const menu = store.state.currentMenu;
    const keys = getItemKeys(menu.items);
    const oldChildren = [...listEl.children];
    const oldByKey = new Map(oldChildren.map((child) => [child.dataset.menuItemKey, child]));
    const used = new Set();
    const activeElement = document.activeElement;
    const focusedRow = oldChildren.find((child) => child.contains?.(activeElement));
    if (isCoarsePointer) {
      listEl.removeAttribute("role");
      listEl.removeAttribute("aria-label");
    } else {
      listEl.setAttribute("role", "listbox");
    }
    menu.items.forEach((item, index) => {
      const key = keys[index];
      const li = oldByKey.get(key) || createItemNode(item, key);
      updateItemNode(li, item, index, key);
      used.add(li);
    });
    for (const child of oldChildren) {
      if (!used.has(child)) {
        child.remove();
      }
    }
    const desiredChildren = [...used];
    for (let index = 0; index < desiredChildren.length; index += 1) {
      const li = desiredChildren[index];
      if (listEl.children[index] !== li) {
        listEl.insertBefore(li, listEl.children[index] || null);
      }
    }
    if (focusedRow && used.has(focusedRow) && document.activeElement !== activeElement) {
      activeElement.focus?.({ preventScroll: true });
    }
    applySelection(menu.selection);
  }

  function renderFull() {
    renderVersion += 1;
    searchBuffer = "";
    lastTypeTime = 0;
    listEl.innerHTML = "";
    reconcileItems();
  }

  listEl.addEventListener("focus", () => {
    applySelection(store.state.currentMenu.selection);
  });

  store.subscribe(() => {
    const menu = store.state.currentMenu;
    const nextStructureSnapshot = menuStructureSnapshot(menu);
    if (nextStructureSnapshot !== lastStructureSnapshot) {
      lastStructureSnapshot = nextStructureSnapshot;
      if (menu.menuId !== lastRenderedMenuId) {
        lastRenderedMenuId = menu.menuId;
        renderFull();
      } else {
        reconcileItems();
      }
      return;
    }
    if (menu.selection !== lastSelection) {
      applySelection(menu.selection);
    }
  });
  let lastRenderedMenuId = store.state.currentMenu.menuId;
  lastStructureSnapshot = menuStructureSnapshot(store.state.currentMenu);
  renderFull();

  return {
    setSelection,
    moveSelection,
    handleTypeNavigation,
    activateSelection,
    getElement() {
      return listEl;
    },
    getCurrentItemText() {
      const menu = store.state.currentMenu;
      if (!menu.items.length) {
        return "";
      }
      const currentItem = menu.items[Math.max(0, Math.min(menu.selection, menu.items.length - 1))];
      return currentItem?.text || "";
    },
  };
}
