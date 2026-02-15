export function createChat({ chatFormEl, chatInputEl, onSend }) {
  chatFormEl.addEventListener("submit", (event) => {
    event.preventDefault();
    const raw = chatInputEl.value.trim();
    if (!raw) {
      return;
    }

    let convo = "local";
    let message = raw;
    if (raw.startsWith(".")) {
      convo = "global";
      message = raw.slice(1).trim();
    }

    if (!message) {
      return;
    }

    onSend({ convo, message });
    chatInputEl.value = "";
  });
}
