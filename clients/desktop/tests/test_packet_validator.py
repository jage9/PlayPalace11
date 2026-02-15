from __future__ import annotations

import sys
import types

import pytest
from jsonschema import ValidationError as SchemaValidationError

# Provide a lightweight wx stub so NetworkManager can import without wxPython installed.
if "wx" not in sys.modules:
    wx_stub = types.SimpleNamespace(CallAfter=lambda func, *args, **kwargs: func(*args, **kwargs))
    sys.modules["wx"] = wx_stub

import network_manager as nm_mod
from packet_validator import PacketValidator, ValidationError, validate_incoming, validate_outgoing


def test_packet_validator_accepts_valid_packets() -> None:
    validator = PacketValidator()
    assert validator.available
    validator.validate_outgoing({"type": "ping"})
    validator.validate_incoming({"type": "pong"})


def test_packet_validator_rejects_missing_fields() -> None:
    validator = PacketValidator()
    assert validator.available
    with pytest.raises(ValidationError):
        validator.validate_outgoing({"type": "authorize"})
    with pytest.raises(ValidationError):
        validator.validate_incoming({"type": "authorize_success"})


class DummyWindow:
    def __init__(self) -> None:
        self.history: list[str] = []

    def add_history(self, message: str, *_args: object) -> None:
        self.history.append(message)


def _make_validation_error(message: str) -> SchemaValidationError:
    return SchemaValidationError(message)


def test_network_manager_validation_hooks(monkeypatch) -> None:
    nm = nm_mod.NetworkManager(main_window=DummyWindow())
    monkeypatch.setattr(nm_mod.wx, "CallAfter", lambda func, *args, **kwargs: func(*args, **kwargs))

    # Force outgoing validation failure
    monkeypatch.setattr(
        nm_mod,
        "validate_outgoing",
        lambda packet: (_ for _ in ()).throw(_make_validation_error("bad outgoing")),
    )
    assert nm._validate_outgoing_packet({"type": "ping"}) is False
    assert nm.main_window.history

    # Allow outgoing packets again
    monkeypatch.setattr(nm_mod, "validate_outgoing", validate_outgoing)
    assert nm._validate_outgoing_packet({"type": "ping"}) is True

    # Now test incoming validation failure
    monkeypatch.setattr(
        nm_mod,
        "validate_incoming",
        lambda packet: (_ for _ in ()).throw(_make_validation_error("bad incoming")),
    )
    assert nm._validate_incoming_packet({"type": "pong"}) is False
    assert len(nm.main_window.history) >= 2

    monkeypatch.setattr(nm_mod, "validate_incoming", validate_incoming)
    assert nm._validate_incoming_packet({"type": "pong"}) is True
