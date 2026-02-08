"""Hangin' with Friends implementation."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import math
import random
import string

from ..base import Game, GameOptions, Player
from ..registry import register_game
from ...game_utils.action_guard_mixin import ActionGuardMixin
from ...game_utils.actions import Action, ActionSet, EditboxInput, MenuInput, Visibility
from ...game_utils.bot_helper import BotHelper
from ...game_utils.game_result import GameResult, PlayerResult
from ...game_utils.options import BoolOption, IntOption, MenuOption, option_field
from ...messages.localization import Localization
from ...ui.keybinds import KeybindState

LETTER_SCORES = {
    "E": 1,
    "A": 1,
    "I": 1,
    "O": 1,
    "N": 1,
    "R": 1,
    "T": 1,
    "L": 1,
    "S": 1,
    "U": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10,
}

DEFAULT_WORDS = [
    "apple",
    "apron",
    "badge",
    "baker",
    "beach",
    "blaze",
    "board",
    "bonus",
    "brave",
    "brick",
    "bring",
    "cable",
    "candy",
    "chair",
    "chase",
    "clear",
    "cloud",
    "coast",
    "crate",
    "dance",
    "dream",
    "eager",
    "earth",
    "fable",
    "flame",
    "float",
    "focus",
    "frame",
    "friend",
    "frost",
    "globe",
    "grace",
    "grape",
    "green",
    "happy",
    "house",
    "jolly",
    "laugh",
    "light",
    "lucky",
    "magic",
    "maple",
    "melon",
    "metal",
    "music",
    "north",
    "ocean",
    "party",
    "pearl",
    "piano",
    "pilot",
    "planet",
    "plaza",
    "point",
    "power",
    "pride",
    "prize",
    "queen",
    "quick",
    "radio",
    "raven",
    "river",
    "robot",
    "royal",
    "score",
    "shape",
    "shine",
    "shore",
    "smile",
    "spark",
    "spice",
    "spoon",
    "sport",
    "sprout",
    "stack",
    "stone",
    "story",
    "storm",
    "sugar",
    "sunny",
    "swing",
    "table",
    "tiger",
    "toast",
    "track",
    "travel",
    "vivid",
    "voice",
    "water",
    "whale",
    "wheat",
    "zebra",
]

# Weighted rack pool (roughly English frequency).
LETTER_POOL = (
    "EEEEEEEEEEEE"
    "AAAAAAAAA"
    "IIIIIIIII"
    "OOOOOOOO"
    "NNNNNN"
    "RRRRRR"
    "TTTTTT"
    "LLLL"
    "SSSS"
    "UUUU"
    "DDDD"
    "GGG"
    "BBCCMMPP"
    "FFHHVVWWYY"
    "K"
    "JX"
    "QZ"
)

BOT_DIFFICULTY_CHOICES = ["easy", "medium", "hard", "extreme"]
BOT_DIFFICULTY_LABELS = {
    "easy": "hwf-bot-difficulty-easy",
    "medium": "hwf-bot-difficulty-medium",
    "hard": "hwf-bot-difficulty-hard",
    "extreme": "hwf-bot-difficulty-extreme",
}
DICTIONARY_MODE_CHOICES = ["strict", "rack-only", "off"]
DICTIONARY_MODE_LABELS = {
    "strict": "hwf-dictionary-mode-strict",
    "rack-only": "hwf-dictionary-mode-rack-only",
    "off": "hwf-dictionary-mode-off",
}
BOT_GUESS_AGGRESSION_CHOICES = ["safe", "balanced", "risky"]
BOT_GUESS_AGGRESSION_LABELS = {
    "safe": "hwf-bot-guess-safe",
    "balanced": "hwf-bot-guess-balanced",
    "risky": "hwf-bot-guess-risky",
}

SOUNDS = {
    "lava": "game_hangin_with_friends/bg_lava5.ogg",
    "click": "game_hangin_with_friends/click.ogg",
    "music": "game_hangin_with_friends/music_lavascene1.ogg",
    "avatar": "game_hangin_with_friends/sfx_avatarpicker3.ogg",
    "balloon": "game_hangin_with_friends/sfx_balloonflyoff3_250ms.ogg",
    "shuffle": "game_hangin_with_friends/sfx_bloopshuffle5.ogg",
    "buy_points": "game_hangin_with_friends/sfx_buypoints1.ogg",
    "click2": "game_hangin_with_friends/sfx_click2.ogg",
    "drop": "game_hangin_with_friends/sfx_dropbloop.ogg",
    "enter_wheel": "game_hangin_with_friends/sfx_entermissions.ogg",
    "lose": "game_hangin_with_friends/sfx_gamelost1.ogg",
    "win": "game_hangin_with_friends/sfx_gamewon1.ogg",
    "history_correct": "game_hangin_with_friends/sfx_historycorrect1.ogg",
    "history_incorrect": "game_hangin_with_friends/sfx_historyincorrect1.ogg",
    "level_up": "game_hangin_with_friends/sfx_levelup1.ogg",
    "level_up_missions": "game_hangin_with_friends/sfx_levelupmissions.ogg",
    "lifeline_bounce": "game_hangin_with_friends/sfx_lifeline_bounce.ogg",
    "lifeline_slide": "game_hangin_with_friends/sfx_lifeline_slide.ogg",
    "menu_close": "game_hangin_with_friends/sfx_menuclose3.ogg",
    "menu_open": "game_hangin_with_friends/sfx_menuopen3.ogg",
    "popup": "game_hangin_with_friends/sfx_missioncompletepopup.ogg",
    "multiplier": "game_hangin_with_friends/sfx_multiplybadge4_1s.ogg",
    "pickup": "game_hangin_with_friends/sfx_pickupbloop1.ogg",
    "roulette": "game_hangin_with_friends/sfx_roulette4.ogg",
    "roulette_ping": "game_hangin_with_friends/sfx_roulette4_ping.ogg",
    "score_flyup": "game_hangin_with_friends/sfx_scoreflyup5_pointscharge.ogg",
    "submit_invalid": "game_hangin_with_friends/sfx_submitwordinvalid6.ogg",
    "submit_valid": "game_hangin_with_friends/sfx_submitwordvalid4_3.ogg",
    "use_lifeline": "game_hangin_with_friends/sfx_uselifeline1.ogg",
}

CORRECT_SEQUENCE_SOUNDS = [
    "game_hangin_with_friends/sfx_correctsequence1_1.ogg",
    "game_hangin_with_friends/sfx_correctsequence1_2.ogg",
    "game_hangin_with_friends/sfx_correctsequence1_3.ogg",
    "game_hangin_with_friends/sfx_correctsequence1_4.ogg",
    "game_hangin_with_friends/sfx_correctsequence1_5.ogg",
    "game_hangin_with_friends/sfx_correctsequence1_6.ogg",
    "game_hangin_with_friends/sfx_correctsequence1_7.ogg",
    "game_hangin_with_friends/sfx_correctsequence1_8.ogg",
]

INCORRECT_SEQUENCE_SOUNDS = [
    "game_hangin_with_friends/sfx_incorrectsequence1_1.ogg",
    "game_hangin_with_friends/sfx_incorrectsequence1_2.ogg",
    "game_hangin_with_friends/sfx_incorrectsequence1_3.ogg",
    "game_hangin_with_friends/sfx_incorrectsequence1_4.ogg",
    "game_hangin_with_friends/sfx_incorrectsequence1_5.ogg",
    "game_hangin_with_friends/sfx_incorrectsequence1_6.ogg",
    "game_hangin_with_friends/sfx_incorrectsequence1_7.ogg",
    "game_hangin_with_friends/sfx_incorrectsequence1_8noballoon.ogg",
]

WHEEL_OUTCOMES = [
    "coin_bonus",
    "extra_guess",
    "fewer_guess",
    "double_points",
    "lifeline_reveal",
    "lifeline_remove",
    "lifeline_retry",
    "nothing",
]


@dataclass
class HanginWithFriendsPlayer(Player):
    """Player state for Hangin' with Friends."""

    balloons_remaining: int = 5
    score: int = 0
    coins: int = 0
    level: int = 1
    correct_streak: int = 0
    wrong_streak: int = 0
    lifeline_reveal: int = 0
    lifeline_remove: int = 0
    lifeline_retry: int = 0
    retry_shield_active: bool = False


@dataclass
class HanginWithFriendsOptions(GameOptions):
    """Config options for Hangin' with Friends."""

    starting_balloons: int = option_field(
        IntOption(
            default=5,
            min_val=1,
            max_val=10,
            value_key="count",
            label="hwf-set-starting-balloons",
            prompt="hwf-enter-starting-balloons",
            change_msg="hwf-option-changed-starting-balloons",
        )
    )
    rack_size: int = option_field(
        IntOption(
            default=12,
            min_val=8,
            max_val=20,
            value_key="count",
            label="hwf-set-rack-size",
            prompt="hwf-enter-rack-size",
            change_msg="hwf-option-changed-rack-size",
        )
    )
    min_word_length: int = option_field(
        IntOption(
            default=3,
            min_val=2,
            max_val=8,
            value_key="count",
            label="hwf-set-min-word-length",
            prompt="hwf-enter-min-word-length",
            change_msg="hwf-option-changed-min-word-length",
        )
    )
    max_word_length: int = option_field(
        IntOption(
            default=8,
            min_val=3,
            max_val=12,
            value_key="count",
            label="hwf-set-max-word-length",
            prompt="hwf-enter-max-word-length",
            change_msg="hwf-option-changed-max-word-length",
        )
    )
    base_wrong_guesses: int = option_field(
        IntOption(
            default=2,
            min_val=0,
            max_val=10,
            value_key="count",
            label="hwf-set-base-wrong-guesses",
            prompt="hwf-enter-base-wrong-guesses",
            change_msg="hwf-option-changed-base-wrong-guesses",
        )
    )
    max_rounds: int = option_field(
        IntOption(
            default=0,
            min_val=0,
            max_val=500,
            value_key="count",
            label="hwf-set-max-rounds",
            prompt="hwf-enter-max-rounds",
            change_msg="hwf-option-changed-max-rounds",
        )
    )
    max_score: int = option_field(
        IntOption(
            default=0,
            min_val=0,
            max_val=500,
            value_key="score",
            label="hwf-set-max-score",
            prompt="hwf-enter-max-score",
            change_msg="hwf-option-changed-max-score",
        )
    )
    default_bot_difficulty: str = option_field(
        MenuOption(
            default="medium",
            choices=BOT_DIFFICULTY_CHOICES,
            value_key="mode",
            label="hwf-set-default-bot-difficulty",
            prompt="hwf-select-default-bot-difficulty",
            change_msg="hwf-option-changed-default-bot-difficulty",
            choice_labels=BOT_DIFFICULTY_LABELS,
        )
    )
    dictionary_mode: str = option_field(
        MenuOption(
            default="rack-only",
            choices=DICTIONARY_MODE_CHOICES,
            value_key="mode",
            label="hwf-set-dictionary-mode",
            prompt="hwf-select-dictionary-mode",
            change_msg="hwf-option-changed-dictionary-mode",
            choice_labels=DICTIONARY_MODE_LABELS,
        )
    )
    allow_full_word_guess: bool = option_field(
        BoolOption(
            default=True,
            value_key="enabled",
            label="hwf-toggle-full-word-guess",
            change_msg="hwf-option-changed-full-word-guess",
        )
    )
    spectators_see_all_actions: bool = option_field(
        BoolOption(
            default=True,
            value_key="enabled",
            label="hwf-toggle-spectators-see-all-actions",
            change_msg="hwf-option-changed-spectators-see-all-actions",
        )
    )
    bot_guess_aggression: str = option_field(
        MenuOption(
            default="balanced",
            choices=BOT_GUESS_AGGRESSION_CHOICES,
            value_key="mode",
            label="hwf-set-bot-guess-aggression",
            prompt="hwf-select-bot-guess-aggression",
            change_msg="hwf-option-changed-bot-guess-aggression",
            choice_labels=BOT_GUESS_AGGRESSION_LABELS,
        )
    )


@dataclass
@register_game
class HanginWithFriendsGame(ActionGuardMixin, Game):
    """Turn-based Hangman variant where players alternate setter/guesser roles."""

    players: list[HanginWithFriendsPlayer] = field(default_factory=list)
    options: HanginWithFriendsOptions = field(default_factory=HanginWithFriendsOptions)

    phase: str = "lobby"  # lobby, choose_word, guessing, round_end, game_end
    setter_id: str = ""
    guesser_id: str = ""
    tile_rack: list[str] = field(default_factory=list)
    secret_word: str = ""
    masked_word: str = ""
    guessed_letters: list[str] = field(default_factory=list)
    wrong_guesses: int = 0
    max_wrong_guesses: int = 0
    rng_seed: int = 0
    bot_difficulties: dict[str, str] = field(default_factory=dict)
    wheel_result: str = ""
    round_points_multiplier: int = 1
    lava_next_tick: int = 0

    def __post_init__(self):
        super().__post_init__()
        self._dictionary_words: tuple[str, ...] = tuple(DEFAULT_WORDS)
        self._dictionary_loaded: bool = False

    def rebuild_runtime_state(self) -> None:
        """Rebuild runtime-only state after load."""
        self._dictionary_words = tuple(DEFAULT_WORDS)
        self._dictionary_loaded = False

    @classmethod
    def get_name(cls) -> str:
        return "Hangin' with Friends"

    @classmethod
    def get_type(cls) -> str:
        return "hangin_with_friends"

    @classmethod
    def get_category(cls) -> str:
        return "category-word-games"

    @classmethod
    def get_min_players(cls) -> int:
        return 2

    @classmethod
    def get_max_players(cls) -> int:
        return 2

    def create_player(
        self, player_id: str, name: str, is_bot: bool = False
    ) -> HanginWithFriendsPlayer:
        return HanginWithFriendsPlayer(id=player_id, name=name, is_bot=is_bot)

    def create_turn_action_set(self, player: HanginWithFriendsPlayer) -> ActionSet:
        action_set = ActionSet(name="turn")

        action_set.add(
            Action(
                id="choose_word",
                label="Choose word",
                handler="_action_choose_word",
                is_enabled="_is_choose_word_enabled",
                is_hidden="_is_choose_word_hidden",
                input_request=EditboxInput(
                    prompt="hwf-prompt-enter-word",
                    bot_input="_bot_choose_word_input",
                ),
            )
        )

        for letter in string.ascii_lowercase:
            action_set.add(
                Action(
                    id=f"guess_letter_{letter}",
                    label=f"Guess {letter.upper()}",
                    handler="_action_guess_letter",
                    is_enabled="_is_guess_letter_enabled",
                    is_hidden="_is_guess_letter_hidden",
                    get_label="_get_guess_letter_label",
                )
            )

        action_set.add(
            Action(
                id="guess_word",
                label="Guess full word",
                handler="_action_guess_word",
                is_enabled="_is_guess_word_enabled",
                is_hidden="_is_guess_word_hidden",
                input_request=EditboxInput(
                    prompt="hwf-prompt-guess-word",
                    bot_input="_bot_guess_word_input",
                ),
            )
        )

        action_set.add(
            Action(
                id="lifeline_reveal",
                label="Use reveal lifeline",
                handler="_action_lifeline_reveal",
                is_enabled="_is_lifeline_reveal_enabled",
                is_hidden="_is_lifeline_reveal_hidden",
            )
        )
        action_set.add(
            Action(
                id="lifeline_remove",
                label="Use remove-strike lifeline",
                handler="_action_lifeline_remove",
                is_enabled="_is_lifeline_remove_enabled",
                is_hidden="_is_lifeline_remove_hidden",
            )
        )
        action_set.add(
            Action(
                id="lifeline_retry",
                label="Use retry-shield lifeline",
                handler="_action_lifeline_retry",
                is_enabled="_is_lifeline_retry_enabled",
                is_hidden="_is_lifeline_retry_hidden",
            )
        )
        return action_set

    def create_lobby_action_set(self, player: Player) -> ActionSet:
        """Add bot-difficulty management action to lobby."""
        action_set = super().create_lobby_action_set(player)
        user = self.get_user(player)
        locale = user.locale if user else "en"
        action_set.add(
            Action(
                id="set_bot_difficulty",
                label=Localization.get(locale, "hwf-set-bot-difficulty"),
                handler="_action_set_bot_difficulty",
                is_enabled="_is_set_bot_difficulty_enabled",
                is_hidden="_is_set_bot_difficulty_hidden",
                input_request=MenuInput(
                    prompt="hwf-select-bot-difficulty",
                    options="_per_bot_difficulty_options",
                ),
            )
        )
        return action_set

    def setup_keybinds(self) -> None:
        super().setup_keybinds()
        self.define_keybind("w", "Guess full word", ["guess_word"], state=KeybindState.ACTIVE)
        self.define_keybind("c", "Choose word", ["choose_word"], state=KeybindState.ACTIVE)
        self.define_keybind("1", "Reveal lifeline", ["lifeline_reveal"], state=KeybindState.ACTIVE)
        self.define_keybind("2", "Remove strike lifeline", ["lifeline_remove"], state=KeybindState.ACTIVE)
        self.define_keybind("3", "Retry shield lifeline", ["lifeline_retry"], state=KeybindState.ACTIVE)

    def on_start(self) -> None:
        self.status = "playing"
        self.game_active = True
        self.round = 0
        self.phase = "lobby"

        active_players = self.get_active_players()
        self._team_manager.team_mode = "individual"
        self._team_manager.setup_teams([p.name for p in active_players])

        self.set_turn_players(active_players)
        for player in active_players:
            player.balloons_remaining = self.options.starting_balloons
            player.score = 0
            player.coins = 0
            player.level = 1
            player.correct_streak = 0
            player.wrong_streak = 0
            player.lifeline_reveal = 0
            player.lifeline_remove = 0
            player.lifeline_retry = 0
            player.retry_shield_active = False

        if self.rng_seed == 0:
            self.rng_seed = random.randint(1, 2_147_483_647)
        self._load_dictionary()
        self._sync_bot_difficulty_overrides()

        self.play_music(SOUNDS["music"])
        self._schedule_next_lava_ambience(initial=True)
        self._start_round()

    def on_tick(self) -> None:
        super().on_tick()
        self.process_scheduled_sounds()
        self._maybe_play_lava_ambience()
        BotHelper.on_tick(self)

    def prestart_validate(self) -> list[str]:
        errors = super().prestart_validate()
        if self.options.min_word_length > self.options.max_word_length:
            errors.append("hwf-error-min-length-greater-than-max")
        if self.options.rack_size < self.options.max_word_length:
            errors.append("hwf-error-rack-smaller-than-max-length")
        return errors

    def _schedule_next_lava_ambience(self, initial: bool = False) -> None:
        jitter = random.randint(80, 180) if initial else random.randint(140, 320)
        self.lava_next_tick = self.sound_scheduler_tick + jitter

    def _maybe_play_lava_ambience(self) -> None:
        if self.sound_scheduler_tick < self.lava_next_tick:
            return
        self.play_sound(SOUNDS["lava"], volume=55)
        self._schedule_next_lava_ambience()

    def _start_round(self) -> None:
        if self._check_match_end():
            return

        self.round += 1
        players = self.turn_players
        if len(players) < 2:
            return

        setter = players[(self.round - 1) % len(players)]
        guesser = players[(self.round) % len(players)]

        self.setter_id = setter.id
        self.guesser_id = guesser.id
        self.tile_rack = self._generate_rack(self.round)
        self.secret_word = ""
        self.masked_word = ""
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.max_wrong_guesses = 0
        self.wheel_result = ""
        self.round_points_multiplier = 1
        setter.retry_shield_active = False
        guesser.retry_shield_active = False

        self.phase = "choose_word"
        self.current_player = setter

        self.play_sound(SOUNDS["menu_open"])
        self.play_sound(SOUNDS["avatar"], volume=70)
        self.play_sound(SOUNDS["shuffle"], volume=85)
        self.broadcast(
            f"Round {self.round}. {setter.name} is choosing a word, {guesser.name} will guess."
        )
        setter_user = self.get_user(setter)
        if setter_user:
            setter_user.speak(f"Your rack is: {' '.join(l.upper() for l in self.tile_rack)}", "table")
        self._broadcast_private_to_spectators(
            f"Setter rack ({setter.name}): {' '.join(l.upper() for l in self.tile_rack)}"
        )
        self._broadcast_spectator_player_boards()

        if setter.is_bot:
            BotHelper.jolt_bot(setter, ticks=random.randint(6, 12))

        self.rebuild_all_menus()

    # action guards
    def _is_choose_word_enabled(self, player: Player) -> str | None:
        error = self.guard_turn_action_enabled(player)
        if error:
            return error
        if self.phase != "choose_word" or player.id != self.setter_id:
            return "action-not-available"
        return None

    def _is_choose_word_hidden(self, player: Player) -> Visibility:
        return self.turn_action_visibility(player, extra_condition=self.phase == "choose_word" and player.id == self.setter_id)

    def _is_guess_letter_enabled(self, player: Player, action_id: str) -> str | None:
        error = self.guard_turn_action_enabled(player)
        if error:
            return error
        if self.phase != "guessing" or player.id != self.guesser_id:
            return "action-not-available"
        letter = action_id.rsplit("_", 1)[-1]
        if letter in self.guessed_letters:
            return "action-not-available"
        return None

    def _is_guess_letter_hidden(self, player: Player, action_id: str) -> Visibility:
        letter = action_id.rsplit("_", 1)[-1]
        return self.turn_action_visibility(
            player,
            extra_condition=(self.phase == "guessing" and player.id == self.guesser_id and letter not in self.guessed_letters),
        )

    def _is_guess_word_enabled(self, player: Player) -> str | None:
        error = self.guard_turn_action_enabled(player)
        if error:
            return error
        if not self.options.allow_full_word_guess:
            return "action-not-available"
        if self.phase != "guessing" or player.id != self.guesser_id:
            return "action-not-available"
        return None

    def _is_guess_word_hidden(self, player: Player) -> Visibility:
        return self.turn_action_visibility(
            player,
            extra_condition=(self.options.allow_full_word_guess and self.phase == "guessing" and player.id == self.guesser_id),
        )

    def _is_set_bot_difficulty_enabled(self, player: Player) -> str | None:
        if self.status != "waiting":
            return "action-game-in-progress"
        if player.name != self.host:
            return "action-not-host"
        if not any(p.is_bot for p in self.players):
            return "action-no-bots"
        return None

    def _is_set_bot_difficulty_hidden(self, player: Player) -> Visibility:
        if self.status != "waiting" or player.name != self.host:
            return Visibility.HIDDEN
        return Visibility.VISIBLE if any(p.is_bot for p in self.players) else Visibility.HIDDEN

    def _is_lifeline_reveal_enabled(self, player: Player) -> str | None:
        error = self._is_guess_word_enabled(player)
        if error:
            return error
        return None if isinstance(player, HanginWithFriendsPlayer) and player.lifeline_reveal > 0 else "action-not-available"

    def _is_lifeline_reveal_hidden(self, player: Player) -> Visibility:
        cond = isinstance(player, HanginWithFriendsPlayer) and player.lifeline_reveal > 0
        return self.turn_action_visibility(player, extra_condition=self.phase == "guessing" and player.id == self.guesser_id and cond)

    def _is_lifeline_remove_enabled(self, player: Player) -> str | None:
        error = self._is_guess_word_enabled(player)
        if error:
            return error
        if not isinstance(player, HanginWithFriendsPlayer) or player.lifeline_remove <= 0:
            return "action-not-available"
        if self.wrong_guesses <= 0:
            return "action-not-available"
        return None

    def _is_lifeline_remove_hidden(self, player: Player) -> Visibility:
        cond = isinstance(player, HanginWithFriendsPlayer) and player.lifeline_remove > 0 and self.wrong_guesses > 0
        return self.turn_action_visibility(player, extra_condition=self.phase == "guessing" and player.id == self.guesser_id and cond)

    def _is_lifeline_retry_enabled(self, player: Player) -> str | None:
        error = self._is_guess_word_enabled(player)
        if error:
            return error
        if not isinstance(player, HanginWithFriendsPlayer) or player.lifeline_retry <= 0:
            return "action-not-available"
        if player.retry_shield_active:
            return "action-not-available"
        return None

    def _is_lifeline_retry_hidden(self, player: Player) -> Visibility:
        cond = isinstance(player, HanginWithFriendsPlayer) and player.lifeline_retry > 0 and not player.retry_shield_active
        return self.turn_action_visibility(player, extra_condition=self.phase == "guessing" and player.id == self.guesser_id and cond)

    def _get_guess_letter_label(self, player: Player, action_id: str) -> str:
        letter = action_id.rsplit("_", 1)[-1]
        return f"Guess {letter.upper()}"

    # actions
    def _action_choose_word(self, player: Player, input_value: str, action_id: str) -> None:
        self.play_sound(SOUNDS["click"])
        word = self._normalize_word(input_value)
        user = self.get_user(player)
        if word is None:
            self.play_sound(SOUNDS["submit_invalid"])
            if user:
                user.speak("Word must contain letters only.", "table")
            return

        if not (self.options.min_word_length <= len(word) <= self.options.max_word_length):
            self.play_sound(SOUNDS["submit_invalid"])
            if user:
                user.speak(f"Word must be {self.options.min_word_length}-{self.options.max_word_length} letters.", "table")
            return

        if self.options.dictionary_mode != "off" and not self._word_uses_rack(word):
            self.play_sound(SOUNDS["submit_invalid"])
            if user:
                user.speak("Word must use only the rack letters.", "table")
            return

        if self.options.dictionary_mode == "strict" and self._dictionary_loaded and word not in self._dictionary_words:
            self.play_sound(SOUNDS["submit_invalid"])
            if user:
                user.speak("Word must be in the dictionary for strict mode.", "table")
            return

        self.secret_word = word
        self.masked_word = "".join("_" for _ in word)
        self.max_wrong_guesses = self.options.base_wrong_guesses + len(word)

        guesser = self.get_player_by_id(self.guesser_id)
        setter = self.get_player_by_id(self.setter_id)
        if guesser is None or setter is None:
            return

        self.play_sound(SOUNDS["submit_valid"])
        self.play_sound(SOUNDS["menu_close"])
        self._spin_wheel(guesser)

        self.phase = "guessing"
        self.current_player = guesser
        self.broadcast(
            f"Word selected. The word has {len(word)} letters. Wrong guesses allowed: {self.max_wrong_guesses}."
        )
        self._broadcast_private_to_spectators(f"Secret word chosen by {setter.name}: {self.secret_word.upper()}")
        self._announce_guess_state()

        if guesser.is_bot:
            BotHelper.jolt_bot(guesser, ticks=random.randint(6, 12))
        self.rebuild_all_menus()

    def _action_guess_letter(self, player: Player, action_id: str) -> None:
        self.play_sound(SOUNDS["click2"], volume=80)
        letter = action_id.rsplit("_", 1)[-1]
        self._resolve_letter_guess(letter)

    def _action_guess_word(self, player: Player, input_value: str, action_id: str) -> None:
        self.play_sound(SOUNDS["click"])
        if not self.options.allow_full_word_guess:
            return

        guess = self._normalize_word(input_value)
        if guess is None:
            user = self.get_user(player)
            if user:
                user.speak("Word guess must contain letters only.", "table")
            return

        if guess == self.secret_word:
            self.play_sound(SOUNDS["history_correct"])
            self._resolve_round(guesser_solved=True)
            return

        self._apply_wrong_guess(player)
        self.broadcast(
            f"{player.name} guessed the wrong word. {self.max_wrong_guesses - self.wrong_guesses} mistakes left."
        )
        if self.wrong_guesses >= self.max_wrong_guesses:
            self._resolve_round(guesser_solved=False)
            return
        self._announce_guess_state()
        self.rebuild_all_menus()

    def _action_lifeline_reveal(self, player: Player, action_id: str) -> None:
        if not isinstance(player, HanginWithFriendsPlayer) or player.lifeline_reveal <= 0:
            return
        hidden_positions = [idx for idx, ch in enumerate(self.masked_word) if ch == "_"]
        if not hidden_positions:
            return
        target_idx = random.choice(hidden_positions)
        target_letter = self.secret_word[target_idx]

        player.lifeline_reveal -= 1
        self.play_sound(SOUNDS["use_lifeline"])
        self.play_sound(SOUNDS["lifeline_slide"])
        self.broadcast(f"{player.name} used reveal lifeline.")
        self._resolve_letter_guess(target_letter, from_lifeline=True)

    def _action_lifeline_remove(self, player: Player, action_id: str) -> None:
        if not isinstance(player, HanginWithFriendsPlayer) or player.lifeline_remove <= 0:
            return
        if self.wrong_guesses <= 0:
            return
        player.lifeline_remove -= 1
        self.wrong_guesses = max(0, self.wrong_guesses - 1)
        self.play_sound(SOUNDS["use_lifeline"])
        self.play_sound(SOUNDS["lifeline_bounce"])
        self.broadcast(f"{player.name} removed one strike with a lifeline.")
        self._announce_guess_state()
        self.rebuild_all_menus()

    def _action_lifeline_retry(self, player: Player, action_id: str) -> None:
        if not isinstance(player, HanginWithFriendsPlayer) or player.lifeline_retry <= 0:
            return
        if player.retry_shield_active:
            return
        player.lifeline_retry -= 1
        player.retry_shield_active = True
        self.play_sound(SOUNDS["use_lifeline"])
        self.play_sound(SOUNDS["lifeline_bounce"])
        self.broadcast(f"{player.name} activated retry shield lifeline.")
        self.rebuild_all_menus()

    def _action_set_bot_difficulty(self, player: Player, value: str, action_id: str) -> None:
        try:
            bot_name, difficulty = value.split("|", 1)
        except ValueError:
            return
        bot = next((p for p in self.players if p.is_bot and p.name == bot_name), None)
        if bot is None:
            return
        selected = self._normalize_bot_difficulty(difficulty)
        self.bot_difficulties[bot.id] = selected
        self.play_sound(SOUNDS["click"])
        self.broadcast(f"{bot.name} bot difficulty set to {selected}.")
        self.rebuild_all_menus()

    # round mechanics
    def _spin_wheel(self, guesser: HanginWithFriendsPlayer) -> None:
        self.play_sound(SOUNDS["enter_wheel"])
        self.play_sound(SOUNDS["roulette"])
        self.schedule_sound(SOUNDS["roulette_ping"], delay_ticks=8)
        self.schedule_sound(SOUNDS["roulette_ping"], delay_ticks=16)
        self.schedule_sound(SOUNDS["roulette_ping"], delay_ticks=24)

        rng = random.Random(self.rng_seed + (self.round * 997) + len(self.secret_word))
        outcome = rng.choice(WHEEL_OUTCOMES)
        self.wheel_result = outcome
        self.play_sound(SOUNDS["drop"])

        if outcome == "coin_bonus":
            guesser.coins += 10
            self.play_sound(SOUNDS["buy_points"])
            self.play_sound(SOUNDS["pickup"])
            self.broadcast(f"Wheel: coin bonus. {guesser.name} gains 10 coins.")
        elif outcome == "extra_guess":
            self.max_wrong_guesses += 1
            self.play_sound(SOUNDS["pickup"])
            self.broadcast("Wheel: extra guess this round.")
        elif outcome == "fewer_guess":
            self.max_wrong_guesses = max(1, self.max_wrong_guesses - 1)
            self.play_sound(SOUNDS["drop"])
            self.broadcast("Wheel: one fewer guess this round.")
        elif outcome == "double_points":
            self.round_points_multiplier = 2
            self.play_sound(SOUNDS["multiplier"])
            self.broadcast("Wheel: double points this round.")
        elif outcome == "lifeline_reveal":
            guesser.lifeline_reveal += 1
            self.play_sound(SOUNDS["pickup"])
            self.play_sound(SOUNDS["lifeline_slide"])
            self.broadcast(f"Wheel: {guesser.name} gains a reveal lifeline.")
        elif outcome == "lifeline_remove":
            guesser.lifeline_remove += 1
            self.play_sound(SOUNDS["pickup"])
            self.play_sound(SOUNDS["lifeline_bounce"])
            self.broadcast(f"Wheel: {guesser.name} gains a remove-strike lifeline.")
        elif outcome == "lifeline_retry":
            guesser.lifeline_retry += 1
            self.play_sound(SOUNDS["pickup"])
            self.play_sound(SOUNDS["lifeline_bounce"])
            self.broadcast(f"Wheel: {guesser.name} gains a retry-shield lifeline.")
        else:
            self.play_sound(SOUNDS["click2"])
            self.broadcast("Wheel: no bonus this round.")

    def _resolve_letter_guess(self, letter: str, from_lifeline: bool = False) -> None:
        guesser = self.get_player_by_id(self.guesser_id)
        if not isinstance(guesser, HanginWithFriendsPlayer):
            return
        if letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)

        if letter in self.secret_word:
            masked = list(self.masked_word)
            for idx, char in enumerate(self.secret_word):
                if char == letter:
                    masked[idx] = char
            self.masked_word = "".join(masked)
            guesser.correct_streak += 1
            guesser.wrong_streak = 0
            self.play_sound(SOUNDS["history_correct"])
            self.play_sound(CORRECT_SEQUENCE_SOUNDS[min(guesser.correct_streak, 8) - 1])
            if not from_lifeline:
                self.broadcast(f"Correct. {letter.upper()} is in the word.")

            if "_" not in self.masked_word:
                self._resolve_round(guesser_solved=True)
                return
        else:
            self._apply_wrong_guess(guesser)
            self.broadcast(
                f"Wrong. {letter.upper()} is not in the word. {self.max_wrong_guesses - self.wrong_guesses} mistakes left."
            )
            if self.wrong_guesses >= self.max_wrong_guesses:
                self._resolve_round(guesser_solved=False)
                return

        self._announce_guess_state()
        self.rebuild_all_menus()

    def _apply_wrong_guess(self, guesser: HanginWithFriendsPlayer) -> None:
        if guesser.retry_shield_active:
            guesser.retry_shield_active = False
            self.play_sound(SOUNDS["lifeline_bounce"])
            self.play_sound(SOUNDS["history_incorrect"])
            self.broadcast("Retry shield blocked the strike.")
            return

        self.wrong_guesses += 1
        guesser.wrong_streak += 1
        guesser.correct_streak = 0
        self.play_sound(SOUNDS["history_incorrect"])
        index = min(guesser.wrong_streak, 8) - 1
        self.play_sound(INCORRECT_SEQUENCE_SOUNDS[index])

    def _resolve_round(self, guesser_solved: bool) -> None:
        setter = self.get_player_by_id(self.setter_id)
        guesser = self.get_player_by_id(self.guesser_id)
        if not isinstance(setter, HanginWithFriendsPlayer) or not isinstance(guesser, HanginWithFriendsPlayer):
            return

        self.phase = "round_end"
        points = self.round_points_multiplier
        if guesser_solved:
            setter.balloons_remaining -= 1
            self._award_score(guesser, points)
            self.play_sound(CORRECT_SEQUENCE_SOUNDS[7])
            self.play_sound(SOUNDS["balloon"])
            self.broadcast(f"{guesser.name} solved '{self.secret_word}'. {setter.name} loses a balloon.")
        else:
            guesser.balloons_remaining -= 1
            self._award_score(setter, points)
            self.play_sound(INCORRECT_SEQUENCE_SOUNDS[7])
            self.play_sound(SOUNDS["balloon"])
            self.broadcast(f"{guesser.name} failed to solve '{self.secret_word}'. {guesser.name} loses a balloon.")

        self._announce_balloons()

        if self._check_match_end():
            return
        self._start_round()

    def _award_score(self, player: HanginWithFriendsPlayer, points: int) -> None:
        player.score += points
        player.coins += points * 2
        self.play_sound(SOUNDS["score_flyup"])
        self.play_sound(SOUNDS["buy_points"])
        self._check_level_up(player)

    def _check_level_up(self, player: HanginWithFriendsPlayer) -> None:
        target_level = 1 + (player.score // 5)
        if target_level <= player.level:
            return
        player.level = target_level
        self.play_sound(SOUNDS["level_up"])
        self.play_sound(SOUNDS["level_up_missions"])
        self.play_sound(SOUNDS["popup"])
        self.broadcast(f"{player.name} reached level {player.level}.")

    def _announce_guess_state(self) -> None:
        masked = self._spoken_masked_word()
        guessed = ", ".join(l.upper() for l in sorted(self.guessed_letters)) or "none"
        self.broadcast(f"Word: {masked}. Guessed letters: {guessed}. Wrong {self.wrong_guesses}/{self.max_wrong_guesses}.")
        self._broadcast_spectator_player_boards()

    def _announce_balloons(self) -> None:
        parts = [f"{p.name}: {p.balloons_remaining} balloons" for p in self.get_active_players()]
        self.broadcast(" | ".join(parts))

    def _check_match_end(self) -> bool:
        active_players = self.get_active_players()
        if not active_players:
            return False

        ranked = sorted(active_players, key=lambda p: (p.score, p.balloons_remaining), reverse=True)
        winner = ranked[0]

        losers = [p for p in active_players if p.balloons_remaining <= 0]
        if losers:
            loser_names = ", ".join(p.name for p in losers)
            self._finish_with_winner(winner, f"{loser_names} ran out of balloons. {winner.name} wins the match.")
            return True

        if self.options.max_score > 0 and winner.score >= self.options.max_score:
            self._finish_with_winner(winner, f"Score limit {self.options.max_score} reached. {winner.name} wins the match.")
            return True

        if self.options.max_rounds > 0 and self.round >= self.options.max_rounds:
            self._finish_with_winner(winner, f"Round limit {self.options.max_rounds} reached. {winner.name} wins the match.")
            return True

        return False

    def _broadcast_private_to_spectators(self, text: str) -> None:
        if not self.options.spectators_see_all_actions:
            return
        for player in self.players:
            if not player.is_spectator:
                continue
            user = self.get_user(player)
            if user:
                user.speak(text, "table")

    def _broadcast_spectator_player_boards(self) -> None:
        if not self.options.spectators_see_all_actions:
            return
        for participant in self.get_active_players():
            if participant.is_spectator:
                continue
            self._broadcast_private_to_spectators(
                f"{participant.name} board: score {participant.score}, balloons {participant.balloons_remaining}, "
                f"coins {participant.coins}, reveal {participant.lifeline_reveal}, "
                f"remove {participant.lifeline_remove}, retry {participant.lifeline_retry}."
            )

    def _finish_with_winner(self, winner: HanginWithFriendsPlayer, message: str) -> None:
        self.phase = "game_end"
        self.broadcast(message)
        for p in self.get_active_players():
            user = self.get_user(p)
            if not user:
                continue
            if p.id == winner.id:
                user.play_sound(SOUNDS["win"])
            else:
                user.play_sound(SOUNDS["lose"])
        self.finish_game()

    # bot logic
    def bot_think(self, player: HanginWithFriendsPlayer) -> str | None:
        if self.phase == "choose_word" and player.id == self.setter_id:
            return "choose_word"
        if self.phase != "guessing" or player.id != self.guesser_id:
            return None

        # use lifelines first if needed
        if player.lifeline_remove > 0 and self.wrong_guesses >= max(1, self.max_wrong_guesses - 1):
            return "lifeline_remove"
        if player.lifeline_retry > 0 and not player.retry_shield_active and self.wrong_guesses >= max(1, self.max_wrong_guesses - 2):
            return "lifeline_retry"
        unknown_count = self.masked_word.count("_")
        if player.lifeline_reveal > 0 and unknown_count >= 4:
            return "lifeline_reveal"

        candidates = self._get_candidate_words()
        guess_limit = {"safe": 1, "balanced": 2, "risky": 4}.get(self.options.bot_guess_aggression, 2)
        if self.options.allow_full_word_guess and 0 < len(candidates) <= guess_limit:
            return "guess_word"

        letter = self._best_guess_letter(candidates)
        if not letter:
            for char in string.ascii_lowercase:
                if char not in self.guessed_letters:
                    letter = char
                    break
        return f"guess_letter_{letter}" if letter else None

    def _bot_choose_word_input(self, player: Player) -> str:
        candidates = self._get_words_for_rack()
        if not candidates:
            rack_letters = self.tile_rack[: self.options.max_word_length]
            return "".join(rack_letters[: self.options.min_word_length])
        return self._select_bot_word_by_difficulty(candidates, self._effective_bot_difficulty(player))

    def _bot_guess_word_input(self, player: Player) -> str:
        candidates = self._get_candidate_words()
        if candidates:
            return candidates[0]
        guess = self.masked_word.replace("_", "a")
        return guess if guess else "aaa"

    def _get_words_for_rack(self) -> list[str]:
        return [w for w in self._dictionary_words if self._word_uses_rack(w)]

    def _get_candidate_words(self) -> list[str]:
        if not self.secret_word:
            return []
        wrong_letters = {letter for letter in self.guessed_letters if letter not in self.secret_word}
        pattern = self.masked_word
        out: list[str] = []
        for word in self._dictionary_words:
            if len(word) != len(pattern):
                continue
            valid = True
            for idx, ch in enumerate(pattern):
                if ch != "_" and word[idx] != ch:
                    valid = False
                    break
                if ch == "_" and word[idx] in wrong_letters:
                    valid = False
                    break
            if valid:
                out.append(word)
        return out

    def _best_guess_letter(self, candidates: list[str]) -> str | None:
        freqs: dict[str, int] = {}
        guessed_set = set(self.guessed_letters)
        for word in candidates:
            for char in set(word):
                if char in guessed_set:
                    continue
                freqs[char] = freqs.get(char, 0) + 1
        if not freqs:
            return None
        return max(freqs.items(), key=lambda kv: (kv[1], kv[0]))[0]

    def _score_word(self, word: str) -> int:
        return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

    def _select_bot_word_by_difficulty(self, candidates: list[str], difficulty: str | None = None) -> str:
        ranked = sorted(candidates, key=lambda w: (self._score_word(w), len(w), w))
        bucketed = self._build_score_buckets(ranked)
        selected = self._normalize_bot_difficulty(difficulty or self.options.default_bot_difficulty)
        bucket_index = {"easy": 0, "medium": 1, "hard": 2, "extreme": 3}[selected]
        return bucketed[bucket_index][-1]

    def _build_score_buckets(self, ranked: list[str]) -> list[list[str]]:
        n = len(ranked)
        if n == 0:
            return [[], [], [], []]

        boundaries = [0, math.ceil(n * 0.25), math.ceil(n * 0.5), math.ceil(n * 0.75), n]
        buckets = [ranked[boundaries[i] : boundaries[i + 1]] for i in range(4)]

        for idx in range(4):
            if buckets[idx]:
                continue
            left = idx - 1
            right = idx + 1
            while left >= 0 or right <= 3:
                if left >= 0 and buckets[left]:
                    buckets[idx] = buckets[left]
                    break
                if right <= 3 and buckets[right]:
                    buckets[idx] = buckets[right]
                    break
                left -= 1
                right += 1

        return buckets

    def _normalize_bot_difficulty(self, value: str) -> str:
        normalized = value.strip().lower()
        return normalized if normalized in {"easy", "medium", "hard", "extreme"} else "medium"

    def _effective_bot_difficulty(self, player: Player) -> str:
        self._sync_bot_difficulty_overrides()
        if player.is_bot and player.id in self.bot_difficulties:
            return self._normalize_bot_difficulty(self.bot_difficulties[player.id])
        return self._normalize_bot_difficulty(self.options.default_bot_difficulty)

    def _sync_bot_difficulty_overrides(self) -> None:
        bot_ids = {p.id for p in self.players if p.is_bot}
        stale = [pid for pid in self.bot_difficulties if pid not in bot_ids]
        for pid in stale:
            self.bot_difficulties.pop(pid, None)

        default = self._normalize_bot_difficulty(self.options.default_bot_difficulty)
        for pid in bot_ids:
            self.bot_difficulties.setdefault(pid, default)

    def _per_bot_difficulty_options(self, player: Player) -> list[str]:
        self._sync_bot_difficulty_overrides()
        options: list[str] = []
        for bot in [p for p in self.players if p.is_bot]:
            for difficulty in BOT_DIFFICULTY_CHOICES:
                options.append(f"{bot.name}|{difficulty}")
        return options

    def _action_add_bot(self, player: Player, bot_name: str, action_id: str) -> None:
        super()._action_add_bot(player, bot_name, action_id)
        self._sync_bot_difficulty_overrides()

    def _action_remove_bot(self, player: Player, action_id: str) -> None:
        super()._action_remove_bot(player, action_id)
        self._sync_bot_difficulty_overrides()

    # utility
    def _generate_rack(self, round_number: int) -> list[str]:
        rng = random.Random(self.rng_seed + (round_number * 7919))
        return [rng.choice(LETTER_POOL).lower() for _ in range(self.options.rack_size)]

    def _word_uses_rack(self, word: str) -> bool:
        rack_counts = Counter(self.tile_rack)
        word_counts = Counter(word)
        return all(rack_counts.get(letter, 0) >= count for letter, count in word_counts.items())

    def _normalize_word(self, value: str) -> str | None:
        word = value.strip().lower()
        return word if word.isalpha() else None

    def _spoken_masked_word(self) -> str:
        """Format masked word for speech, using 'blank' for hidden letters."""
        parts = [("blank" if ch == "_" else ch.lower()) for ch in self.masked_word]
        return ", ".join(parts)

    def _load_dictionary(self) -> None:
        if self._dictionary_loaded:
            return
        candidate_paths = [Path(__file__).with_name("words.txt"), Path("/tmp/hanging/words.txt")]
        loaded: list[str] = []
        for path in candidate_paths:
            if not path.exists():
                continue
            loaded = self._read_words(path)
            if loaded:
                break

        self._dictionary_words = tuple(loaded) if loaded else tuple(DEFAULT_WORDS)
        self._dictionary_loaded = True

    def _read_words(self, path: Path) -> list[str]:
        words: set[str] = set()
        max_words = 50000
        with path.open("r", encoding="utf-8", errors="ignore") as fp:
            for line in fp:
                word = line.strip().lower()
                if not word.isalpha():
                    continue
                if not (self.options.min_word_length <= len(word) <= self.options.max_word_length):
                    continue
                words.add(word)
                if len(words) >= max_words:
                    break
        return sorted(words)

    def build_game_result(self) -> GameResult:
        players = self.get_active_players()
        winner = max(players, key=lambda p: (p.score, p.balloons_remaining), default=None)
        return GameResult(
            game_type=self.get_type(),
            timestamp=datetime.now().isoformat(),
            duration_ticks=self.sound_scheduler_tick,
            player_results=[
                PlayerResult(
                    player_id=p.id,
                    player_name=p.name,
                    is_bot=p.is_bot,
                    is_virtual_bot=getattr(p, "is_virtual_bot", False),
                )
                for p in players
            ],
            custom_data={
                "winner_name": winner.name if winner else None,
                "rounds_played": self.round,
                "scores": {p.name: p.score for p in players},
                "balloons": {p.name: p.balloons_remaining for p in players},
                "coins": {p.name: p.coins for p in players},
                "wheel_result": self.wheel_result,
            },
        )

    def format_end_screen(self, result: GameResult, locale: str) -> list[str]:
        lines = [Localization.get(locale, "game-final-scores-header")]
        balloons = result.custom_data.get("balloons", {})
        scores = result.custom_data.get("scores", {})
        coins = result.custom_data.get("coins", {})
        for name in sorted(scores.keys()):
            lines.append(
                f"{name}: score {scores.get(name, 0)}, balloons {balloons.get(name, 0)}, coins {coins.get(name, 0)}"
            )
        winner = result.custom_data.get("winner_name")
        if winner:
            lines.append(f"Winner: {winner}")
        return lines
