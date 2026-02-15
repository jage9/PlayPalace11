"""Packet validation helpers backed by the generated JSON schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError

_SCHEMA_PATH = Path(__file__).with_name("packet_schema.json")


class PacketValidator:
    """Wraps jsonschema validators for both directions."""

    def __init__(self) -> None:
        self._available = False
        self._client_validator: Draft202012Validator | None = None
        self._server_validator: Draft202012Validator | None = None
        self._load()

    @property
    def available(self) -> bool:
        return self._available

    def _load(self) -> None:
        try:
            payload = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
        except FileNotFoundError:
            self._available = False
            return

        client_schema = payload.get("client_to_server")
        server_schema = payload.get("server_to_client")
        if not client_schema or not server_schema:
            self._available = False
            return

        self._client_validator = Draft202012Validator(client_schema)
        self._server_validator = Draft202012Validator(server_schema)
        self._available = True

    def validate_outgoing(self, packet: dict[str, Any]) -> None:
        if not self._available or not self._client_validator:
            return
        self._client_validator.validate(packet)
        if packet.get("type") == "authorize":
            if not (packet.get("password") or packet.get("session_token")):
                raise ValidationError("authorize requires password or session_token")

    def validate_incoming(self, packet: dict[str, Any]) -> None:
        if not self._available or not self._server_validator:
            return
        self._server_validator.validate(packet)


VALIDATOR = PacketValidator()


def validate_outgoing(packet: dict[str, Any]) -> None:
    """Validate a client->server packet."""
    VALIDATOR.validate_outgoing(packet)


def validate_incoming(packet: dict[str, Any]) -> None:
    """Validate a server->client packet."""
    VALIDATOR.validate_incoming(packet)


__all__ = ["validate_outgoing", "validate_incoming", "ValidationError"]
