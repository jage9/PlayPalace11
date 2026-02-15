function isAbsoluteUrl(path) {
  return /^https?:\/\//i.test(path);
}

function isCrossOriginUrl(url) {
  try {
    const target = new URL(url, window.location.href);
    return target.origin !== window.location.origin;
  } catch {
    return false;
  }
}

function createAudioElement(url) {
  const audio = new Audio();
  if (isCrossOriginUrl(url)) {
    // Required for Web Audio processing of cross-origin media.
    audio.crossOrigin = "anonymous";
  }
  audio.src = url;
  return audio;
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
  let pendingMusicPacket = null;
  let currentAmbience = null;
  let currentAmbienceLoop = null;
  let currentAmbienceLoopName = "";
  let pendingAmbiencePacket = null;
  const pendingEffectPackets = [];
  const MAX_PENDING_EFFECTS = 24;
  const activeEffects = new Set();
  let muted = false;

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
      retryPendingPlayback();
      return false;
    }
    if (context.state !== "running") {
      await context.resume();
    }
    retryPendingPlayback();
    return context.state === "running";
  }

  function safePlay(audio, { onRejected } = {}) {
    audio.muted = muted;
    try {
      const maybePromise = audio.play();
      if (maybePromise && typeof maybePromise.catch === "function") {
        maybePromise.catch(() => {
          if (onRejected) {
            onRejected();
          }
        });
      }
    } catch {
      if (onRejected) {
        onRejected();
      }
    }
  }

  function connectElement(audio, gainNode, panValue = 0, url = "") {
    if (!context || !gainNode) {
      return false;
    }

    if (isCrossOriginUrl(url)) {
      // Cross-origin media can be silenced by Web Audio without CORS;
      // let the element play directly as a fallback.
      return false;
    }

    try {
      const source = context.createMediaElementSource(audio);
      if (typeof context.createStereoPanner === "function") {
        const panner = context.createStereoPanner();
        panner.pan.value = Math.max(-1, Math.min(1, panValue));
        source.connect(panner);
        panner.connect(gainNode);
        return true;
      }
      source.connect(gainNode);
      return true;
    } catch {
      // Fallback to direct element playback if node creation fails.
      return false;
    }
  }

  function playSound(packet) {
    const name = packet.name || packet.sound || "";
    const url = toSoundUrl(name, soundBaseUrl);
    if (!url) {
      return;
    }

    const audio = createAudioElement(url);
    audio.muted = muted;
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
      const attached = connectElement(audio, effectsGain, (packet.pan ?? 0) / 100, url);
      if (!attached && effectsGain) {
        audio.volume *= effectsGain.gain.value;
      }
      safePlay(audio, {
        onRejected: () => {
          if (pendingEffectPackets.length >= MAX_PENDING_EFFECTS) {
            pendingEffectPackets.shift();
          }
          pendingEffectPackets.push({
            name,
            volume: packet.volume ?? 100,
            pan: packet.pan ?? 0,
            pitch: packet.pitch ?? 100,
          });
        },
      });
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
        safePlay(currentMusic, {
          onRejected: () => {
            pendingMusicPacket = { name, looping };
          },
        });
      }
      return;
    }

    stopMusic();

    const audio = createAudioElement(url);
    audio.muted = muted;
    audio.preload = "auto";
    audio.loop = looping;
    audio.volume = 1.0;

    try {
      const attached = connectElement(audio, musicGain, 0, url);
      if (!attached && musicGain) {
        audio.volume *= musicGain.gain.value;
      }
      currentMusic = audio;
      currentMusicName = name;
      currentMusicLooping = looping;
      pendingMusicPacket = null;
      safePlay(audio, {
        onRejected: () => {
          pendingMusicPacket = { name, looping };
        },
      });
    } catch {
      currentMusic = audio;
      currentMusicName = name;
      currentMusicLooping = looping;
      pendingMusicPacket = { name, looping };
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
    pendingMusicPacket = null;
  }

  function stopAmbience() {
    if (currentAmbience) {
      try {
        currentAmbience.pause();
        currentAmbience.currentTime = 0;
      } catch {
        // Ignore stop failures.
      }
      currentAmbience = null;
    }
    if (currentAmbienceLoop) {
      try {
        currentAmbienceLoop.pause();
        currentAmbienceLoop.currentTime = 0;
      } catch {
        // Ignore stop failures.
      }
      currentAmbienceLoop = null;
    }
    currentAmbienceLoopName = "";
    pendingAmbiencePacket = null;
  }

  function playAmbience(packet) {
    const loopName = packet.loop || "";
    const introName = packet.intro || "";
    if (!loopName) {
      return;
    }
    if (currentAmbienceLoop && currentAmbienceLoopName === loopName) {
      if (currentAmbienceLoop.paused) {
        safePlay(currentAmbienceLoop, {
          onRejected: () => {
            pendingAmbiencePacket = {
              loop: loopName,
              intro: introName,
              outro: packet.outro || "",
            };
          },
        });
      }
      return;
    }

    stopAmbience();

    const loopAudio = createAudioElement(toSoundUrl(loopName, soundBaseUrl));
    loopAudio.muted = muted;
    loopAudio.preload = "auto";
    loopAudio.loop = true;
    loopAudio.volume = 1.0;
    const loopUrl = toSoundUrl(loopName, soundBaseUrl);
    const loopAttached = connectElement(loopAudio, ambienceGain, 0, loopUrl);
    if (!loopAttached && ambienceGain) {
      loopAudio.volume *= ambienceGain.gain.value;
    }

    const startLoop = () => {
      currentAmbienceLoop = loopAudio;
      currentAmbienceLoopName = loopName;
      pendingAmbiencePacket = null;
      safePlay(loopAudio, {
        onRejected: () => {
          pendingAmbiencePacket = {
            loop: loopName,
            intro: introName,
            outro: packet.outro || "",
          };
        },
      });
    };

    if (introName) {
      const introAudio = createAudioElement(toSoundUrl(introName, soundBaseUrl));
      introAudio.muted = muted;
      introAudio.preload = "auto";
      introAudio.loop = false;
      introAudio.volume = 1.0;
      const introUrl = toSoundUrl(introName, soundBaseUrl);
      const introAttached = connectElement(introAudio, ambienceGain, 0, introUrl);
      if (!introAttached && ambienceGain) {
        introAudio.volume *= ambienceGain.gain.value;
      }
      introAudio.addEventListener("ended", startLoop, { once: true });
      currentAmbience = introAudio;
      safePlay(introAudio, {
        onRejected: () => {
          pendingAmbiencePacket = {
            loop: loopName,
            intro: introName,
            outro: packet.outro || "",
          };
          startLoop();
        },
      });
      return;
    }

    startLoop();
  }

  function retryPendingPlayback() {
    if (pendingMusicPacket) {
      const packet = pendingMusicPacket;
      pendingMusicPacket = null;
      playMusic(packet);
    }
    if (pendingAmbiencePacket) {
      const packet = pendingAmbiencePacket;
      pendingAmbiencePacket = null;
      playAmbience(packet);
    }
    if (pendingEffectPackets.length > 0) {
      const packets = pendingEffectPackets.splice(0, pendingEffectPackets.length);
      for (const packet of packets) {
        playSound(packet);
      }
    }
  }

  function setMusicVolumePercent(percent) {
    const bounded = Math.max(0, Math.min(100, Number(percent)));
    if (musicGain) {
      musicGain.gain.value = bounded / 100;
    } else if (currentMusic) {
      currentMusic.volume = bounded / 100;
    }
    return bounded;
  }

  function setAmbienceVolumePercent(percent) {
    const bounded = Math.max(0, Math.min(100, Number(percent)));
    if (ambienceGain) {
      ambienceGain.gain.value = bounded / 100;
    } else {
      if (currentAmbience) {
        currentAmbience.volume = bounded / 100;
      }
      if (currentAmbienceLoop) {
        currentAmbienceLoop.volume = bounded / 100;
      }
    }
    return bounded;
  }

  function setMuted(nextMuted) {
    muted = Boolean(nextMuted);
    if (currentMusic) {
      currentMusic.muted = muted;
    }
    if (currentAmbience) {
      currentAmbience.muted = muted;
    }
    if (currentAmbienceLoop) {
      currentAmbienceLoop.muted = muted;
    }
    for (const effect of activeEffects) {
      effect.muted = muted;
    }
  }

  function isMuted() {
    return muted;
  }

  function getMusicVolumePercent() {
    if (musicGain) {
      return Math.round(musicGain.gain.value * 100);
    }
    if (currentMusic) {
      return Math.round(currentMusic.volume * 100);
    }
    return 20;
  }

  function getAmbienceVolumePercent() {
    if (ambienceGain) {
      return Math.round(ambienceGain.gain.value * 100);
    }
    if (currentAmbienceLoop) {
      return Math.round(currentAmbienceLoop.volume * 100);
    }
    return 100;
  }

  function stopAll() {
    stopMusic();
    stopAmbience();
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
    playAmbience,
    stopMusic,
    stopAmbience,
    stopAll,
    setMusicVolumePercent,
    setAmbienceVolumePercent,
    getMusicVolumePercent,
    getAmbienceVolumePercent,
    setMuted,
    isMuted,
    retryPendingPlayback,
  };
}
