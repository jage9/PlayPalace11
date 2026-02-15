"""User preferences for PlayPalace."""

from dataclasses import dataclass, field
from enum import Enum


class DiceKeepingStyle(Enum):
    """Dice keeping style preference."""

    PLAYPALACE = "playpalace"  # Dice indexes (1-5 keys)
    QUENTIN_C = "quentin_c"  # Dice values (1-6 keys)

    @classmethod
    def from_str(cls, value: str) -> "DiceKeepingStyle":
        """Convert string to enum, defaulting to PLAYPALACE."""
        try:
            return cls(value)
        except ValueError:
            return cls.PLAYPALACE


@dataclass
class UserPreferences:
    """User preferences that persist across sessions."""

    # Sound preferences
    play_turn_sound: bool = True  # Play sound when it's your turn

    # Dice game preferences
    clear_kept_on_roll: bool = False  # Clear kept dice after rolling
    dice_keeping_style: DiceKeepingStyle = field(
        default_factory=lambda: DiceKeepingStyle.PLAYPALACE
    )

    def to_dict(self) -> dict:
        """Convert to dictionary for storage."""
        return {
            "play_turn_sound": self.play_turn_sound,
            "clear_kept_on_roll": self.clear_kept_on_roll,
            "dice_keeping_style": self.dice_keeping_style.value,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "UserPreferences":
        """Create from dictionary."""
        return cls(
            play_turn_sound=data.get("play_turn_sound", True),
            clear_kept_on_roll=data.get("clear_kept_on_roll", False),
            dice_keeping_style=DiceKeepingStyle.from_str(
                data.get("dice_keeping_style", "playpalace")
            ),
        )
