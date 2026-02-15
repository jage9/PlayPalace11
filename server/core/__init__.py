"""Core server infrastructure."""

from importlib import import_module

from .state import ServerLifecycleState, ServerMode
from .tick import TickScheduler, load_server_config, DEFAULT_TICK_INTERVAL_MS

__all__ = [
    "Server",
    "ServerLifecycleState",
    "ServerMode",
    "TickScheduler",
    "load_server_config",
    "DEFAULT_TICK_INTERVAL_MS",
]


def __getattr__(name: str):
    if name == "Server":
        server_module = import_module(".server", __name__)
        Server = server_module.Server  # type: ignore[attr-defined]
        globals()["Server"] = Server
        return Server
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
