"""Pydantic schemas for identities.json validation.

Provides a single source of truth for the structure of servers, accounts, option profiles,
and the top-level identities object. Used for validation on load and for
constructing new objects with all required fields.
"""

import uuid
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, field_validator


class AudioOptions(BaseModel):
    model_config = ConfigDict(extra="ignore")

    music_volume: int = 20
    ambience_volume: int = 20


class SocialOptions(BaseModel):
    model_config = ConfigDict(extra="ignore")


class InterfaceOptions(BaseModel):
    model_config = ConfigDict(extra="ignore")

    invert_multiline_enter_behavior: bool = False
    play_typing_sounds: bool = True


class LocalTableOptions(BaseModel):
    model_config = ConfigDict(extra="ignore")


class OptionsProfile(BaseModel):
    model_config = ConfigDict(extra="ignore")

    local_table: LocalTableOptions = LocalTableOptions()
    social: SocialOptions = SocialOptions()
    audio: AudioOptions = AudioOptions()
    interface: InterfaceOptions = InterfaceOptions()


class UserAccount(BaseModel):
    model_config = ConfigDict(extra="ignore")

    account_id: str = ""
    username: str = ""
    password: str = ""
    refresh_token: str = ""
    refresh_expires_at: int | None = None
    email: str = ""
    notes: str = ""

    def model_post_init(self, __context: Any) -> None:
        if not self.account_id:
            self.account_id = str(uuid.uuid4())


class Server(BaseModel):
    model_config = ConfigDict(extra="ignore")

    server_id: str = ""
    name: str = ""
    host: str = ""
    port: int = 8000
    notes: str = ""
    accounts: Dict[str, UserAccount] = {}
    last_account_id: Optional[str] = None
    options_profile: OptionsProfile = OptionsProfile()
    trusted_certificate: Optional[Dict[str, Any]] = None

    def model_post_init(self, __context: Any) -> None:
        if not self.server_id:
            self.server_id = str(uuid.uuid4())

    @field_validator("port", mode="before")
    @classmethod
    def coerce_port(cls, v: Any) -> int:
        if isinstance(v, str):
            return int(v)
        return v


class Identities(BaseModel):
    model_config = ConfigDict(extra="ignore")

    last_server_id: Optional[str] = None
    default_options_profile: OptionsProfile = OptionsProfile()
    servers: Dict[str, Server] = {}


class ExportedIdentities(BaseModel):
    """Schema for the exported/imported identities JSON file."""
    model_config = ConfigDict(extra="ignore")

    description: str
    timestamp: int
    servers: List[Server]

    @field_validator("description", mode="before")
    @classmethod
    def description_not_empty(cls, v: Any) -> str:
        if not isinstance(v, str) or not v.strip():
            raise ValueError("description cannot be empty")
        return v

    @field_validator("servers", mode="before")
    @classmethod
    def servers_not_empty(cls, v: Any) -> list:
        if not v:
            raise ValueError("servers cannot be empty")
        return v


def validate_identities(raw_data: dict) -> dict:
    """Parse raw data through the Identities schema and return a plain dict.

    On validation failure, returns default identities.
    """
    try:
        model = Identities.model_validate(raw_data)
        return model.model_dump()
    except Exception:
        return Identities().model_dump()
