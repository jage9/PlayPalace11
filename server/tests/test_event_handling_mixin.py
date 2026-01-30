"""Targeted tests for the EventHandlingMixin behaviors."""

from dataclasses import dataclass

from server.games.base import Player, ActionContext

from server.game_utils.event_handling_mixin import EventHandlingMixin


@dataclass
class DummyAction:
    id: str


@dataclass
class DummyResolved:
    action: DummyAction
    enabled: bool = True
    disabled_reason: str | None = None


class DummyUser:
    def __init__(self):
        self.removed = []
        self.spoken = []

    def remove_menu(self, menu_id: str) -> None:
        self.removed.append(menu_id)

    def speak_l(self, message_id: str, **_: object) -> None:
        self.spoken.append(message_id)


class DummyKeybind:
    def __init__(self, actions: list[str], *, allow: bool = True, requires_focus: bool = False):
        self.actions = actions
        self._allow = allow
        self.requires_focus = requires_focus

    def can_player_use(self, _game, _player, _is_spectator: bool = False) -> bool:
        return self._allow


class DummyGame(EventHandlingMixin):
    def __init__(self):
        self._actions_menu_open: set[str] = set()
        self._pending_actions: dict[str, str] = {}
        self._status_box_open: set[str] = set()
        self._keybinds: dict[str, list[DummyKeybind]] = {}
        self._visible_actions: list[DummyResolved] = []
        self._actions: dict[str, DummyAction] = {}
        self._resolved: dict[str, DummyResolved] = {}
        self._users: dict[str, DummyUser] = {}
        self.executed: list[tuple[str, str, dict]] = []
        self.rebuild_all_calls = 0
        self.rebuild_player_calls = 0
        self.leave_requests: list[str] = []

    # Helpers for tests
    def register_action(self, action_id: str, *, enabled: bool = True, disabled_reason: str | None = None) -> None:
        action = DummyAction(action_id)
        self._actions[action_id] = action
        self._resolved[action_id] = DummyResolved(action, enabled=enabled, disabled_reason=disabled_reason)

    def set_visible_actions(self, resolved: list[DummyResolved]) -> None:
        self._visible_actions = resolved

    # Methods used by mixin
    def get_user(self, player: Player) -> DummyUser | None:
        return self._users.get(player.id)

    def find_action(self, _player: Player, action_id: str) -> DummyAction | None:
        return self._actions.get(action_id)

    def resolve_action(self, _player: Player, action: DummyAction) -> DummyResolved:
        return self._resolved[action.id]

    def execute_action(self, player: Player, action_id: str, input_value=None, context=None) -> None:
        self.executed.append(
            (
                player.id,
                action_id,
                {
                    "input": input_value,
                    "context": context,
                },
            )
        )

    def get_all_visible_actions(self, _player: Player) -> list[DummyResolved]:
        return self._visible_actions

    def rebuild_all_menus(self) -> None:
        self.rebuild_all_calls += 1

    def rebuild_player_menu(self, _player: Player) -> None:
        self.rebuild_player_calls += 1

    def _is_player_spectator(self, player: Player) -> bool:
        return player.is_spectator

    def _perform_leave_game(self, player: Player) -> None:
        self.leave_requests.append(player.id)


def make_player(player_id: str = "p1") -> Player:
    return Player(id=player_id, name=f"Player-{player_id}")


def test_turn_menu_selection_by_id_executes_action():
    game = DummyGame()
    player = make_player()
    game._actions_menu_open.add(player.id)
    game.register_action("attack")

    game.handle_event(
        player,
        {"type": "menu", "menu_id": "turn_menu", "selection_id": "attack"},
    )

    assert player.id not in game._actions_menu_open
    assert game.executed == [(player.id, "attack", {"input": None, "context": None})]
    assert game.rebuild_all_calls == 1


def test_turn_menu_selection_by_index_fallback():
    game = DummyGame()
    player = make_player("p2")
    disabled = DummyResolved(DummyAction("wait"), enabled=False)
    enabled = DummyResolved(DummyAction("defend"), enabled=True)
    game.set_visible_actions([disabled, enabled])
    game.register_action("defend")  # needed for execute lookup
    game._resolved["defend"] = enabled

    game.handle_event(
        player,
        {"type": "menu", "menu_id": "turn_menu", "selection": 2},
    )

    assert game.executed[-1] == (player.id, "defend", {"input": None, "context": None})
    assert game.rebuild_all_calls == 1


def test_action_input_menu_executes_and_clears_pending():
    game = DummyGame()
    player = make_player()
    game._pending_actions[player.id] = "cast_spell"
    game.register_action("cast_spell")

    game.handle_event(
        player,
        {
            "type": "menu",
            "menu_id": "action_input_menu",
            "selection_id": "fireball",
        },
    )

    assert player.id not in game._pending_actions
    assert game.executed[-1] == (
        player.id,
        "cast_spell",
        {"input": "fireball", "context": None},
    )
    assert game.rebuild_player_calls == 1


def test_leave_game_confirm_yes_calls_handler_and_clears_state():
    game = DummyGame()
    player = make_player()
    user = DummyUser()
    game._users[player.id] = user
    game._pending_actions[player.id] = "confirm_leave"

    game.handle_event(
        player,
        {"type": "menu", "menu_id": "leave_game_confirm", "selection": 1},
    )

    assert "leave_game_confirm" in user.removed
    assert player.id not in game._pending_actions
    assert game.leave_requests == [player.id]
    assert game.rebuild_player_calls == 1


def test_keybind_event_executes_enabled_and_speaks_disabled():
    game = DummyGame()
    player = make_player()
    user = DummyUser()
    game._users[player.id] = user
    game._keybinds["space"] = [
        DummyKeybind(["needs_energy"]),
        DummyKeybind(["jump"]),
    ]
    game.register_action("needs_energy", enabled=False, disabled_reason="not-ready")
    game.register_action("jump", enabled=True)

    game.handle_event(player, {"type": "keybind", "key": "SPACE"})

    assert user.spoken == ["not-ready"]
    executed = game.executed[-1]
    assert executed[:2] == (player.id, "jump")
    context = executed[2]["context"]
    assert isinstance(context, ActionContext)
    assert context.from_keybind
    assert game.rebuild_all_calls == 1
