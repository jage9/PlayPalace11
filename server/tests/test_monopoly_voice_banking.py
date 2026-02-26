"""Integration tests for Monopoly voice banking preset behavior."""

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.users.test_user import MockUser


def _create_two_player_game(options: MonopolyOptions | None = None) -> MonopolyGame:
    game = MonopolyGame(options=options or MonopolyOptions())
    host_user = MockUser("Host")
    guest_user = MockUser("Guest")
    game.add_player("Host", host_user)
    game.add_player("Guest", guest_user)
    game.host = "Host"
    return game


def _start_two_player_game(options: MonopolyOptions | None = None) -> MonopolyGame:
    game = _create_two_player_game(options)
    game.on_start()
    return game


def test_voice_banking_on_start_initializes_profile_and_accounts():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    assert game.voice_banking_profile is not None
    assert game.voice_banking_profile.anchor_edition_id == "monopoly-e4816"
    assert game.banking_state is not None
    assert game._bank_balance(game.players[0]) > 0


def test_voice_commands_require_exact_voice_prefix():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None

    game.execute_action(host, "voice_command", input_value="Voice: balance")
    assert game.voice_last_response_by_player_id.get(host.id) == "missing_prefix"

    game.execute_action(host, "voice_command", input_value="voice: balance")
    assert game.voice_last_response_by_player_id.get(host.id) == "check_balance"


def test_voice_balance_and_ledger_and_repeat_flow():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None

    game.execute_action(host, "voice_command", input_value="voice: balance")
    assert game.voice_last_response_by_player_id[host.id] == "check_balance"

    game.execute_action(host, "voice_command", input_value="voice: ledger")
    assert game.voice_last_response_by_player_id[host.id] == "show_recent_ledger"

    game.execute_action(host, "voice_command", input_value="voice: repeat")
    assert game.voice_last_response_by_player_id[host.id] == "repeat_last_bank_result"


def test_voice_transfer_requires_confirm_then_executes():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None
    guest = game.players[1]

    game.execute_action(host, "voice_command", input_value=f"voice: transfer 200 to {guest.name}")
    assert host.id in game.voice_pending_transfer_by_player_id
    assert game._bank_balance(host) == 1500

    game.execute_action(host, "voice_command", input_value="voice: confirm transfer")
    assert host.id not in game.voice_pending_transfer_by_player_id
    assert game._bank_balance(host) == 1300
    assert game._bank_balance(guest) == 1700


def test_voice_transfer_insufficient_funds_keeps_balances_unchanged():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None
    guest = game.players[1]
    assert game.banking_state is not None
    game.banking_state.accounts[host.id].balance = 100
    game._sync_player_cash_from_banking(host)

    game.execute_action(host, "voice_command", input_value=f"voice: transfer 200 to {guest.name}")
    game.execute_action(host, "voice_command", input_value="voice: confirm transfer")

    assert game._bank_balance(host) == 100
    assert game._bank_balance(guest) == 1500
