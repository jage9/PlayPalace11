"""Table lifecycle and transition checks across all registered games."""

from unittest.mock import Mock

import pytest

from server.game_utils.game_status import GameStatus
from server.games.registry import GameRegistry
from server.tests.test_game_lifecycle import make_table


GAME_CLASSES = [
    game_class
    for game_class in GameRegistry.get_all()
    if game_class.get_type() != "roulette"
]


def _compatible_target(game_type: str, player_count: int):
    return next(
        game_class
        for game_class in GAME_CLASSES
        if game_class.get_type() != game_type
        and game_class.get_min_players() <= player_count <= game_class.get_max_players()
    )


@pytest.mark.parametrize("game_class", GAME_CLASSES, ids=lambda cls: cls.get_type())
def test_host_can_stop_restart_and_change_each_game(game_class):
    table = make_table(game_class)
    table._server = Mock()
    game = table.game
    host = game.get_player_by_name("Alice")
    host_user = game.get_user(host)

    game.execute_action(host, "start_game")
    assert game.status == table.status == GameStatus.PLAYING
    assert "game_menu" in host_user.menus

    host_user.show_menu("stale_options", ["stale"])
    host_user.show_editbox("action_input_editbox", "stale")
    game._pending_actions[host.id] = "stale_action"
    game.schedule_event("stale_event", {}, delay_ticks=100)
    game.schedule_sound("click.ogg", delay_ticks=100)
    old_options = getattr(game, "options", None)

    game.execute_action(host, "stop_game")

    stopped = table.game
    assert stopped is not game
    assert stopped.status == table.status == GameStatus.WAITING
    if old_options is not None:
        assert stopped.options == old_options
        assert stopped.options is not old_options
    assert "stale_options" not in host_user.menus
    assert not host_user.editboxes
    assert not game._pending_actions
    assert not game.event_queue and not game.scheduled_sounds
    assert not stopped._pending_actions
    assert table._server.on_game_result.call_count == 0

    stopped_host = stopped.get_player_by_name("Alice")
    stopped.execute_action(stopped_host, "start_game")
    assert stopped.status == table.status == GameStatus.PLAYING
    stopped.finish_game()
    assert stopped.status == table.status == GameStatus.FINISHED

    target = _compatible_target(stopped.get_type(), len(stopped.players))
    stopped_host = stopped.get_player_by_name("Alice")
    stopped.handle_event(
        stopped_host,
        {"type": "menu", "menu_id": "game_over", "selection_id": "change_game"},
    )
    stopped.handle_event(
        stopped_host,
        {
            "type": "menu",
            "menu_id": "transient_display",
            "selection_id": target.get_type(),
        },
    )

    changed = table.game
    target_defaults = getattr(target(), "options", None)
    stopped_options = getattr(stopped, "options", None)
    assert changed is not stopped
    assert changed.get_type() == target.get_type()
    assert changed.status == table.status == GameStatus.WAITING
    if target_defaults is not None:
        assert changed.options == target_defaults
        assert changed.options is not target_defaults
        if stopped_options is not None:
            assert changed.options is not stopped_options

    # Exercise every game as a switch destination too, while another game is running.
    changed_host = changed.get_player_by_name("Alice")
    changed.execute_action(changed_host, "start_game")
    changed.execute_action(changed_host, "change_game")
    changed.rebuild_all_menus()  # Turn updates must not replace the open game chooser.
    assert changed._get_transient_display_state(changed_host).kind == "change_game"
    changed.handle_event(changed_host, {
        "type": "menu", "menu_id": "transient_display", "selection_id": game_class.get_type(),
    })
    returned = table.game
    assert returned.get_type() == game_class.get_type()
    assert getattr(returned, "options", None) == getattr(game_class(), "options", None)
    assert returned.status == table.status == GameStatus.WAITING
    assert not returned._transient_display_state
