import types

import pytest

import sound_cacher
from sound_cacher import SoundCacher


class DummyStream:
    def __init__(self, mem, file, length):
        self._frequency = 44100
        self.pan = 0.0
        self.volume = 1.0
        self.played = False
        self.mem = mem
        self.length = length

    def play(self):
        self.played = True

    def get_frequency(self):
        return self._frequency

    def set_frequency(self, value):
        self._frequency = value


def test_sound_cacher_returns_stream(monkeypatch, tmp_path):
    monkeypatch.setattr(sound_cacher, "o", object())

    dummy_stream = DummyStream
    fake_stream_module = types.SimpleNamespace(FileStream=dummy_stream)
    monkeypatch.setattr(sound_cacher, "stream", fake_stream_module)

    cache = SoundCacher()
    audio_file = tmp_path / "beep.ogg"
    audio_file.write_bytes(b"wave-data")

    stream = cache.play(str(audio_file), pan=0.4, volume=0.6, pitch=1.2)

    assert isinstance(stream, DummyStream)
    assert stream.played is True
    assert pytest.approx(stream.pan) == 0.4
    assert pytest.approx(stream.volume) == 0.6
    assert pytest.approx(stream.get_frequency()) == int(44100 * 1.2)
    # Second call should reuse cached bytes
    cache.play(str(audio_file))
    assert str(audio_file) in cache.cache


def test_sound_cacher_returns_none_when_no_output(monkeypatch, tmp_path):
    monkeypatch.setattr(sound_cacher, "o", None)
    cache = SoundCacher()
    assert cache.play(str(tmp_path / "missing.ogg")) is None
