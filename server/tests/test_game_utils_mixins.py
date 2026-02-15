import json
import threading
from dataclasses import dataclass
from types import SimpleNamespace

from server.game_utils.action_execution_mixin import ActionExecutionMixin
from server.game_utils.actions import Action, MenuInput, EditboxInput, ResolvedAction
from server.game_utils.duration_estimate_mixin import DurationEstimateMixin
from server.game_utils.game_prediction_mixin import GamePredictionMixin
from server.game_utils.game_scores_mixin import GameScoresMixin
from server.game_utils.options import GameOptions, MenuOption, option_field
from server.core.users.base import EscapeBehavior, MenuItem, TrustLevel
from server.games.base import Player
from server.messages.localization import Localization


class StubUser:
    def __init__(self, locale: str = "en", trust_level: TrustLevel = TrustLevel.ADMIN):
        self.locale = locale
        self.trust_level = trust_level
        self.spoken = []
        self.menus = []
        self.editboxes = []

    def speak(self, text: str, buffer: str = "misc") -> None:
        self.spoken.append(("speak", text, buffer))

    def speak_l(self, key: str, buffer: str = "misc", **kwargs) -> None:
        self.spoken.append(("speak_l", key, buffer, kwargs))

    def show_menu(
        self,
        menu_id: str,
        items: list[str | MenuItem],
        *,
        multiletter: bool = True,
        escape_behavior: EscapeBehavior = EscapeBehavior.KEYBIND,
        position: int | None = None,
        grid_enabled: bool = False,
        grid_width: int = 1,
    ) -> None:
        self.menus.append(
            {
                "menu_id": menu_id,
                "items": items,
                "multiletter": multiletter,
                "escape_behavior": escape_behavior,
                "position": position,
                "grid_enabled": grid_enabled,
                "grid_width": grid_width,
            }
        )

    def show_editbox(self, menu_id: str, prompt: str, default: str) -> None:
        self.editboxes.append((menu_id, prompt, default))


class DummyPredictionGame(GamePredictionMixin):
    def __init__(self, user_map: dict[str, StubUser]):
        self.players: list[Player] = []
        self._table = SimpleNamespace(_db=object())
        self._users = user_map
        self.status_calls: list[tuple[str, list[str]]] = []

    def get_user(self, player: Player) -> StubUser | None:
        return self._users.get(player.id)

    def get_type(self) -> str:
        return "dummy-prediction"

    def status_box(self, player: Player, lines: list[str]) -> None:
        self.status_calls.append((player.id, lines))


def test_prediction_requires_db(monkeypatch):
    user = StubUser()
    game = DummyPredictionGame({"p1": user})
    player = Player(id="p1", name="Alice")
    game.players = [player]
    game._table = SimpleNamespace(_db=None)

    game._action_predict_outcomes(player, "predict")

    assert ("speak_l", "predict-unavailable", "misc", {}) in user.spoken
    assert game.status_calls == []


def test_prediction_needs_two_humans(monkeypatch):
    user = StubUser()
    other_user = StubUser()
    game = DummyPredictionGame({"p1": user, "p2": other_user})
    p1 = Player(id="p1", name="Alice")
    spectator = Player(id="p2", name="Bob", is_spectator=True)
    game.players = [p1, spectator]

    game._action_predict_outcomes(p1, "predict")

    assert ("speak_l", "predict-need-players", "misc", {}) in user.spoken
    assert game.status_calls == []


def test_prediction_formats_results(monkeypatch):
    user = StubUser()
    other_user = StubUser()
    game = DummyPredictionGame({"p1": user, "p2": other_user})
    p1 = Player(id="p1", name="Alice")
    p2 = Player(id="p2", name="Bob")
    game.players = [p1, p2]

    class DummyRating:
        def __init__(self, ordinal: float):
            self.ordinal = ordinal

    class DummyRatingHelper:
        def __init__(self, db, game_type):
            self.calls = []

        def get_rating(self, player_id: str):
            return DummyRating({"p1": 30, "p2": 20}[player_id])

        def predict_win_probability(self, player_id: str, other_id: str) -> float:
            assert {player_id, other_id} == {"p1", "p2"}
            return 0.65 if player_id == "p1" else 0.35

    monkeypatch.setattr(
        "server.game_utils.game_prediction_mixin.RatingHelper",
        DummyRatingHelper,
    )

    game._action_predict_outcomes(p1, "predict")

    assert not user.spoken  # status box used instead
    assert game.status_calls
    _, lines = game.status_calls[0]
    assert lines[0] == Localization.get("en", "predict-header")
    assert "Alice" in lines[1] and "%" in lines[1]


class DummyActionGame(ActionExecutionMixin):
    def __init__(self):
        self._pending_actions: dict[str, str] = {}
        self._action_context: dict[str, object] = {}
        self.actions: dict[str, Action] = {}
        self.resolved: dict[tuple[str, str], ResolvedAction] = {}
        self.users: dict[str, StubUser] = {}
        self.handler_calls: list[tuple] = []
        self.options: GameOptions | None = None

    def register(
        self,
        action: Action,
        player_id: str,
        resolved: ResolvedAction,
        user: StubUser,
    ) -> None:
        self.actions[action.id] = action
        self.resolved[(player_id, action.id)] = resolved
        self.users[player_id] = user

    def get_user(self, player: Player) -> StubUser | None:
        return self.users.get(player.id)

    def find_action(self, player: Player, action_id: str) -> Action | None:
        return self.actions.get(action_id)

    def resolve_action(self, player: Player, action: Action) -> ResolvedAction:
        return self.resolved[(player.id, action.id)]

    def advance_turn(self) -> None:
        self.handler_calls.append(("advance",))

    def _handle_simple(self, player: Player, action_id: str) -> None:
        self.handler_calls.append(("simple", player.id, action_id))

    def _handle_with_input(self, player: Player, value: str, action_id: str) -> None:
        self.handler_calls.append(("input", player.id, action_id, value))

    def get_choices(self, player: Player) -> list[str]:
        return ["alpha", "beta"]

    def choose_for_bot(self, player: Player, options: list[str]) -> str:
        return options[-1]

    def bot_text_input(self, player: Player) -> str:
        return "bot-value"

    def dynamic_options(self, player: Player) -> list[str]:
        return ["first", "second"]

    def no_options(self, player: Player) -> list[str]:
        return []

    def bot_editbox_choice(self, player: Player) -> str:
        return "typed-by-bot"


@dataclass
class SampleExecOptions(GameOptions):
    mode: str = option_field(
        MenuOption(
            default="classic",
            choices=["classic", "neon"],
            label="set-mode",
            prompt="mode-prompt",
            change_msg="mode-change",
            choice_labels={"classic": "mode-classic", "neon": "mode-neon"},
        )
    )


def test_execute_action_disabled_speaks_reason(monkeypatch):
    game = DummyActionGame()
    user = StubUser()
    player = Player(id="p1", name="Alice")
    action = Action(
        id="do",
        label="Do",
        handler="_handle_simple",
        is_enabled="",
        is_hidden="",
    )
    resolved = ResolvedAction(
        action=action,
        label="Do",
        enabled=False,
        disabled_reason="not-now",
        visible=True,
    )
    game.register(action, player.id, resolved, user)

    game.execute_action(player, "do")

    assert ("speak_l", "not-now", "misc", {}) in user.spoken
    assert ("simple", player.id, "do") not in game.handler_calls


def test_execute_action_requests_menu_input_for_human(monkeypatch):
    game = DummyActionGame()
    user = StubUser()
    player = Player(id="p1", name="Alice")
    menu_input = MenuInput(prompt="choose", options="get_choices")
    action = Action(
        id="configure",
        label="Configure",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=menu_input,
    )
    resolved = ResolvedAction(
        action=action,
        label="Configure",
        enabled=True,
        disabled_reason=None,
        visible=True,
    )
    game.register(action, player.id, resolved, user)

    game.execute_action(player, "configure")

    assert game._pending_actions[player.id] == "configure"
    assert user.menus
    menu_info = user.menus[0]
    assert menu_info["menu_id"] == "action_input_menu"
    assert menu_info["escape_behavior"] is EscapeBehavior.SELECT_LAST
    labels = [item.text for item in menu_info["items"] if isinstance(item, MenuItem)]
    assert Localization.get("en", "cancel") in labels


def test_execute_action_bot_input(monkeypatch):
    game = DummyActionGame()
    bot_user = StubUser()
    player = Player(id="p2", name="Bot", is_bot=True)
    menu_input = MenuInput(
        prompt="choose",
        options="get_choices",
        bot_select="choose_for_bot",
    )
    action = Action(
        id="configure",
        label="Configure",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=menu_input,
    )
    resolved = ResolvedAction(
        action=action,
        label="Configure",
        enabled=True,
        disabled_reason=None,
        visible=True,
    )
    game.register(action, player.id, resolved, bot_user)

    game.execute_action(player, "configure")

    assert ("input", player.id, "configure", "beta") in game.handler_calls
    assert player.id not in game._pending_actions


def test_execute_action_unknown_action_noop():
    game = DummyActionGame()
    player = Player(id="p1", name="Alice")

    game.execute_action(player, "missing")

    assert game.handler_calls == []


def test_execute_action_handler_missing():
    game = DummyActionGame()
    user = StubUser()
    player = Player(id="p1", name="Alice")
    action = Action(
        id="noop",
        label="Do nothing",
        handler="_does_not_exist",
        is_enabled="",
        is_hidden="",
    )
    resolved = ResolvedAction(
        action=action,
        label="Do nothing",
        enabled=True,
        disabled_reason=None,
        visible=True,
    )
    game.register(action, player.id, resolved, user)

    game.execute_action(player, "noop")

    assert game.handler_calls == []
    assert player.id not in game._action_context


def test_execute_action_bot_menu_without_options():
    game = DummyActionGame()
    bot_user = StubUser()
    player = Player(id="p2", name="Bot", is_bot=True)
    menu_input = MenuInput(
        prompt="choose",
        options="no_options",
        bot_select="choose_for_bot",
    )
    action = Action(
        id="configure",
        label="Configure",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=menu_input,
    )
    resolved = ResolvedAction(
        action=action,
        label="Configure",
        enabled=True,
        disabled_reason=None,
        visible=True,
    )
    game.register(action, player.id, resolved, bot_user)

    game.execute_action(player, "configure")

    assert ("input", player.id, "configure", "beta") not in game.handler_calls
    assert player.id not in game._pending_actions


def test_get_menu_options_prefers_method():
    game = DummyActionGame()
    player = Player(id="p1", name="Alice")
    action = Action(
        id="choose",
        label="Choose",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=MenuInput(prompt="pick", options="dynamic_options"),
    )

    options = game._get_menu_options_for_action(action, player)

    assert options == ["first", "second"]


def test_get_menu_options_fallbacks_to_option_meta():
    game = DummyActionGame()
    game.options = SampleExecOptions()
    player = Player(id="p1", name="Alice")
    action = Action(
        id="set_mode",
        label="Mode",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=MenuInput(prompt="mode", options="missing_method"),
    )

    options = game._get_menu_options_for_action(action, player)

    assert options == ["classic", "neon"]


def test_get_bot_input_editbox_uses_custom_method():
    game = DummyActionGame()
    bot_user = StubUser()
    player = Player(id="p2", name="Bot", is_bot=True)
    edit_input = EditboxInput(prompt="enter", default="fallback", bot_input="bot_editbox_choice")
    action = Action(
        id="type",
        label="Type",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=edit_input,
    )
    resolved = ResolvedAction(
        action=action,
        label="Type",
        enabled=True,
        disabled_reason=None,
        visible=True,
    )
    game.register(action, player.id, resolved, bot_user)

    game.execute_action(player, "type")

    assert ("input", player.id, "type", "typed-by-bot") in game.handler_calls


def test_request_action_input_handles_missing_options():
    game = DummyActionGame()
    user = StubUser()
    player = Player(id="p1", name="Alice")
    game.users[player.id] = user
    action = Action(
        id="choose",
        label="Choose",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=MenuInput(prompt="pick", options="no_options"),
    )

    game._request_action_input(action, player)

    assert player.id not in game._pending_actions
    assert ("speak_l", "no-options-available", "misc", {}) in user.spoken


def test_request_action_input_editbox_shows_prompt():
    game = DummyActionGame()
    user = StubUser()
    player = Player(id="p1", name="Alice")
    game.users[player.id] = user
    action = Action(
        id="name",
        label="Name",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=EditboxInput(prompt="enter-name", default="Alice"),
    )

    game._request_action_input(action, player)

    assert game._pending_actions[player.id] == "name"
    assert user.editboxes[-1][0] == "action_input_editbox"


def test_request_action_input_menu_option_uses_choice_labels(monkeypatch):
    game = DummyActionGame()
    game.options = SampleExecOptions()
    user = StubUser()
    player = Player(id="p1", name="Alice")
    game.users[player.id] = user
    action = Action(
        id="set_mode",
        label="Mode",
        handler="_handle_with_input",
        is_enabled="",
        is_hidden="",
        input_request=MenuInput(prompt="mode", options="missing"),
    )

    def fake_get(locale, key, **kwargs):
        mapping = {
            "mode-classic": "Classic Label",
            "mode-neon": "Neon Label",
            "cancel": "Cancel",
            "set-mode": f"Mode {kwargs.get('mode', '')}",
        }
        return mapping.get(key, key)

    monkeypatch.setattr(
        "server.game_utils.action_execution_mixin.Localization.get",
        fake_get,
    )

    game._request_action_input(action, player)

    menu = user.menus[-1]
    texts = [item.text if isinstance(item, MenuItem) else item for item in menu["items"]]
    assert "Classic Label" in texts
    assert "Neon Label" in texts
    assert "Cancel" in texts


def test_get_action_context_returns_default():
    game = DummyActionGame()
    player = Player(id="p1", name="Alice")

    context = game.get_action_context(player)

    assert hasattr(context, "menu_item_id")
    assert player.id not in game._action_context


class DummyTeamManager:
    def __init__(self, has_teams: bool, brief: str = "", detailed: list[str] | None = None):
        self.teams = ["team"] if has_teams else []
        self._brief = brief
        self._detailed = detailed or ["line1", "line2"]

    def format_scores_brief(self, locale: str) -> str:
        return self._brief

    def format_scores_detailed(self, locale: str) -> list[str]:
        return self._detailed


class DummyScoresGame(GameScoresMixin):
    def __init__(self, team_manager, user_map):
        self.team_manager = team_manager
        self._users = user_map
        self.players: list[Player] = []
        self.current_player: Player | None = None
        self.status_boxes: list[tuple[str, list[str]]] = []

    def get_user(self, player: Player) -> StubUser | None:
        return self._users.get(player.id)

    def status_box(self, player: Player, lines: list[str]) -> None:
        self.status_boxes.append((player.id, lines))


def test_whose_turn_announces_player():
    user = StubUser()
    team_manager = DummyTeamManager(has_teams=False)
    game = DummyScoresGame(team_manager, {"p1": user})
    player = Player(id="p1", name="Alice")
    game.players = [player]
    game.current_player = Player(id="p2", name="Bob")

    game._action_whose_turn(player, "turn")

    assert ("speak_l", "game-turn-start", "misc", {"player": "Bob"}) in user.spoken


def test_check_scores_uses_team_manager(monkeypatch):
    user = StubUser()
    team_manager = DummyTeamManager(has_teams=True, brief="scores", detailed=["scores detailed"])
    game = DummyScoresGame(team_manager, {"p1": user})
    player = Player(id="p1", name="Alice")
    teammate = Player(id="p2", name="Bob")
    game.players = [player, teammate]

    game._action_whos_at_table(player, "who")
    game._action_check_scores(player, "check")
    game._action_check_scores_detailed(player, "check_detailed")

    spoken_keys = [entry[1] for entry in user.spoken if entry[0] == "speak_l"]
    assert "table-players-many" in spoken_keys
    assert ("speak", "scores", "misc") in user.spoken
    assert game.status_boxes[0][1] == ["scores detailed"]


class DummyDurationGame(DurationEstimateMixin):
    def __init__(self, user_map):
        self._estimate_threads = []
        self._estimate_results = []
        self._estimate_errors = []
        self._estimate_running = False
        self._estimate_lock = threading.Lock()
        self.players: list[Player] = []
        self._users = user_map
        self.broadcasts: list[tuple[str, dict]] = []
        self.messages: list[str] = []

    def get_user(self, player: Player) -> StubUser | None:
        return self._users.get(player.id)

    def broadcast_l(self, key: str, **kwargs) -> None:
        self.broadcasts.append((key, kwargs))

    def broadcast(self, message: str) -> None:
        self.messages.append(message)

    def get_type(self) -> str:
        return "duration-game"

    def get_min_players(self) -> int:
        return 2


def test_duration_estimate_runs_and_reports(monkeypatch):
    monkeypatch.setattr(
        "server.game_utils.duration_estimate_mixin.DurationEstimateMixin.NUM_ESTIMATE_SIMULATIONS",
        2,
    )

    calls = {"count": 0}

    def fake_run(*args, **kwargs):
        idx = calls["count"]
        calls["count"] += 1
        data = {"ticks": 100 + idx * 100}
        return SimpleNamespace(returncode=0, stdout=json.dumps(data), stderr="")

    class FakeThread:
        def __init__(self, target, daemon):
            self._target = target
            self._alive = True

        def start(self):
            self._target()
            self._alive = False

        def is_alive(self):
            return self._alive

    monkeypatch.setattr("server.game_utils.duration_estimate_mixin.subprocess.run", fake_run)
    monkeypatch.setattr("server.game_utils.duration_estimate_mixin.threading.Thread", FakeThread)

    user = StubUser()
    game = DummyDurationGame({"p1": user})
    player = Player(id="p1", name="Alice")
    game.players = [player]

    game._action_estimate_duration(player, "estimate")
    assert game._estimate_running
    assert ("estimate-computing", {}) in game.broadcasts

    game.check_estimate_completion()
    assert not game._estimate_running
    estimate_result = next(
        kwargs for key, kwargs in game.broadcasts if key == "estimate-result"
    )
    assert "bot_time" in estimate_result
    assert estimate_result["bot_time"] == "7 seconds"
    assert estimate_result["human_time"] == "15 seconds"


def test_duration_estimate_rejects_parallel_request(monkeypatch):
    user = StubUser()
    game = DummyDurationGame({"p1": user})
    player = Player(id="p1", name="Alice")
    game._estimate_running = True

    game._action_estimate_duration(player, "estimate")

    assert ("speak_l", "estimate-already-running", "misc", {}) in user.spoken
