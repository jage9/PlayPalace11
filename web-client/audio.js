function isAbsoluteUrl(path) {
  return /^https?:\/\//i.test(path);
}

function toSoundUrl(name, soundBaseUrl) {
  if (!name) {
    return "";
  }
  if (isAbsoluteUrl(name) || name.startsWith("/")) {
    return name;
  }
  const base = String(soundBaseUrl || "./sounds").replace(/\/+$/, "");
  return `${base}/${name}`;
}

export function createAudioEngine(options = {}) {
  const soundBaseUrl = options.soundBaseUrl || "./sounds";
  const AudioCtx = window.AudioContext || window.webkitAudioContext;
  const context = AudioCtx ? new AudioCtx() : null;

  let effectsGain = null;
  let musicGain = null;
  let ambienceGain = null;
  let currentMusic = null;
  let currentMusicName = "";
  let currentMusicLooping = true;
  const activeEffects = new Set();

  if (context) {
    effectsGain = context.createGain();
    musicGain = context.createGain();
    ambienceGain = context.createGain();

    effectsGain.gain.value = 1.0;
    musicGain.gain.value = 0.2;
    ambienceGain.gain.value = 1.0;

    effectsGain.connect(context.destination);
    musicGain.connect(context.destination);
    ambienceGain.connect(context.destination);
  }

  async function unlock() {
    if (!context) {
      return false;
    }
    if (context.state !== "running") {
      await context.resume();
    }
    return context.state === "running";
  }

  function connectElement(audio, gainNode, panValue = 0) {
    if (!context || !gainNode) {
      return;
    }

    const source = context.createMediaElementSource(audio);
    if (typeof context.createStereoPanner === "function") {
      const panner = context.createStereoPanner();
      panner.pan.value = Math.max(-1, Math.min(1, panValue));
      source.connect(panner);
      panner.connect(gainNode);
      return;
    }
    source.connect(gainNode);
  }

  function playSound(packet) {
    const name = packet.name || packet.sound || "";
    const url = toSoundUrl(name, soundBaseUrl);
    if (!url) {
      return;
    }

    const audio = new Audio(url);
    audio.preload = "auto";
    audio.volume = Math.max(0, Math.min(1, (packet.volume ?? 100) / 100));
    audio.playbackRate = Math.max(0.5, Math.min(2, (packet.pitch ?? 100) / 100));

    activeEffects.add(audio);
    audio.addEventListener("ended", () => {
      activeEffects.delete(audio);
    });
    audio.addEventListener("pause", () => {
      if (audio.currentTime === 0 || audio.ended) {
        activeEffects.delete(audio);
      }
    });

    try {
      connectElement(audio, effectsGain, (packet.pan ?? 0) / 100);
      void audio.play();
    } catch {
      // Ignore autoplay/stream failures before unlock.
    }
  }

  function playMusic(packet) {
    const name = packet.name || packet.music || "";
    const url = toSoundUrl(name, soundBaseUrl);
    if (!url) {
      return;
    }
    const looping = packet.looping ?? true;

    // Match desktop behavior: don't restart music if the same track is already active.
    if (currentMusic && currentMusicName === name && currentMusicLooping === looping) {
      if (currentMusic.paused) {
        void currentMusic.play().catch(() => {});
      }
      return;
    }

    stopMusic();

    const audio = new Audio(url);
    audio.preload = "auto";
    audio.loop = looping;
    audio.volume = 1.0;

    try {
      connectElement(audio, musicGain);
      void audio.play();
      currentMusic = audio;
      currentMusicName = name;
      currentMusicLooping = looping;
    } catch {
      currentMusic = audio;
      currentMusicName = name;
      currentMusicLooping = looping;
    }
  }

  function stopMusic() {
    if (!currentMusic) {
      return;
    }
    try {
      currentMusic.pause();
      currentMusic.currentTime = 0;
    } catch {
      // Ignore stop failures.
    }
    currentMusic = null;
    currentMusicName = "";
    currentMusicLooping = true;
  }

  function stopAll() {
    stopMusic();
    for (const audio of activeEffects) {
      try {
        audio.pause();
        audio.currentTime = 0;
      } catch {
        // Ignore per-element stop failures.
      }
    }
    activeEffects.clear();
  }

  return {
    unlock,
    playSound,
    playMusic,
    stopMusic,
    stopAll,
  };
}
