import json
from unittest.mock import Mock

import pytest

from server.core.users.test_user import MockUser
from server.game_utils.actions import Action, ActionSet, Visibility
from server.games.pig.game import PigGame


class DummyGame:
    def _enabled(self, player, *, action_id: str | None = None) -> str | None:
        return None

    def _hidden(self, player, *, action_id: str | None = None) -> Visibility:
        return Visibility.VISIBLE


class DummyPlayer:
    pass


def test_actions_menu_respects_show_in_actions_menu():
    action_set = ActionSet(name="turn")
    action_set.add(
        Action(
            id="shown",
            label="Shown",
            handler="_action",
            is_enabled="_enabled",
            is_hidden="_hidden",
        )
    )
    action_set.add(
        Action(
            id="hidden",
            label="Hidden",
            handler="_action",
            is_enabled="_enabled",
            is_hidden="_hidden",
            show_in_actions_menu=False,
        )
    )
    game = DummyGame()
    player = DummyPlayer()

    enabled = action_set.get_enabled_actions(game, player)
    assert [ra.action.id for ra in enabled] == ["shown"]


def test_saved_action_metadata_without_removed_spectator_field_loads():
    game = PigGame()
    player = game.create_player("p1", "Alice")
    game.players = [player]
    game.setup_player_actions(player)
    payload = json.loads(game.to_json())
    for action_sets in payload["player_action_sets"].values():
        for action_set in action_sets:
            for action in action_set["_actions"].values():
                action["include_spectators"] = True

    restored = PigGame.from_dict(payload)

    assert restored.player_action_sets["p1"]


@pytest.mark.parametrize("spectator", [False, True])
def test_f5_opens_actions_menu_and_back_resumes_game_menu(spectator):
    game = PigGame()
    user = MockUser("Alice")
    game.initialize_lobby("Alice", user)
    player = game.players[0]
    player.is_spectator = spectator
    user.messages.clear()

    game.handle_event(player, {"type": "keybind", "key": "escape"})
    assert player.id not in game._actions_menu_open
    game.handle_event(player, {"type": "keybind", "key": "f5"})
    assert player.id in game._actions_menu_open
    assert user.messages[-1].data["menu_id"] == "actions_menu"

    game.handle_event(player, {
        "type": "menu", "menu_id": "actions_menu", "selection_id": "go_back",
    })
    assert player.id not in game._actions_menu_open
    assert user.messages[-1].data["menu_id"] == "turn_menu"


@pytest.mark.parametrize("event", [
    {"type": "menu", "menu_id": "turn_menu", "selection_id": "roll"},
    {"type": "menu", "menu_id": "actions_menu", "selection_id": "roll"},
    {"type": "keybind", "key": "r"},
])
def test_all_command_routes_format_disabled_reasons_and_protect_pending_input(event):
    game = PigGame()
    user = MockUser("Alice")
    player = game.add_player("Alice", user)
    game.status = "playing"
    game.setup_keybinds()
    game._is_roll_enabled = lambda player: ("reason-with-arguments", {"points": 5})
    game._action_roll = Mock()
    user.speak_l = Mock()

    game.handle_event(player, event)

    user.speak_l.assert_called_once_with("reason-with-arguments", points=5)
    game._action_roll.assert_not_called()

    user.speak_l.reset_mock()
    game._pending_actions[player.id] = "confirmation"
    game.handle_event(player, event)

    user.speak_l.assert_not_called()
    game._action_roll.assert_not_called()
    assert game._pending_actions[player.id] == "confirmation"
