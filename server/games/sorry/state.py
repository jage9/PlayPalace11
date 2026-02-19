"""Serializable state models and board helpers for Sorry."""

from dataclasses import dataclass, field
import random


TRACK_LENGTH = 60
SAFETY_LENGTH = 5
PAWNS_PER_PLAYER = 4
MAX_PLAYERS = 4
SEAT_START_TRACKS: tuple[int, ...] = (0, 15, 30, 45)

CARD_FACES: tuple[str, ...] = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "7",
    "8",
    "10",
    "11",
    "12",
    "sorry",
)


@dataclass
class SorryPawnState:
    """State for one pawn on the Sorry board."""

    pawn_index: int
    zone: str = "start"  # start | track | home_path | home
    track_position: int | None = None
    home_steps: int = 0


def create_default_pawns() -> list[SorryPawnState]:
    """Create default pawn states for a player."""
    return [SorryPawnState(pawn_index=i + 1) for i in range(PAWNS_PER_PLAYER)]


def create_pawns_for_count(pawns_per_player: int) -> list[SorryPawnState]:
    """Create pawn states for the requested profile pawn count."""
    return [SorryPawnState(pawn_index=i + 1) for i in range(pawns_per_player)]


@dataclass
class SorryPlayerState:
    """Serializable board state for one player."""

    player_id: str
    seat_index: int
    start_track: int
    home_entry_track: int
    pawns: list[SorryPawnState] = field(default_factory=create_default_pawns)


@dataclass
class SorryGameState:
    """Serializable game-level state for Sorry."""

    player_order: list[str] = field(default_factory=list)
    player_states: dict[str, SorryPlayerState] = field(default_factory=dict)
    draw_pile: list[str] = field(default_factory=list)
    discard_pile: list[str] = field(default_factory=list)
    current_card: str | None = None
    turn_phase: str = "draw"  # draw | choose_move | resolve
    turn_number: int = 1


def normalize_track_position(position: int) -> int:
    """Normalize a track position to 0..TRACK_LENGTH-1."""
    return position % TRACK_LENGTH


def get_start_track_for_seat(seat_index: int) -> int:
    """Get track entry position for a player seat."""
    return SEAT_START_TRACKS[seat_index % MAX_PLAYERS]


def get_home_entry_track_for_seat(seat_index: int) -> int:
    """Get track square just before entering this seat's home path."""
    start_track = get_start_track_for_seat(seat_index)
    return normalize_track_position(start_track - 1)


def clockwise_distance(start: int, end: int) -> int:
    """Compute clockwise steps from one track position to another."""
    return normalize_track_position(end - start)


def build_default_draw_pile() -> list[str]:
    """Build classic deck composition used by the current baseline rules."""
    deck: list[str] = []
    for card in CARD_FACES:
        deck.extend([card] * 4)
    return deck


def shuffle_cards(cards: list[str], rng: random.Random | None = None) -> None:
    """Shuffle card list in place."""
    if rng is None:
        random.shuffle(cards)
        return
    rng.shuffle(cards)


def draw_next_card(
    state: SorryGameState,
    rng: random.Random | None = None,
) -> str | None:
    """Draw next card, reshuffling discard into draw pile when needed."""
    if not state.draw_pile and state.discard_pile:
        state.draw_pile = state.discard_pile[:]
        state.discard_pile = []
        shuffle_cards(state.draw_pile, rng)
    if not state.draw_pile:
        return None
    card = state.draw_pile.pop()
    state.current_card = card
    return card


def discard_current_card(state: SorryGameState) -> None:
    """Move current card to discard pile and clear current card slot."""
    if state.current_card is None:
        return
    state.discard_pile.append(state.current_card)
    state.current_card = None


def get_track_occupancy(
    state: SorryGameState,
) -> dict[int, list[tuple[str, int]]]:
    """Return mapping of track position to occupying pawns."""
    occupancy: dict[int, list[tuple[str, int]]] = {}
    for player_id, player_state in state.player_states.items():
        for pawn in player_state.pawns:
            if pawn.zone != "track" or pawn.track_position is None:
                continue
            pos = normalize_track_position(pawn.track_position)
            occupancy.setdefault(pos, []).append((player_id, pawn.pawn_index))
    return occupancy


def build_initial_game_state(
    player_ids: list[str],
    *,
    pawns_per_player: int = PAWNS_PER_PLAYER,
    faster_setup_one_pawn_out: bool = False,
    shuffle_deck: bool = True,
    rng: random.Random | None = None,
) -> SorryGameState:
    """Build initial serializable state for a new game."""
    if len(player_ids) > MAX_PLAYERS:
        raise ValueError("Sorry supports at most 4 players")
    if pawns_per_player < 1:
        raise ValueError("Sorry requires at least one pawn per player")

    player_states: dict[str, SorryPlayerState] = {}
    ordered_player_ids = player_ids[:]
    for seat_index, player_id in enumerate(ordered_player_ids):
        start_track = get_start_track_for_seat(seat_index)
        home_entry_track = get_home_entry_track_for_seat(seat_index)
        player_state = SorryPlayerState(
            player_id=player_id,
            seat_index=seat_index,
            start_track=start_track,
            home_entry_track=home_entry_track,
            pawns=create_pawns_for_count(pawns_per_player),
        )
        if faster_setup_one_pawn_out and player_state.pawns:
            player_state.pawns[0].zone = "track"
            player_state.pawns[0].track_position = start_track
        player_states[player_id] = player_state

    draw_pile = build_default_draw_pile()
    if shuffle_deck:
        shuffle_cards(draw_pile, rng)

    return SorryGameState(
        player_order=ordered_player_ids,
        player_states=player_states,
        draw_pile=draw_pile,
    )
