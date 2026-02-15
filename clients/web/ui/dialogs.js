export function createInputDialog({ store, dialogEl, promptEl, inputEl, cancelEl, formEl, onSubmit }) {
  function closeDialog() {
    if (dialogEl.open) {
      dialogEl.close();
    }
    store.setPendingInput(null);
  }

  function show(packet) {
    store.setPendingInput(packet);
    promptEl.textContent = packet.prompt || "Enter value";
    inputEl.value = packet.default_value || "";
    inputEl.readOnly = Boolean(packet.read_only);

    if (!dialogEl.open) {
      dialogEl.showModal();
    }
    inputEl.focus();
  }

  cancelEl.addEventListener("click", () => {
    closeDialog();
  });

  formEl.addEventListener("submit", (event) => {
    event.preventDefault();
    const pending = store.state.pendingInput;
    if (!pending) {
      closeDialog();
      return;
    }
    onSubmit({
      input_id: pending.input_id,
      text: inputEl.value,
    });
    closeDialog();
  });

  return { show, closeDialog };
}
