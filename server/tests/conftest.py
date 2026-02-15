"""Pytest configuration and fixtures."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Initialize localization for tests
from server.messages.localization import Localization

_locales_dir = Path(__file__).parent.parent / "locales"
Localization.init(_locales_dir)

def pytest_addoption(parser):
    parser.addoption(
        "--runslow",
        action="store_true",
        default=False,
        help="run tests marked as slow",
    )


def pytest_runtest_setup(item):
    if "slow" in item.keywords and not item.config.getoption("--runslow"):
        pytest.skip("use --runslow to run slow tests")


@pytest.fixture
def mock_user():
    """Create a mock user."""
    from server.core.users.test_user import MockUser

    return MockUser("TestPlayer")


@pytest.fixture
def bot():
    """Create a bot user."""
    from server.core.users.bot import Bot

    return Bot("TestBot")


@pytest.fixture
def pig_game():
    """Create a fresh Pig game."""
    from server.games.pig.game import PigGame

    return PigGame()


@pytest.fixture
def pig_game_with_players():
    """Create a Pig game with two players."""
    from server.games.pig.game import PigGame
    from server.core.users.test_user import MockUser

    game = PigGame()
    user1 = MockUser("Alice")
    user2 = MockUser("Bob")
    game.add_player("Alice", user1)
    game.add_player("Bob", user2)
    return game, user1, user2
