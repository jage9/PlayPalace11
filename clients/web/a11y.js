export function createA11y({ politeEl, assertiveEl }) {
  let announcementNonce = 0;
  let latestPoliteId = 0;
  let latestAssertiveId = 0;
  let lastAnnouncementText = "";
  let lastAnnouncementAt = 0;

  function announce(text, options = {}) {
    const { assertive = false } = options;
    const target = assertive ? assertiveEl : politeEl;
    if (!target) {
      return;
    }
    announcementNonce += 1;
    const normalized = String(text)
      .replace(/\s*\n+\s*/g, " ")
      .replace(/\s{2,}/g, " ")
      .trim();
    const now = performance.now();
    // VoiceOver can double-speak when identical live-region updates happen in quick succession.
    if (normalized && normalized === lastAnnouncementText && now - lastAnnouncementAt < 700) {
      return;
    }
    lastAnnouncementText = normalized;
    lastAnnouncementAt = now;
    const id = announcementNonce;
    if (assertive) {
      latestAssertiveId = id;
    } else {
      latestPoliteId = id;
    }
    requestAnimationFrame(() => {
      if (assertive && id !== latestAssertiveId) {
        return;
      }
      if (!assertive && id !== latestPoliteId) {
        return;
      }
      // Reinsert as a fresh node so identical repeated text can still be announced.
      const span = document.createElement("span");
      span.setAttribute("data-announce-id", String(announcementNonce));
      span.textContent = normalized;
      target.replaceChildren(span);
    });
  }

  return { announce };
}
