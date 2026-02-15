import pytest

import sound_manager as sm_mod
from sound_manager import SoundManager


class DummySound:
    def __init__(self):
        self.stop_called = False
        self.volume = 1.0
        self.looping = False
        self.pan = 0.0
        self.played = False

    def stop(self):
        self.stop_called = True

    def play(self):
        self.played = True


class FakeSoundCacher:
    def __init__(self):
        self.calls = []
        self.refs = []
        self.cache = {}

    def play(self, path, pan=0.0, volume=1.0, pitch=1.0):
        sound = DummySound()
        sound.pan = pan
        sound.volume = volume
        sound.pitch = pitch
        self.calls.append((path, pan, volume, pitch))
        return sound


def make_manager(tmp_path):
    manager = SoundManager()
    manager.sound_cacher = FakeSoundCacher()
    manager.sounds_folder = str(tmp_path)
    return manager


def test_play_passes_full_path(tmp_path):
    (tmp_path / "click.ogg").write_bytes(b"123")
    manager = make_manager(tmp_path)
    stream = manager.play("click.ogg", volume=0.4, pan=0.1, pitch=1.1)

    assert isinstance(stream, DummySound)
    path, pan, volume, pitch = manager.sound_cacher.calls[0]
    assert path.endswith("click.ogg")
    assert pan == 0.1
    assert volume == 0.4
    assert pitch == 1.1


def test_music_stops_previous_track(tmp_path):
    (tmp_path / "intro.ogg").write_bytes(b"1")
    (tmp_path / "loop.ogg").write_bytes(b"2")
    manager = make_manager(tmp_path)

    manager.music("intro.ogg")
    first_stream = manager.current_music
    manager.music("loop.ogg")

    assert first_stream.stop_called is True
    assert manager.current_music_name == "loop.ogg"


def test_stop_music_without_fade(tmp_path):
    manager = make_manager(tmp_path)
    manager.current_music = DummySound()
    manager.current_music_name = "playing.ogg"

    manager.stop_music(fade=False)
    assert manager.current_music is None
    assert manager.current_music_name is None
    assert manager.sound_cacher.calls == []


def test_set_music_volume_updates_current_stream(tmp_path):
    manager = make_manager(tmp_path)
    manager.current_music = DummySound()
    manager.set_music_volume(0.75)
    assert pytest.approx(manager.current_music.volume, rel=0.0) == 0.75


def test_menu_sounds_use_configured_names(tmp_path):
    manager = make_manager(tmp_path)
    manager.set_menuclick_sound("click.ogg")
    manager.set_menuenter_sound("enter.ogg")
    manager.play_menuclick()
    manager.play_menuenter()
    played = [call[0].rsplit("\\", 1)[-1].rsplit("/", 1)[-1] for call in manager.sound_cacher.calls]
    assert played == ["click.ogg", "enter.ogg"]


def test_add_and_remove_playlist(monkeypatch, tmp_path):
    created = {}

    class DummyPlaylist:
        def __init__(self, tracks, audio_type, sound_manager, shuffle, repeats, auto_start, auto_remove):
            self.tracks = list(tracks)
            self.audio_type = audio_type
            self.sound_manager = sound_manager
            self.stop_called = False
            created["playlist"] = self

        def stop(self):
            self.stop_called = True

    monkeypatch.setattr(sm_mod, "AudioPlaylist", DummyPlaylist)
    manager = make_manager(tmp_path)
    manager.add_playlist("bgm", ["track.ogg"], audio_type="music", auto_start=False)

    assert "bgm" in manager.playlists
    playlist = manager.playlists["bgm"]
    assert playlist.tracks == ["track.ogg"]

    manager.remove_playlist("bgm")
    assert playlist.stop_called is True
    assert "bgm" not in manager.playlists


def test_play_returns_none_when_sound_cacher_fails(tmp_path):
    manager = make_manager(tmp_path)

    def boom(*_args, **_kwargs):
        raise FileNotFoundError

    manager.sound_cacher.play = boom  # type: ignore[assignment]
    assert manager.play("missing.ogg") is None


def test_music_handles_exception_and_resets_state(tmp_path):
    manager = make_manager(tmp_path)
    old_music = DummySound()
    manager.current_music = old_music
    manager.current_music_name = "old.ogg"

    def boom(*_args, **_kwargs):
        raise IOError("bad audio")

    manager.sound_cacher.play = boom  # type: ignore[assignment]
    manager.music("new.ogg")

    assert old_music.stop_called is True
    assert manager.current_music is None
    assert manager.current_music_name is None


def test_music_skips_restart_when_same_track(tmp_path):
    manager = make_manager(tmp_path)
    existing = DummySound()
    manager.current_music = existing
    manager.current_music_name = "loop.ogg"

    called = []

    def fake_play(*_args, **_kwargs):
        called.append(1)
        return DummySound()

    manager.sound_cacher.play = fake_play  # type: ignore[assignment]
    manager.music("loop.ogg")

    assert called == []
    assert manager.current_music is existing
