import pytest

from server.game_utils.actions import Visibility
from server.game_utils.cards import Card, Deck, DeckFactory
from server.games.crazyeights.game import CrazyEightsGame, CrazyEightsOptions
from server.messages.localization import Localization
from server.core.users.bot import Bot
from server.core.users.test_user import MockUser


def create_game_with_host(host_name: str = "Host"):
    game = CrazyEightsGame()
    host_user = MockUser(host_name)
    host_player = game.add_player(host_name, host_user)
    game.host = host_name
    return game, host_player, host_user


def make_card(card_id: int, rank: int, suit: int) -> Card:
    return Card(id=card_id, rank=rank, suit=suit)


def test_crazyeights_game_creation():
    game = CrazyEightsGame()
    assert game.get_name() == "Crazy Eights"
    assert game.get_name_key() == "game-name-crazyeights"
    assert game.get_type() == "crazyeights"
    assert game.get_category() == "category-card-games"
    assert game.get_min_players() == 2
    assert game.get_max_players() == 8


def test_crazyeights_options_defaults():
    game = CrazyEightsGame()
    assert game.options.winning_score == 500
    assert game.options.turn_timer == "0"


def test_crazyeights_bot_game_completes():
    options = CrazyEightsOptions(winning_score=50)
    game = CrazyEightsGame(options=options)
    for i in range(2):
        bot = Bot(f"Bot{i}")
        game.add_player(f"Bot{i}", bot)
    game.on_start()

    for _ in range(40000):
        if game.status == "finished":
            break
        game.on_tick()

    assert game.status == "finished"


def test_crazyeights_add_bot_uses_available_name():
    game, host_player, host_user = create_game_with_host()
    host_user.clear_messages()

    game._action_add_bot(host_player, "", "add_bot")

    bots = [player for player in game.players if player.is_bot]
    assert bots and bots[0].name == "Alice"
    assert bots[0].id in game.player_action_sets
    assert "game_crazyeights/botsit.ogg" in host_user.get_sounds_played()


def test_crazyeights_add_bot_without_available_names_notifies_player(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("server.game_utils.lobby_actions_mixin.BOT_NAMES", ["Robo"])
    game, host_player, host_user = create_game_with_host()

    existing_bot = game.add_player("Robo", Bot("Robo"))
    host_user.clear_messages()
    existing_ids = {player.id for player in game.players}

    game._action_add_bot(host_player, "", "add_bot")

    assert {player.id for player in game.players} == existing_ids
    expected_warning = Localization.get(host_user.locale, "no-bot-names-available")
    assert host_user.get_last_spoken() == expected_warning
    assert existing_bot.id in game.player_action_sets


def test_crazyeights_remove_bot_plays_sound_and_cleans_up():
    game, host_player, host_user = create_game_with_host()
    game.add_player("Bot1", Bot("Bot1"))
    bot2 = game.add_player("Bot2", Bot("Bot2"))
    host_user.clear_messages()

    game._action_remove_bot(host_player, "remove_bot")

    assert bot2 not in game.players
    assert bot2.id not in game.player_action_sets
    assert bot2.id not in game._users
    assert "game_crazyeights/botleave.ogg" in host_user.get_sounds_played()


def test_crazyeights_perform_leave_game_replaces_human_with_bot_when_playing():
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    host_user.clear_messages()
    guest_user.clear_messages()

    game._perform_leave_game(host_player)

    assert host_player in game.players
    assert host_player.is_bot
    replacement_user = game.get_user(host_player)
    assert isinstance(replacement_user, Bot)
    assert replacement_user.uuid == host_player.id
    assert "game_crazyeights/personleave.ogg" in guest_user.get_sounds_played()
    assert not game._destroyed
    assert guest_player in game.players


def test_crazyeights_perform_leave_game_reassigns_host_when_waiting():
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "waiting"
    game.host = host_player.name
    host_user.clear_messages()
    guest_user.clear_messages()

    game._perform_leave_game(host_player)

    assert host_player not in game.players
    assert game.host == guest_player.name
    expected_host_message = Localization.get(guest_user.locale, "new-host", player=guest_player.name)
    assert expected_host_message in guest_user.get_spoken_messages()
    assert "game_crazyeights/personleave.ogg" in guest_user.get_sounds_played()
    assert not game._destroyed


def test_crazyeights_choose_suit_transitions_wild_state():
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player])
    game.awaiting_wild_suit = True
    game.pending_round_winner_id = host_player.id
    host_user.clear_messages()
    guest_user.clear_messages()
    game.timer.start(30)

    game._action_choose_suit(host_player, "suit_hearts")

    assert game.current_suit == 3
    assert not game.awaiting_wild_suit
    assert game.wild_wait_ticks == 15
    assert game.wild_wait_player_id == host_player.id
    assert game.wild_end_round_pending
    assert game.timer.seconds_remaining() == 0
    assert "game_crazyeights/morf.ogg" in host_user.get_sounds_played()
    expected_suit_message = Localization.get(
        guest_user.locale,
        "crazyeights-suit-chosen",
        suit=game._suit_name(3, guest_user.locale),
    )
    assert expected_suit_message in guest_user.get_spoken_messages()


def test_crazyeights_start_new_hand_uses_number_start_card(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)

    class FixedDeck(Deck):
        def shuffle(self) -> None:  # deterministic order
            return

    cards = [
        make_card(i, rank, suit)
        for i, (rank, suit) in enumerate(
            [
                (2, 1),
                (3, 2),
                (4, 3),
                (5, 4),
                (6, 1),
                (7, 2),
                (9, 3),
                (10, 4),
                (2, 2),
                (3, 3),
                (8, 1),   # first start candidate (wild)
                (5, 2),   # actual start card
                (6, 3),
            ]
        )
    ]
    test_deck = FixedDeck(cards=list(cards))
    card_lookup = {card.id: card for card in cards}
    monkeypatch.setattr(DeckFactory, "standard_deck", lambda num_decks=1: (test_deck, card_lookup))

    game._start_new_hand()

    assert len(host_player.hand) == 5
    assert len(guest_player.hand) == 5
    assert game.round == 1
    assert game.dealer_index == 0
    assert game.turn_index == 1  # next player after dealer
    assert game.discard_pile
    start_card = game.discard_pile[-1]
    assert start_card.rank == 5 and start_card.suit == 2
    assert game.current_suit == 2


def test_crazyeights_timer_warning_plays_once():
    game, host_player, host_user = create_game_with_host()
    game.status = "playing"
    game.options.turn_timer = "20"
    game.timer.ticks_remaining = 100  # 5 seconds remaining
    host_user.clear_messages()

    game._maybe_play_timer_warning()

    sounds = host_user.get_sounds_played()
    assert "game_crazyeights/fivesec.ogg" in sounds
    count = sounds.count("game_crazyeights/fivesec.ogg")

    game._maybe_play_timer_warning()

    assert host_user.get_sounds_played().count("game_crazyeights/fivesec.ogg") == count
    assert game.timer_warning_played


def test_crazyeights_handle_turn_timeout_executes_bot_action(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    game.status = "playing"
    game.set_turn_players([host_player], reset_index=True)

    monkeypatch.setattr("server.games.crazyeights.game.bot_think", lambda g, p: "draw")
    executed: list[tuple[object, str]] = []

    def fake_execute_action(player, action_id):
        executed.append((player, action_id))

    monkeypatch.setattr(game, "execute_action", fake_execute_action)
    host_user.clear_messages()

    game._handle_turn_timeout()

    assert executed == [(host_player, "draw")]
    assert "game_crazyeights/expired.ogg" in host_user.get_sounds_played()


def test_crazyeights_action_draw_triggers_new_hand_when_deck_empty(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)
    host_player.hand = []
    game.discard_pile = []
    game.deck = Deck(cards=[])

    new_hand_called = {"count": 0}

    def fake_start_new_hand():
        new_hand_called["count"] += 1

    monkeypatch.setattr(game, "_start_new_hand", fake_start_new_hand)

    game._action_draw(host_player, "draw")

    assert new_hand_called["count"] == 1


def test_crazyeights_action_pass_requires_draw(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)
    game.turn_has_drawn = True
    game.turn_drawn_card = make_card(200, 7, 1)

    advance_called = {"count": 0}

    def fake_advance_turn():
        advance_called["count"] += 1

    monkeypatch.setattr(game, "_advance_turn", fake_advance_turn)
    host_user.clear_messages()

    game._action_pass(host_player, "pass")

    assert advance_called["count"] == 1
    assert not game.turn_has_drawn
    assert game.turn_drawn_card is None
    assert "game_crazyeights/pass.ogg" in host_user.get_sounds_played()


def test_crazyeights_apply_card_effects(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.set_turn_players([host_player, guest_player], reset_index=True)
    game.turn_index = 0

    skip_card = make_card(300, 12, 1)
    game._apply_card_effects(skip_card)
    assert game.turn_skip_count == 1

    game.turn_skip_count = 0
    reverse_card = make_card(301, 11, 1)
    game._apply_card_effects(reverse_card)
    assert game.turn_skip_count == 1

    skip_calls: list[int] = []
    draw_calls: list[tuple[object, int]] = []

    def fake_skip(count=1):
        skip_calls.append(count)

    def fake_draw_for_player(player, count):
        draw_calls.append((player, count))

    monkeypatch.setattr(game, "skip_next_players", fake_skip)
    monkeypatch.setattr(game, "_draw_for_player", fake_draw_for_player)
    draw_two_card = make_card(302, 13, 4)
    game._apply_card_effects(draw_two_card)

    assert skip_calls == [1]
    assert draw_calls == [(guest_player, 2)]


def test_crazyeights_end_round_scores_and_resets(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    bot = Bot("Bot")
    bot_player = game.add_player("Bot", bot)
    game.status = "playing"

    guest_player.hand = [make_card(400, 8, 1), make_card(401, 5, 2)]
    bot_player.hand = [make_card(402, 11, 3), make_card(403, 2, 4)]
    host_player.hand = []

    game._end_round(host_player, last_card=None)

    assert host_player.score == 77
    assert guest_player.hand == []
    assert bot_player.hand == []
    assert game.hand_wait_ticks == 100
    assert game.discard_pile == []
    assert game.turn_player_ids == []

    assert "game_crazyeights/youwin.ogg" in host_user.get_sounds_played()
    assert "game_crazyeights/loser.ogg" in guest_user.get_sounds_played()


def test_crazyeights_end_round_triggers_game_end():
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.options.winning_score = 100

    guest_player.hand = [make_card(500, 12, 1)]
    host_player.hand = []
    host_player.score = 90

    game._end_round(host_player, last_card=None)

    assert game.status == "finished"
    assert not game.game_active
    expected = Localization.get(host_user.locale, "crazyeights-you-win-game", score=host_player.score)
    assert host_user.get_spoken_messages()[-1] == expected


def test_crazyeights_build_result_and_end_screen():
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    host_player.score = 120
    guest_player.score = 80
    game.sound_scheduler_tick = 25

    result = game.build_game_result()

    assert result.custom_data["winner_name"] == host_player.name
    assert result.custom_data["final_scores"][host_player.name] == 120
    assert result.duration_ticks == 25

    lines = game.format_end_screen(result, host_user.locale)
    assert lines[0] == Localization.get(host_user.locale, "game-final-scores")
    assert any(f"{host_player.name}: 120" in line for line in lines)


def test_crazyeights_turn_loop_controls_ambience():
    game, host_player, host_user = create_game_with_host()
    host_user.clear_messages()

    game._start_turn_loop(host_player)
    assert ("play_ambience", {"loop": "game_crazyeights/yourturn.ogg", "intro": "", "outro": ""}) in [
        (m.type, m.data) for m in host_user.messages
    ]

    game._stop_turn_loop()
    assert ("stop_ambience", {}) in [(m.type, m.data) for m in host_user.messages]
    assert game._turn_sound_player_id is None


def test_crazyeights_on_player_skipped_announces_to_player():
    game, host_player, host_user = create_game_with_host()
    host_user.clear_messages()

    game.on_player_skipped(host_player)

    expected = Localization.get(host_user.locale, "crazyeights-you-are-skipped", player=host_player.name)
    assert expected in host_user.get_spoken_messages()


def test_crazyeights_perform_leave_game_last_human_destroys_playing(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    game.add_player("Bot", Bot("Bot"))
    game.status = "playing"

    destroyed = {"called": 0}

    monkeypatch.setattr(game, "destroy", lambda: destroyed.__setitem__("called", destroyed["called"] + 1))

    game._perform_leave_game(host_player)

    assert destroyed["called"] == 1
    assert all(player.is_bot for player in game.players)


def test_crazyeights_perform_leave_game_last_human_destroys_waiting(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    game.status = "waiting"

    destroyed = {"called": 0}

    monkeypatch.setattr(game, "destroy", lambda: destroyed.__setitem__("called", destroyed["called"] + 1))

    game._perform_leave_game(host_player)

    assert destroyed["called"] == 1
    assert host_player not in game.players


def test_crazyeights_setup_keybinds_registers_expected_keys():
    game = CrazyEightsGame()
    game.setup_keybinds()

    assert "space" in game._keybinds
    assert any("draw" in bind.actions for bind in game._keybinds["space"])
    assert "c" in game._keybinds
    c_actions = game._keybinds["c"]
    assert any(bind.actions == ["read_top"] and bind.include_spectators for bind in c_actions)
    assert any(bind.actions == ["suit_clubs"] and not bind.include_spectators for bind in c_actions)
    read_counts_bind = [
        bind for bind in game._keybinds["e"] if "read_counts" in bind.actions
    ]
    assert read_counts_bind and read_counts_bind[0].include_spectators


def test_crazyeights_sync_turn_actions_orders_cards_and_draw_pass():
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    spectator = game.add_spectator("Spectator", MockUser("Spectator"))

    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)

    card_a = make_card(10, 9, 2)
    card_b = make_card(11, 7, 4)
    wild_card = make_card(12, 8, 3)
    host_player.hand = [card_b, card_a, wild_card]

    turn_set = game.get_action_set(host_player, "turn")
    assert turn_set is not None

    game._sync_turn_actions(host_player)
    play_actions = [aid for aid in turn_set._order if aid.startswith("play_card_")]
    assert play_actions[0] == f"play_card_{card_a.id}"
    assert play_actions[-1] == f"play_card_{wild_card.id}"
    assert "draw" in turn_set._order
    assert "pass" in turn_set._order

    # Spectator should short-circuit without errors
    game._sync_turn_actions(spectator)


def test_crazyeights_on_tick_wild_wait_ends_round(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.game_active = True
    game.set_turn_players([host_player, guest_player], reset_index=True)

    game.wild_wait_ticks = 1
    game.wild_wait_player_id = host_player.id
    game.pending_round_winner_id = host_player.id
    game.wild_end_round_pending = True

    called = {"end_round": 0}

    def fake_end_round(player, last_card=None):
        called["end_round"] += 1

    monkeypatch.setattr(game, "_end_round", fake_end_round)

    game.on_tick()

    assert called["end_round"] == 1
    assert game.wild_wait_player_id is None
    assert not game.wild_end_round_pending


def test_crazyeights_on_tick_timer_timeout(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.game_active = True
    game.set_turn_players([host_player, guest_player], reset_index=True)

    game.timer.ticks_remaining = 1
    executed: list[tuple[object, str]] = []

    monkeypatch.setattr(game, "_handle_turn_timeout", lambda: executed.append(("timeout", "handled")))

    game.on_tick()

    assert ("timeout", "handled") in executed


def test_crazyeights_action_play_card_wild_sets_state(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players(game.players[:2], reset_index=True)

    wild_card = make_card(200, 8, 1)
    other_card = make_card(201, 5, 2)
    host_player.hand = [wild_card, other_card]

    monkeypatch.setattr("random.randint", lambda a, b: a)

    game._action_play_card(host_player, f"play_card_{wild_card.id}")

    assert game.awaiting_wild_suit
    assert game.turn_has_drawn is False
    assert game.turn_drawn_card is None
    assert game.wild_wait_ticks == 0


def test_crazyeights_action_play_card_draw_two_finishes(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)

    draw_two = make_card(210, 13, 3)
    host_player.hand = [draw_two]

    drawn_for_next: list[int] = []
    end_round_calls = {"count": 0}

    monkeypatch.setattr(game, "_draw_for_player", lambda player, count: drawn_for_next.append(count))
    monkeypatch.setattr(game, "_end_round", lambda player, last_card=None: end_round_calls.__setitem__("count", end_round_calls["count"] + 1))

    game._action_play_card(host_player, f"play_card_{draw_two.id}")

    assert drawn_for_next == [2]
    assert end_round_calls["count"] == 1


def test_crazyeights_action_play_card_regular_advances(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)

    card = make_card(220, 7, 3)
    remaining_card = make_card(221, 4, 1)
    host_player.hand = [card, remaining_card]

    advance_calls = {"count": 0}
    monkeypatch.setattr(game, "_advance_turn", lambda: advance_calls.__setitem__("count", advance_calls["count"] + 1))
    monkeypatch.setattr(game, "_apply_card_effects", lambda card: None)

    game._action_play_card(host_player, f"play_card_{card.id}")

    assert advance_calls["count"] == 1


def test_crazyeights_action_draw_playable_card_sounds(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)

    playable_card = make_card(230, 5, 2)
    game.deck = Deck(cards=[playable_card])
    game.discard_pile = [make_card(5000, 5, 3)]
    host_player.hand = []

    monkeypatch.setattr("random.randint", lambda a, b: a)

    game._action_draw(host_player, "draw")

    assert game.turn_has_drawn
    assert host_player.hand[-1] == playable_card
    assert "game_crazyeights/drawPlayable.ogg" in host_user.get_sounds_played()
    assert "game_crazyeights/draw.ogg" in guest_user.get_sounds_played()


def test_crazyeights_action_read_counts_and_timer_messages():
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)
    host_user.clear_messages()

    host_player.hand = [make_card(240, 3, 1)]
    guest_player.hand = [make_card(241, 4, 2), make_card(242, 8, 3)]
    game.deck = Deck(cards=[make_card(243, 5, 4)])

    game._action_read_counts(host_player, "read_counts")

    counts_message = host_user.get_last_spoken()
    assert host_player.name in counts_message and guest_player.name in counts_message

    game.timer.start(10)
    game._action_check_turn_timer(host_player, "check_turn_timer")
    assert host_user.get_last_spoken() == Localization.get(host_user.locale, "poker-timer-remaining", seconds=10)

    game.timer.clear()
    game._action_check_turn_timer(host_player, "check_turn_timer")
    assert host_user.get_last_spoken() == Localization.get(host_user.locale, "poker-timer-disabled")


def test_crazyeights_visibility_helpers_cover_branches():
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    spectator = game.add_spectator("Spectator", MockUser("Spectator"))

    assert game._is_turn_action_enabled(host_player) == "action-not-playing"

    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)

    assert game._is_turn_action_enabled(guest_player) == "action-not-your-turn"
    assert game._is_turn_action_enabled(spectator) == "action-spectator"
    assert game._require_active_player(guest_player) is None
    assert game._require_active_player(host_player) == host_player

    game.awaiting_wild_suit = True
    assert game._is_draw_enabled(host_player) == "action-not-available"
    assert game._is_pass_enabled(host_player) == "action-not-available"
    assert game._is_suit_choice_hidden(host_player) == Visibility.VISIBLE

    game.awaiting_wild_suit = False
    host_player.hand = [make_card(250, 7, 2)]
    game.current_suit = 3
    game.discard_pile = [make_card(9999, 5, 3)]
    assert game._has_playable_cards(host_player) is False
    assert game._is_draw_enabled(host_player) is None
    assert game._is_draw_hidden(host_player) == Visibility.VISIBLE

    game.turn_has_drawn = True
    assert game._is_pass_enabled(host_player) is None
    assert game._is_pass_hidden(host_player) == Visibility.VISIBLE
    game.turn_has_drawn = False

    game.max_hand_size = 1
    host_player.hand = [make_card(251, 4, 1)]
    assert game._is_pass_enabled(host_player) is None
    assert game._is_pass_hidden(host_player) == Visibility.VISIBLE

    game.turn_has_drawn = True
    assert game._can_draw(host_player) is False
    assert game._is_always_hidden(host_player) == Visibility.HIDDEN


def test_crazyeights_card_helper_methods(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    guest_user = MockUser("Guest")
    guest_player = game.add_player("Guest", guest_user)
    game.status = "playing"
    game.set_turn_players([host_player, guest_player], reset_index=True)

    card_number = make_card(260, 6, 1)
    card_wild = make_card(261, 8, 2)
    card_reverse = make_card(262, 11, 3)

    assert game._is_number_card(card_number)
    assert not game._is_number_card(card_wild)

    game.discard_pile = [make_card(4000, 6, 4)]
    assert game._is_card_playable(card_number)
    game.current_suit = 2
    assert game._is_card_playable(make_card(270, 3, 2))
    game.current_suit = None
    assert game._is_card_playable(make_card(271, 6, 1))
    game.discard_pile = [make_card(4001, 8, 1)]
    game.awaiting_wild_suit = True
    assert not game._is_card_playable(card_number)
    game.awaiting_wild_suit = False
    assert game._is_card_playable(card_wild)

    host_player.hand = [card_number, card_reverse]
    game.discard_pile = [make_card(4002, 8, 1)]
    game.current_suit = 1
    playable_indices = game.get_playable_indices(host_player)
    assert playable_indices == [0]

    game.discard_pile = [make_card(5001, 5, 1), make_card(5002, 4, 2)]
    game.deck = Deck(cards=[])
    monkeypatch.setattr(game.deck, "is_empty", lambda: True)
    monkeypatch.setattr(game.deck, "draw_one", lambda: None)
    play_sounds = []
    monkeypatch.setattr(game, "play_sound", lambda sound, volume=100, pan=0, pitch=100: play_sounds.append(sound))
    game._reshuffle_discard_into_deck()
    assert "game_crazyeights/pileempty.ogg" in play_sounds

    sounds = []
    monkeypatch.setattr(game, "play_sound", lambda sound, volume=100, pan=0, pitch=100: sounds.append(sound))
    game._play_card_sound(card_wild)
    game._play_card_sound(make_card(263, 13, 1))
    game._play_card_sound(make_card(264, 12, 1))
    game._play_card_sound(make_card(265, 11, 1))
    game._play_card_sound(make_card(266, 5, 1))
    assert set(sounds) == {
        "game_crazyeights/discwild.ogg",
        "game_crazyeights/discdraw.ogg",
        "game_crazyeights/discskip.ogg",
        "game_crazyeights/discrev.ogg",
        "game_crazyeights/discarded.ogg",
    }


def test_crazyeights_draw_card_reshuffle(monkeypatch: pytest.MonkeyPatch):
    game, host_player, host_user = create_game_with_host()
    card_top = make_card(280, 7, 1)
    recycle = [make_card(281, 9, 2), make_card(282, 3, 3)]
    game.discard_pile = recycle + [card_top]
    game.deck = Deck(cards=[])

    shuffled = {"called": False}

    def fake_shuffle():
        shuffled["called"] = True

    monkeypatch.setattr(game.deck, "shuffle", fake_shuffle)

    drawn = game._draw_card()

    assert shuffled["called"]
    assert drawn is not None
    assert game.discard_pile[-1] == card_top
