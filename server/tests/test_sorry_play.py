"""Play and persistence tests for Sorry."""

import random

from server.core.users.bot import Bot
from server.core.users.test_user import MockUser
from server.games.sorry.game import SorryGame, SorryOptions
from server.games.sorry.state import SAFETY_LENGTH


def _set_track(pawn, position: int) -> None:
    pawn.zone = "track"
    pawn.track_position = position
    pawn.home_steps = 0


def _set_home(pawn) -> None:
    pawn.zone = "home"
    pawn.track_position = None
    pawn.home_steps = SAFETY_LENGTH + 1


def _assert_state_invariants(game: SorryGame) -> None:
    valid_zones = {"start", "track", "home_path", "home"}
    expected_pawns = game.get_rules_profile().pawns_per_player
    for player in game.players:
        state = game.game_state.player_states[player.id]
        assert len(state.pawns) == expected_pawns

        track_positions: list[int] = []
        home_steps: list[int] = []
        for pawn in state.pawns:
            assert pawn.zone in valid_zones
            if pawn.zone == "track":
                assert pawn.track_position is not None
                track_positions.append(pawn.track_position)
                assert pawn.home_steps == 0
            elif pawn.zone == "home_path":
                assert pawn.track_position is None
                assert 1 <= pawn.home_steps <= SAFETY_LENGTH
                home_steps.append(pawn.home_steps)
            elif pawn.zone == "home":
                assert pawn.track_position is None
                assert pawn.home_steps == SAFETY_LENGTH + 1
            else:
                assert pawn.zone == "start"
                assert pawn.track_position is None
                assert pawn.home_steps == 0

        # A player cannot stack their own pawns in track/home path.
        assert len(track_positions) == len(set(track_positions))
        assert len(home_steps) == len(set(home_steps))

        assert player.pawns_in_start == sum(1 for pawn in state.pawns if pawn.zone == "start")
        assert player.pawns_in_home == sum(1 for pawn in state.pawns if pawn.zone == "home")


def _run_bot_game(
    *,
    seed: int,
    auto_apply_single_move: bool,
    faster_setup_one_pawn_out: bool,
    max_ticks: int,
    rules_profile: str = "classic_00390",
    reload_every: int | None = None,
) -> tuple[SorryGame, int]:
    random.seed(seed)
    game = SorryGame(
        options=SorryOptions(
            rules_profile=rules_profile,
            auto_apply_single_move=auto_apply_single_move,
            faster_setup_one_pawn_out=faster_setup_one_pawn_out,
        )
    )

    bots = [Bot("Bot1"), Bot("Bot2")]
    for bot in bots:
        game.add_player(bot.username, bot)
    game.on_start()

    for tick in range(max_ticks):
        _assert_state_invariants(game)
        if game.status == "finished":
            return game, tick

        if reload_every and tick > 0 and tick % reload_every == 0:
            payload = game.to_json()
            game = SorryGame.from_json(payload)
            for bot in bots:
                game.attach_user(bot.uuid, bot)
            game.rebuild_runtime_state()
            for player in game.players:
                game.setup_player_actions(player)
            _assert_state_invariants(game)

        game.on_tick()

    return game, max_ticks


def test_two_bot_game_completes_from_fresh_start() -> None:
    """A two-bot Sorry game should complete from a fresh start."""
    game, ticks = _run_bot_game(
        seed=4242,
        auto_apply_single_move=False,
        faster_setup_one_pawn_out=False,
        max_ticks=4000,
    )
    assert game.status == "finished"
    assert game.game_active is False
    assert ticks < 4000


def test_two_bot_game_completes_with_save_reload_cycles() -> None:
    """Bot game should survive repeated save/load cycles and still complete."""
    game, ticks = _run_bot_game(
        seed=4343,
        auto_apply_single_move=True,
        faster_setup_one_pawn_out=True,
        max_ticks=4000,
        reload_every=25,
    )
    assert game.status == "finished"
    assert game.game_active is False
    assert ticks < 4000


def test_two_bot_game_completes_from_fresh_start_a5065_core() -> None:
    """A5065 core bot game should complete from a fresh start."""
    game, ticks = _run_bot_game(
        seed=4444,
        rules_profile="a5065_core",
        auto_apply_single_move=False,
        faster_setup_one_pawn_out=False,
        max_ticks=4000,
    )
    assert game.status == "finished"
    assert game.game_active is False
    assert ticks < 4000


def test_mixed_human_bot_table_progresses_cleanly() -> None:
    """Human + bot turn flow should stay stable in one table."""
    game = SorryGame(
        options=SorryOptions(
            auto_apply_single_move=True,
            faster_setup_one_pawn_out=False,
        )
    )
    human = MockUser("Alice")
    bot = Bot("Bot1")
    human_player = game.add_player("Alice", human)
    bot_player = game.add_player("Bot1", bot)
    game.on_start()

    assert game.current_player is not None
    assert game.current_player.id == human_player.id

    human_state = game.game_state.player_states[human_player.id]
    bot_state = game.game_state.player_states[bot_player.id]
    _set_track(human_state.pawns[0], 0)
    _set_track(bot_state.pawns[0], 30)
    for pawn in human_state.pawns[1:]:
        _set_home(pawn)
    for pawn in bot_state.pawns[1:]:
        _set_home(pawn)

    # Draw pile pops from the end: Alice gets 3, bot gets 5.
    game.game_state.draw_pile = ["5", "3"]

    # Human turns are not auto-driven on tick.
    game.on_tick()
    assert game.current_player is not None
    assert game.current_player.id == human_player.id
    assert game.game_state.turn_phase == "draw"
    assert game.game_state.current_card is None

    game.execute_action(human_player, "draw_card")
    assert human_state.pawns[0].track_position == 3
    assert game.current_player is not None
    assert game.current_player.id == bot_player.id
    assert game.game_state.turn_phase == "draw"
    assert game.game_state.current_card is None

    game.on_tick()
    # Bot lands on another color's slide start (35) and slides to 39 in classic.
    assert bot_state.pawns[0].track_position == 39
    assert game.current_player is not None
    assert game.current_player.id == human_player.id
    assert game.game_state.turn_phase == "draw"
    assert game.game_state.current_card is None
    assert game.status == "playing"
