"""Compatibility shim for RoundTimer (moved to turn_system)."""

from .turn_system import RoundTransitionTimer, RoundTimer

__all__ = ["RoundTransitionTimer", "RoundTimer"]
