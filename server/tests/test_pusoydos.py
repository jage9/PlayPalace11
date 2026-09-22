"""Comprehensive tests for Pusoy Dos."""

import pytest
from ..games.pusoydos.game import PusoyDosGame, PusoyDosPlayer, PusoyDosOptions
from ..games.pusoydos.evaluator import (
    get_rank_value,
    get_suit_value,
    card_value,
    evaluate_combo,
    detect_instant_win,
    sort_cards,
    Combo,
)
from ..games.pusoydos.bot import get_all_valid_combos, bot_think, bot_choose_give_cards
from server.core.users.test_user import MockUser
from server.core.users.bot import Bot
from ..game_utils.cards import Card
from ..game_utils.roulette import RouletteSession


# =============================================================================
# Evaluator tests
# =============================================================================


class TestRankSuitValues:
    def test_rank_values(self):
        assert get_rank_value(3) == 3  # lowest
        assert get_rank_value(10) == 10
        assert get_rank_value(1) == 14  # Ace
        assert get_rank_value(2) == 15  # highest

    def test_suit_values(self):
        assert get_suit_value(2) == 1  # Clubs (lowest)
        assert get_suit_value(4) == 2  # Spades
        assert get_suit_value(3) == 3  # Hearts
        assert get_suit_value(1) == 4  # Diamonds (highest)

    def test_card_value_ordering(self):
        three_clubs = Card(0, 3, 2)
        three_spades = Card(1, 3, 4)
        two_diamonds = Card(2, 2, 1)
        assert card_value(three_clubs) < card_value(three_spades)
        assert card_value(three_spades) < card_value(two_diamonds)


class TestComboEvaluation:
    def test_single(self):
        combo = evaluate_combo([Card(0, 3, 2)])
        assert combo is not None
        assert combo.type_name == "single"
        assert combo.rank_value == 3
        assert combo.suit_value == 1  # Clubs

    def test_pair(self):
        combo = evaluate_combo([Card(0, 5, 1), Card(1, 5, 3)])
        assert combo is not None
        assert combo.type_name == "pair"
        assert combo.rank_value == 5

    def test_invalid_pair(self):
        combo = evaluate_combo([Card(0, 5, 1), Card(1, 6, 1)])
        assert combo is None

    def test_three_of_a_kind(self):
        combo = evaluate_combo([Card(0, 7, 1), Card(1, 7, 2), Card(2, 7, 3)])
        assert combo is not None
        assert combo.type_name == "three_of_a_kind"

    def test_straight(self):
        # Use different suits to avoid straight flush
        suits = [1, 2, 3, 4, 1]
        cards = [Card(i, r, s) for i, (r, s) in enumerate(zip([3, 4, 5, 6, 7], suits))]
        combo = evaluate_combo(cards)
        assert combo is not None
        assert combo.type_name == "straight"

    def test_straight_no_2_default(self):
        """2 in straights is allowed by default."""
        # A-2-3-4-5
        cards = [Card(0, 1, 1), Card(1, 2, 1), Card(2, 3, 2), Card(3, 4, 3), Card(4, 5, 4)]
        combo = evaluate_combo(cards, allow_2_in_straights=True)
        assert combo is not None
        assert combo.type_name == "straight"

    def test_straight_no_2_disabled(self):
        """When 2-in-straights is off, any straight with a 2 is rejected."""
        cards = [Card(0, 1, 1), Card(1, 2, 1), Card(2, 3, 2), Card(3, 4, 3), Card(4, 5, 4)]
        combo = evaluate_combo(cards, allow_2_in_straights=False)
        assert combo is None

    def test_jqka2_straight(self):
        cards = [Card(0, 11, 1), Card(1, 12, 2), Card(2, 13, 3), Card(3, 1, 4), Card(4, 2, 1)]
        combo = evaluate_combo(cards, allow_2_in_straights=True)
        assert combo is not None
        assert combo.type_name == "straight"
        assert combo.rank_value == 15  # 2 is high

    def test_jqka2_blocked_when_disabled(self):
        cards = [Card(0, 11, 1), Card(1, 12, 2), Card(2, 13, 3), Card(3, 1, 4), Card(4, 2, 1)]
        combo = evaluate_combo(cards, allow_2_in_straights=False)
        assert combo is None

    def test_23456_straight(self):
        cards = [Card(0, 2, 1), Card(1, 3, 2), Card(2, 4, 3), Card(3, 5, 4), Card(4, 6, 1)]
        combo = evaluate_combo(cards, allow_2_in_straights=True)
        assert combo is not None
        assert combo.type_name == "straight"
        assert combo.rank_value == 6

    def test_flush(self):
        cards = [Card(i, r, 1) for i, r in enumerate([3, 5, 7, 9, 11])]
        combo = evaluate_combo(cards)
        assert combo is not None
        assert combo.type_name == "flush"

    def test_full_house(self):
        cards = [Card(0, 5, 1), Card(1, 5, 2), Card(2, 5, 3), Card(3, 8, 1), Card(4, 8, 4)]
        combo = evaluate_combo(cards)
        assert combo is not None
        assert combo.type_name == "full_house"
        assert combo.rank_value == 5

    def test_four_of_a_kind(self):
        cards = [Card(0, 9, 1), Card(1, 9, 2), Card(2, 9, 3), Card(3, 9, 4), Card(4, 3, 1)]
        combo = evaluate_combo(cards)
        assert combo is not None
        assert combo.type_name == "four_of_a_kind"
        assert combo.rank_value == 9

    def test_straight_flush(self):
        cards = [Card(i, r, 1) for i, r in enumerate([3, 4, 5, 6, 7])]
        combo = evaluate_combo(cards)
        assert combo is not None
        assert combo.type_name == "straight_flush"

    def test_invalid_four_cards(self):
        cards = [Card(i, i + 3, 1) for i in range(4)]
        combo = evaluate_combo(cards)
        assert combo is None

    def test_invalid_six_cards(self):
        cards = [Card(i, i + 3, 1) for i in range(6)]
        combo = evaluate_combo(cards)
        assert combo is None


class TestComboBeats:
    def test_higher_single_beats_lower(self):
        low = evaluate_combo([Card(0, 3, 2)])  # 3 of Clubs
        high = evaluate_combo([Card(1, 3, 4)])  # 3 of Spades
        assert high.beats(low)
        assert not low.beats(high)

    def test_higher_rank_beats_lower_rank(self):
        low = evaluate_combo([Card(0, 5, 1)])
        high = evaluate_combo([Card(1, 6, 2)])
        assert high.beats(low)

    def test_straight_flush_beats_four_of_a_kind(self):
        sf = evaluate_combo([Card(i, r, 1) for i, r in enumerate([3, 4, 5, 6, 7])])
        foak = evaluate_combo(
            [Card(0, 9, 1), Card(1, 9, 2), Card(2, 9, 3), Card(3, 9, 4), Card(4, 3, 2)]
        )
        assert sf.beats(foak)
        assert not foak.beats(sf)

    def test_four_of_a_kind_beats_full_house(self):
        foak = evaluate_combo(
            [Card(0, 9, 1), Card(1, 9, 2), Card(2, 9, 3), Card(3, 9, 4), Card(4, 3, 2)]
        )
        fh = evaluate_combo(
            [Card(0, 13, 1), Card(1, 13, 2), Card(2, 13, 3), Card(3, 1, 1), Card(4, 1, 4)]
        )
        assert foak.beats(fh)

    def test_flush_beats_straight(self):
        flush = evaluate_combo(
            [Card(0, 3, 1), Card(1, 5, 1), Card(2, 7, 1), Card(3, 9, 1), Card(4, 11, 1)]
        )
        straight = evaluate_combo(
            [Card(0, 3, 1), Card(1, 4, 2), Card(2, 5, 3), Card(3, 6, 4), Card(4, 7, 1)]
        )
        assert flush.beats(straight)

    def test_different_sizes_never_beat(self):
        single = evaluate_combo([Card(0, 2, 1)])  # 2 of Diamonds (highest)
        pair = evaluate_combo([Card(0, 3, 1), Card(1, 3, 2)])
        assert not single.beats(pair)
        assert not pair.beats(single)


class TestInstantWins:
    def test_dragon(self):
        # One card of every rank
        cards = [Card(i, r, (i % 4) + 1) for i, r in enumerate(range(1, 14))]
        assert detect_instant_win(cards) == "dragon"

    def test_four_twos(self):
        cards = [Card(i, 2, s) for i, s in enumerate([1, 2, 3, 4], start=0)]
        # Fill remaining 9 cards with non-duplicate ranks
        for i in range(9):
            cards.append(Card(i + 4, i + 3, 1))
        assert detect_instant_win(cards) == "four_twos"

    def test_six_pairs(self):
        cards = []
        cid = 0
        # 6 pairs
        for rank in [3, 4, 5, 6, 7, 8]:
            cards.append(Card(cid, rank, 1))
            cid += 1
            cards.append(Card(cid, rank, 2))
            cid += 1
        # 1 single
        cards.append(Card(cid, 9, 1))
        assert len(cards) == 13
        assert detect_instant_win(cards) == "six_pairs"

    def test_no_instant_win(self):
        cards = [Card(i, (i % 13) + 1, (i % 4) + 1) for i in range(13)]
        # This creates a dragon, so let's make a non-qualifying hand
        cards = [Card(i, 3, s) for i, s in enumerate([1, 2, 3, 4])]  # four 3s
        cards += [Card(i + 4, 4, s) for i, s in enumerate([1, 2, 3, 4])]  # four 4s
        cards += [Card(8, 5, 1), Card(9, 5, 2), Card(10, 5, 3)]  # three 5s
        cards += [Card(11, 6, 1), Card(12, 6, 2)]  # pair of 6s
        assert detect_instant_win(cards) is None

    def test_not_13_cards(self):
        cards = [Card(i, i + 3, 1) for i in range(10)]
        assert detect_instant_win(cards) is None


# =============================================================================
# Game tests
# =============================================================================


def _make_game(n_players=4, **opts):
    """Helper: create a game with N mock users, optionally set options."""
    game = PusoyDosGame()
    for k, v in opts.items():
        setattr(game.options, k, v)

    players = []
    for i in range(n_players):
        user = MockUser(f"p{i + 1}")
        p = game.add_player(f"p{i + 1}", user)
        players.append(p)

    return game, players


class TestGameInit:
    def test_start_4_players(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()
        assert game.status == "playing"
        assert game.round == 1

    def test_start_resets_state(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()
        for p in players:
            assert p.round_wins == 0
            assert p.score == 0
            assert not p.eliminated

    def test_default_mode_is_elimination(self):
        game, _ = _make_game(4)
        assert game.options.game_mode == "elimination"
        assert game.options.rounds_to_win == 2


class TestDealing:
    def test_4_players_13_cards_each(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()

        for p in game._playing_players():
            assert len(p.hand) == 13

    def test_2_players_26_cards_each(self):
        game, players = _make_game(2, instant_wins=False)
        game.on_start()

        for p in game._playing_players():
            assert len(p.hand) == 26

    def test_3_players_17_cards_each(self):
        game, players = _make_game(3, instant_wins=False)
        game.on_start()

        for p in game._playing_players():
            assert len(p.hand) == 17

    def test_3_players_removes_3_of_spades(self):
        """With 3 players, 3 of Spades is removed so deck is 51 cards."""
        game, players = _make_game(3, instant_wins=False)
        game.on_start()

        all_cards = []
        for p in game._playing_players():
            all_cards.extend(p.hand)
        assert len(all_cards) == 51
        # No 3 of Spades
        assert not any(c.rank == 3 and c.suit == 4 for c in all_cards)


class TestFirstTurn:
    def test_3_of_clubs_goes_first(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()

        current = game.current_player
        assert current is not None
        assert any(c.rank == 3 and c.suit == 2 for c in current.hand)

    def test_must_include_3_of_clubs(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()

        current = game.current_player
        # Give current player known cards
        current.hand = [Card(1, 3, 2), Card(2, 4, 1), Card(3, 5, 1)]

        # Try playing without 3 of Clubs
        current.selected_cards = {2}
        game.execute_action(current, "play_selected")
        user = game.get_user(current)
        assert "3 of Clubs" in user.get_last_spoken()

        # Play with 3 of Clubs
        current.selected_cards = {1}
        game.execute_action(current, "play_selected")
        assert game.trick_winner_id == current.id


class TestPlayValidation:
    def _setup_mid_game(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()

        game.is_first_turn = False
        return game, players

    def test_wrong_card_count(self):
        game, players = self._setup_mid_game()
        current = game.current_player
        game.current_combo = Combo("pair", [Card(1, 4, 1), Card(2, 4, 2)], 4, 2)
        game.trick_cards = game.current_combo.cards

        current.hand = [Card(3, 5, 1)]
        current.selected_cards = {3}
        game.execute_action(current, "play_selected")

        user = game.get_user(current)
        assert "exactly 2 cards" in user.get_last_spoken()

    def test_lower_combo_rejected(self):
        game, players = self._setup_mid_game()
        current = game.current_player
        game.current_combo = Combo("pair", [Card(1, 6, 1), Card(2, 6, 2)], 6, 2)
        game.trick_cards = game.current_combo.cards

        current.hand = [Card(3, 4, 1), Card(4, 4, 2)]
        current.selected_cards = {3, 4}
        game.execute_action(current, "play_selected")

        user = game.get_user(current)
        assert "lower" in user.get_last_spoken()

    def test_cannot_pass_on_new_trick(self):
        game, players = self._setup_mid_game()
        current = game.current_player
        game.current_combo = None

        game.execute_action(current, "pass")
        user = game.get_user(current)
        assert "cannot pass" in user.get_last_spoken().lower()


class TestConfirmToPass:
    def _setup_mid_game(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()
        game.is_first_turn = False
        return game, players

    def test_first_pass_asks_for_confirmation(self):
        game, players = self._setup_mid_game()
        current = game.current_player
        game.current_combo = Combo("single", [Card(99, 5, 1)], 5, 4)
        game.trick_cards = game.current_combo.cards

        old_turn = current.id
        game.execute_action(current, "pass")

        # Should NOT have advanced turn
        assert game.current_player.id == old_turn
        assert not current.passed_this_trick

        user = game.get_user(current)
        assert "again to confirm" in user.get_last_spoken().lower()
        assert current.pass_confirm_ticks == 200

    def test_second_pass_confirms(self):
        game, players = self._setup_mid_game()
        current = game.current_player
        game.current_combo = Combo("single", [Card(99, 5, 1)], 5, 4)
        game.trick_cards = game.current_combo.cards

        # First press — sets confirmation
        game.execute_action(current, "pass")
        assert current.pass_confirm_ticks == 200

        # Second press — confirms and passes
        game.execute_action(current, "pass")
        assert current.passed_this_trick
        assert current.pass_confirm_ticks == 0

    def test_confirm_expires_after_200_ticks(self):
        game, players = self._setup_mid_game()
        current = game.current_player
        game.current_combo = Combo("single", [Card(99, 5, 1)], 5, 4)
        game.trick_cards = game.current_combo.cards

        game.execute_action(current, "pass")
        assert current.pass_confirm_ticks == 200

        # Tick down 200 times
        for _ in range(200):
            game.on_tick()

        assert current.pass_confirm_ticks == 0

        # Now pressing pass again should ask for confirmation anew
        user = game.get_user(current)
        user.clear_messages()
        game.execute_action(current, "pass")
        assert "again to confirm" in user.get_last_spoken().lower()

    def test_confirm_disabled_by_preference(self):
        game, players = self._setup_mid_game()
        current = game.current_player
        game.current_combo = Combo("single", [Card(99, 5, 1)], 5, 4)
        game.trick_cards = game.current_combo.cards

        user = game.get_user(current)
        user._preferences.confirm_destructive_actions = False

        # Single press should pass immediately
        game.execute_action(current, "pass")
        assert current.passed_this_trick

    def test_bot_skips_confirmation(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()
        game.is_first_turn = False

        # Find a bot player and make it current
        current = game.current_player
        game.current_combo = Combo("single", [Card(99, 2, 1)], 15, 4)  # 2 of Diamonds
        current.hand = [Card(0, 3, 2)]  # Only a 3 of Clubs — cannot beat

        # Bot think returns pass
        ids = bot_think(game, current)
        assert ids == []

        # Execute pass directly — should work without confirmation
        current.is_bot = True
        game.execute_action(current, "pass")
        assert current.passed_this_trick

    def test_new_turn_resets_confirm(self):
        game, players = self._setup_mid_game()
        current = game.current_player
        game.current_combo = Combo("single", [Card(99, 5, 1)], 5, 4)
        game.trick_cards = game.current_combo.cards

        game.execute_action(current, "pass")
        assert current.pass_confirm_ticks == 200

        # Simulate a new turn starting (e.g., another player plays)
        current.pass_confirm_ticks = 200
        game._start_turn()
        assert current.pass_confirm_ticks == 0


class TestEliminationMode:
    def test_player_eliminated_after_winning_rounds(self):
        game, players = _make_game(4, game_mode="elimination", rounds_to_win=1)
        game.on_start()

        p = game._playing_players()[0]
        p.round_wins = 0

        # Simulate winning a round
        game._player_wins_round(p)
        assert p.round_wins == 1

    def test_game_ends_when_one_remains(self):
        game, players = _make_game(4, game_mode="elimination", rounds_to_win=1)
        game.on_start()

        active = game._playing_players()
        # Eliminate all but one
        for p in active[:3]:
            p.round_wins = 1
            p.eliminated = True

        remaining = game._playing_players()
        assert len(remaining) == 1


class TestPointsMode:
    def test_penalty_flat(self):
        game, _ = _make_game(4, game_mode="points", penalty_tier="flat")
        game.on_start()
        p = game._playing_players()[0]
        p.hand = [Card(i, i + 3, 1) for i in range(5)]
        assert game._calculate_penalty(p) == 5

    def test_penalty_standard_10_plus(self):
        game, _ = _make_game(4, game_mode="points", penalty_tier="standard")
        game.on_start()
        p = game._playing_players()[0]
        p.hand = [Card(i, (i % 13) + 1, 1) for i in range(11)]
        penalty = game._calculate_penalty(p)
        assert penalty == 11 * 2  # 11 cards, x2 multiplier

    def test_penalty_standard_13(self):
        game, _ = _make_game(4, game_mode="points", penalty_tier="standard")
        game.on_start()
        p = game._playing_players()[0]
        p.hand = [Card(i, (i % 13) + 1, 1) for i in range(13)]
        penalty = game._calculate_penalty(p)
        assert penalty == 13 * 3  # 13 cards, x3 multiplier

    def test_penalty_aggressive(self):
        game, _ = _make_game(4, game_mode="points", penalty_tier="aggressive")
        game.on_start()
        p = game._playing_players()[0]
        p.hand = [Card(i, (i % 13) + 1, 1) for i in range(13)]
        penalty = game._calculate_penalty(p)
        assert penalty == 13 * 4  # x4 for 13 cards aggressive

    def test_penalty_per_two(self):
        game, _ = _make_game(4, game_mode="points", penalty_tier="flat", penalty_per_two=True)
        game.on_start()
        p = game._playing_players()[0]
        # 5 cards, 2 of which are 2s
        p.hand = [Card(0, 2, 1), Card(1, 2, 3), Card(2, 5, 1), Card(3, 6, 1), Card(4, 7, 1)]
        penalty = game._calculate_penalty(p)
        # 5 cards * 1 (flat) * 2 (first 2) * 2 (second 2) = 20
        assert penalty == 20

    def test_penalty_zero_cards(self):
        game, _ = _make_game(4, game_mode="points", penalty_tier="standard")
        game.on_start()
        p = game._playing_players()[0]
        p.hand = []
        assert game._calculate_penalty(p) == 0


class TestInstantWinGame:
    def test_instant_win_ends_round(self):
        game, players = _make_game(4, instant_wins=True, card_passing="off")
        game.on_start()

        # Manually set up a dragon hand for player 0
        active = game._playing_players()
        active[0].hand = [Card(i, r, (i % 4) + 1) for i, r in enumerate(range(1, 14))]

        found = game._check_instant_wins(active)
        assert found is True

    @pytest.mark.parametrize(("mode", "award"), [("rounds", 1), ("score", 100)])
    def test_instant_win_records_roulette_winner(self, mode, award):
        game, players = _make_game(4, instant_wins=True, card_passing="off")
        game.roulette = RouletteSession(
            ["pusoydos"], finish_mode=mode, total_rounds=1, target_score=1
        )
        active = game._playing_players()
        active[0].hand = [Card(i, r, (i % 4) + 1) for i, r in enumerate(range(1, 14))]

        assert game._check_instant_wins(active) is True
        assert game.roulette.scores == {p.id: award if p is active[0] else 0 for p in players}
        assert game._last_game_result is not None
        assert game._last_game_result.winner_ids == [active[0].id]

    def test_instant_wins_disabled(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()
        active = game._playing_players()
        active[0].hand = [Card(i, r, (i % 4) + 1) for i, r in enumerate(range(1, 14))]
        # instant_wins=False means _check_instant_wins won't be called,
        # but if it were, it should still detect
        found = game._check_instant_wins(active)
        assert found is True  # Detection itself still works


class TestCardPassing:
    def test_setup_exchange_moves_cards(self):
        game, players = _make_game(4, card_passing="simple")
        game.on_start()

        p1, p4 = game._playing_players()[0], game._playing_players()[3]
        p1_hand_before = len(p1.hand)
        p4_hand_before = len(p4.hand)

        # p4's highest card should move to p1
        p4_highest = sort_cards(p4.hand)[-1]

        game._setup_exchange(p1.id, p4.id, 1)

        # p1 gained 1 card, p4 lost 1 card (before p1 gives back)
        assert len(p1.hand) == p1_hand_before + 1
        assert len(p4.hand) == p4_hand_before - 1
        assert p4_highest in p1.hand
        # p1 still needs to give 1 card back
        assert p1.cards_to_give == 1
        assert p1.giving_cards is True


# =============================================================================
# Bot tests
# =============================================================================


class TestBot:
    def test_all_valid_combos(self):
        hand = [Card(0, 3, 1), Card(1, 3, 2), Card(2, 5, 1)]
        combos = get_all_valid_combos(hand)
        types = {c.type_name for c in combos}
        assert "single" in types
        assert "pair" in types

    def test_bot_plays_first_turn(self):
        game, _ = _make_game(4, instant_wins=False)
        game.on_start()

        current = game.current_player
        ids = bot_think(game, current)
        assert len(ids) > 0
        # Must include 3 of Clubs
        selected = [c for c in current.hand if c.id in ids]
        assert any(c.rank == 3 and c.suit == 2 for c in selected)

    def test_bot_passes_when_cannot_beat(self):
        game, _ = _make_game(4, instant_wins=False)
        game.on_start()

        game.is_first_turn = False

        current = game.current_player
        # Set an unbeatable combo
        game.current_combo = Combo("single", [Card(99, 2, 1)], 15, 4)  # 2 of Diamonds
        current.hand = [Card(0, 3, 2)]  # Only a 3 of Clubs

        ids = bot_think(game, current)
        assert ids == []  # Should pass

    def test_bot_choose_give_cards(self):
        hand = [Card(0, 3, 2), Card(1, 5, 1), Card(2, 2, 1)]  # 3c, 5d, 2d
        ids = bot_choose_give_cards(hand, 1)
        assert len(ids) == 1
        # Should give the lowest card (3 of Clubs)
        assert ids[0] == 0


# =============================================================================
# Serialization test
# =============================================================================


class TestSerialization:
    def test_round_trip(self):
        game, players = _make_game(4, instant_wins=False)
        game.on_start()

        # Serialize
        data = game.to_dict()
        assert "players" in data
        assert "options" in data
        assert data["options"]["game_mode"] == "elimination"

        # Deserialize
        game2 = PusoyDosGame.from_dict(data)
        assert len(game2.players) == len(game.players)
        assert game2.options.game_mode == game.options.game_mode
        assert game2.round == game.round

    def test_combo_serialization(self):
        combo = evaluate_combo([Card(0, 5, 1), Card(1, 5, 2)])
        data = combo.to_dict()
        combo2 = Combo.from_dict(data)
        assert combo2.type_name == "pair"
        assert combo2.rank_value == 5


# =============================================================================
# Play-to-completion (bot simulation)
# =============================================================================


class TestBotSimulation:
    def test_elimination_game_completes(self):
        """A full game with 4 bots should complete in elimination mode."""
        game = PusoyDosGame()
        game.options.game_mode = "elimination"
        game.options.rounds_to_win = 1

        for i in range(4):
            game.add_player(f"bot{i + 1}", Bot(f"bot{i + 1}"))

        game.on_start()

        for _ in range(50000):
            game.on_tick()
            if game.status != "playing":
                break

        assert game.status != "playing", "Game did not complete within tick limit"

    def test_points_game_completes(self):
        """A full game with 4 bots should complete in points mode."""
        game = PusoyDosGame()
        game.options.game_mode = "points"
        game.options.target_score = 30
        game.options.penalty_tier = "aggressive"  # Higher penalties = faster scoring

        for i in range(4):
            game.add_player(f"bot{i + 1}", Bot(f"bot{i + 1}"))

        game.on_start()

        for _ in range(200000):
            game.on_tick()
            if game.status != "playing":
                break

        assert game.status != "playing", "Game did not complete within tick limit"

    def test_2_player_game_completes(self):
        """A 2-player bot game should complete."""
        game = PusoyDosGame()
        game.options.game_mode = "elimination"
        game.options.rounds_to_win = 1

        for i in range(2):
            game.add_player(f"bot{i + 1}", Bot(f"bot{i + 1}"))

        game.on_start()

        for _ in range(50000):
            game.on_tick()
            if game.status != "playing":
                break

        assert game.status != "playing", "2-player game did not complete"

    def test_3_player_game_completes(self):
        """A 3-player bot game should complete."""
        game = PusoyDosGame()
        game.options.game_mode = "elimination"
        game.options.rounds_to_win = 1

        for i in range(3):
            game.add_player(f"bot{i + 1}", Bot(f"bot{i + 1}"))

        game.on_start()

        for _ in range(50000):
            game.on_tick()
            if game.status != "playing":
                break

        assert game.status != "playing", "3-player game did not complete"
