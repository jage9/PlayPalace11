"""Monopoly game scaffold wired to generated preset artifacts."""

from __future__ import annotations

from dataclasses import dataclass, field
import random

from ..base import Game, Player, GameOptions
from ..registry import register_game
from ...game_utils.action_guard_mixin import ActionGuardMixin
from ...game_utils.bot_helper import BotHelper
from ...game_utils.actions import Action, ActionSet, EditboxInput, Visibility, MenuInput
from ...game_utils.options import MenuOption, option_field
from ...messages.localization import Localization
from ...core.ui.keybinds import KeybindState
from .banking_sim import (
    BANK_ACCOUNT_ID,
    BankingState,
    ElectronicBankingProfile,
    credit as bank_credit,
    debit as bank_debit,
    get_balance as bank_get_balance,
    init_accounts as init_bank_accounts,
    transfer as bank_transfer,
)
from .board_profile import (
    DEFAULT_BOARD_ID,
    DEFAULT_BOARD_RULES_MODE,
    get_board_label_keys as _board_label_keys,
    get_board_profile,
    get_available_board_ids as _board_profile_ids,
    get_available_board_rules_modes as _board_rules_modes,
    resolve_board_plan,
)
from .board_parity import get_board_parity_profile
from .board_rules_registry import (
    get_card_cash_override,
    get_card_id_remap,
    get_pass_go_credit_override,
    get_rule_pack,
    supports_capability,
)
from .city_engine import CityEngine
from .city_profile import CityProfile, resolve_city_profile
from .cheaters_engine import CheaterOutcome, CheatersEngine
from .cheaters_profile import CheatersProfile, resolve_cheaters_profile
from .electronic_banking_profile import resolve_electronic_banking_profile
from .junior_rules import (
    JuniorRuleset,
    get_junior_ruleset,
    is_junior_ruleset_preset,
)
from .voice_banking_profile import (
    VoiceBankingProfile,
    resolve_voice_banking_profile,
)
from .hardware_emulation import HardwareEvent, HardwareResult, resolve_hardware_event
from .manual_rules.loader import load_manual_rule_set
from .manual_rules.models import ManualRuleSet
from .deck_provider import resolve_deck_provider
from .presets import (
    DEFAULT_PRESET_ID,
    MonopolyPreset,
    get_available_preset_ids as _catalog_preset_ids,
    get_default_preset_id as _catalog_default_preset_id,
    get_preset as _catalog_get_preset,
)
from .actions import guards as action_guards
from .actions import handlers as action_handlers
from .actions import options as action_options


PRESET_LABEL_KEYS = {
    "classic_standard": "monopoly-preset-classic-standard",
    "junior": "monopoly-preset-junior",
    "junior_modern": "monopoly-preset-junior-modern",
    "junior_legacy": "monopoly-preset-junior-legacy",
    "cheaters": "monopoly-preset-cheaters",
    "electronic_banking": "monopoly-preset-electronic-banking",
    "voice_banking": "monopoly-preset-voice-banking",
    "sore_losers": "monopoly-preset-sore-losers",
    "speed": "monopoly-preset-speed",
    "builder": "monopoly-preset-builder",
    "city": "monopoly-preset-city",
    "bid_card_game": "monopoly-preset-bid-card-game",
    "deal_card_game": "monopoly-preset-deal-card-game",
    "knockout": "monopoly-preset-knockout",
    "free_parking_jackpot": "monopoly-preset-free-parking-jackpot",
}
BOARD_LABEL_KEYS = _board_label_keys()
BOARD_RULES_MODE_LABEL_KEYS = {
    "auto": "monopoly-board-rules-mode-auto",
    "skin_only": "monopoly-board-rules-mode-skin-only",
}
JUNIOR_MODERN_PRESET_ID = "junior_modern"
JUNIOR_LEGACY_PRESET_ID = "junior_legacy"


@dataclass(frozen=True)
class MonopolySpace:
    """A board space on the classic Monopoly board."""

    index: int
    space_id: str
    name: str
    kind: str
    price: int = 0
    rent: int = 0
    color_group: str = ""
    house_cost: int = 0
    rents: tuple[int, ...] = ()


CLASSIC_STANDARD_BOARD = [
    MonopolySpace(0, "go", "GO", "start"),
    MonopolySpace(
        1,
        "mediterranean_avenue",
        "Mediterranean Avenue",
        "property",
        60,
        2,
        color_group="brown",
        house_cost=50,
        rents=(2, 10, 30, 90, 160, 250),
    ),
    MonopolySpace(2, "community_chest_1", "Community Chest", "community_chest"),
    MonopolySpace(
        3,
        "baltic_avenue",
        "Baltic Avenue",
        "property",
        60,
        4,
        color_group="brown",
        house_cost=50,
        rents=(4, 20, 60, 180, 320, 450),
    ),
    MonopolySpace(4, "income_tax", "Income Tax", "tax"),
    MonopolySpace(5, "reading_railroad", "Reading Railroad", "railroad", 200, 25),
    MonopolySpace(
        6,
        "oriental_avenue",
        "Oriental Avenue",
        "property",
        100,
        6,
        color_group="light_blue",
        house_cost=50,
        rents=(6, 30, 90, 270, 400, 550),
    ),
    MonopolySpace(7, "chance_1", "Chance", "chance"),
    MonopolySpace(
        8,
        "vermont_avenue",
        "Vermont Avenue",
        "property",
        100,
        6,
        color_group="light_blue",
        house_cost=50,
        rents=(6, 30, 90, 270, 400, 550),
    ),
    MonopolySpace(
        9,
        "connecticut_avenue",
        "Connecticut Avenue",
        "property",
        120,
        8,
        color_group="light_blue",
        house_cost=50,
        rents=(8, 40, 100, 300, 450, 600),
    ),
    MonopolySpace(10, "jail", "Jail / Just Visiting", "jail"),
    MonopolySpace(
        11,
        "st_charles_place",
        "St. Charles Place",
        "property",
        140,
        10,
        color_group="pink",
        house_cost=100,
        rents=(10, 50, 150, 450, 625, 750),
    ),
    MonopolySpace(12, "electric_company", "Electric Company", "utility", 150, 20),
    MonopolySpace(
        13,
        "states_avenue",
        "States Avenue",
        "property",
        140,
        10,
        color_group="pink",
        house_cost=100,
        rents=(10, 50, 150, 450, 625, 750),
    ),
    MonopolySpace(
        14,
        "virginia_avenue",
        "Virginia Avenue",
        "property",
        160,
        12,
        color_group="pink",
        house_cost=100,
        rents=(12, 60, 180, 500, 700, 900),
    ),
    MonopolySpace(15, "pennsylvania_railroad", "Pennsylvania Railroad", "railroad", 200, 25),
    MonopolySpace(
        16,
        "st_james_place",
        "St. James Place",
        "property",
        180,
        14,
        color_group="orange",
        house_cost=100,
        rents=(14, 70, 200, 550, 750, 950),
    ),
    MonopolySpace(17, "community_chest_2", "Community Chest", "community_chest"),
    MonopolySpace(
        18,
        "tennessee_avenue",
        "Tennessee Avenue",
        "property",
        180,
        14,
        color_group="orange",
        house_cost=100,
        rents=(14, 70, 200, 550, 750, 950),
    ),
    MonopolySpace(
        19,
        "new_york_avenue",
        "New York Avenue",
        "property",
        200,
        16,
        color_group="orange",
        house_cost=100,
        rents=(16, 80, 220, 600, 800, 1000),
    ),
    MonopolySpace(20, "free_parking", "Free Parking", "free_parking"),
    MonopolySpace(
        21,
        "kentucky_avenue",
        "Kentucky Avenue",
        "property",
        220,
        18,
        color_group="red",
        house_cost=150,
        rents=(18, 90, 250, 700, 875, 1050),
    ),
    MonopolySpace(22, "chance_2", "Chance", "chance"),
    MonopolySpace(
        23,
        "indiana_avenue",
        "Indiana Avenue",
        "property",
        220,
        18,
        color_group="red",
        house_cost=150,
        rents=(18, 90, 250, 700, 875, 1050),
    ),
    MonopolySpace(
        24,
        "illinois_avenue",
        "Illinois Avenue",
        "property",
        240,
        20,
        color_group="red",
        house_cost=150,
        rents=(20, 100, 300, 750, 925, 1100),
    ),
    MonopolySpace(25, "bo_railroad", "B. & O. Railroad", "railroad", 200, 25),
    MonopolySpace(
        26,
        "atlantic_avenue",
        "Atlantic Avenue",
        "property",
        260,
        22,
        color_group="yellow",
        house_cost=150,
        rents=(22, 110, 330, 800, 975, 1150),
    ),
    MonopolySpace(
        27,
        "ventnor_avenue",
        "Ventnor Avenue",
        "property",
        260,
        22,
        color_group="yellow",
        house_cost=150,
        rents=(22, 110, 330, 800, 975, 1150),
    ),
    MonopolySpace(28, "water_works", "Water Works", "utility", 150, 20),
    MonopolySpace(
        29,
        "marvin_gardens",
        "Marvin Gardens",
        "property",
        280,
        24,
        color_group="yellow",
        house_cost=150,
        rents=(24, 120, 360, 850, 1025, 1200),
    ),
    MonopolySpace(30, "go_to_jail", "Go to Jail", "go_to_jail"),
    MonopolySpace(
        31,
        "pacific_avenue",
        "Pacific Avenue",
        "property",
        300,
        26,
        color_group="green",
        house_cost=200,
        rents=(26, 130, 390, 900, 1100, 1275),
    ),
    MonopolySpace(
        32,
        "north_carolina_avenue",
        "North Carolina Avenue",
        "property",
        300,
        26,
        color_group="green",
        house_cost=200,
        rents=(26, 130, 390, 900, 1100, 1275),
    ),
    MonopolySpace(33, "community_chest_3", "Community Chest", "community_chest"),
    MonopolySpace(
        34,
        "pennsylvania_avenue",
        "Pennsylvania Avenue",
        "property",
        320,
        28,
        color_group="green",
        house_cost=200,
        rents=(28, 150, 450, 1000, 1200, 1400),
    ),
    MonopolySpace(35, "short_line", "Short Line", "railroad", 200, 25),
    MonopolySpace(36, "chance_3", "Chance", "chance"),
    MonopolySpace(
        37,
        "park_place",
        "Park Place",
        "property",
        350,
        35,
        color_group="dark_blue",
        house_cost=200,
        rents=(35, 175, 500, 1100, 1300, 1500),
    ),
    MonopolySpace(38, "luxury_tax", "Luxury Tax", "tax"),
    MonopolySpace(
        39,
        "boardwalk",
        "Boardwalk",
        "property",
        400,
        50,
        color_group="dark_blue",
        house_cost=200,
        rents=(50, 200, 600, 1400, 1700, 2000),
    ),
]
SPACE_BY_ID = {space.space_id: space for space in CLASSIC_STANDARD_BOARD}
COLOR_GROUP_TO_SPACE_IDS: dict[str, list[str]] = {}
for _space in CLASSIC_STANDARD_BOARD:
    if _space.color_group:
        COLOR_GROUP_TO_SPACE_IDS.setdefault(_space.color_group, []).append(_space.space_id)
PURCHASABLE_KINDS = {"property", "railroad", "utility"}
BOARD_SIZE = len(CLASSIC_STANDARD_BOARD)
STARTING_CASH = 1500
PASS_GO_CASH = 200
TAX_AMOUNTS = {"income_tax": 200, "luxury_tax": 100}
BAIL_AMOUNT = 50
MIN_AUCTION_INCREMENT = 10
TOTAL_HOUSES = 32
TOTAL_HOTELS = 12
JAIL_CARD_TRADE_CASH = 50

CHANCE_CARD_IDS = [
    "advance_to_go",
    "bank_dividend_50",
    "go_back_three",
    "go_to_jail",
    "poor_tax_15",
]
COMMUNITY_CHEST_CARD_IDS = [
    "bank_error_collect_200",
    "doctor_fee_pay_50",
    "income_tax_refund_20",
    "go_to_jail",
    "get_out_of_jail_free",
]
CARD_DESCRIPTION_KEYS = {
    "advance_to_go": "monopoly-card-advance-to-go",
    "bank_dividend_50": "monopoly-card-bank-dividend-50",
    "go_back_three": "monopoly-card-go-back-three",
    "go_to_jail": "monopoly-card-go-to-jail",
    "poor_tax_15": "monopoly-card-poor-tax-15",
    "bank_error_collect_200": "monopoly-card-bank-error-200",
    "doctor_fee_pay_50": "monopoly-card-doctor-fee-50",
    "income_tax_refund_20": "monopoly-card-tax-refund-20",
    "get_out_of_jail_free": "monopoly-card-get-out-of-jail",
}


@dataclass(frozen=True)
class MonopolyRuleProfile:
    """Preset-scoped gameplay rule switches and economy knobs."""

    preset_id: str
    starting_cash: int = STARTING_CASH
    pass_go_cash: int = PASS_GO_CASH
    bail_amount: int = BAIL_AMOUNT
    enable_free_parking_jackpot: bool = False
    allow_manual_property_buy: bool = True
    auto_auction_unowned_property: bool = False
    doubles_grant_extra_roll: bool = True
    require_full_set_for_build: bool = True
    builder_blocks_per_purchase: int = 0
    builder_block_required_for_build: bool = False
    sore_loser_rebate_on_payment: int = 0


RULE_PROFILES: dict[str, MonopolyRuleProfile] = {
    DEFAULT_PRESET_ID: MonopolyRuleProfile(preset_id=DEFAULT_PRESET_ID),
    "electronic_banking": MonopolyRuleProfile(preset_id="electronic_banking"),
    JUNIOR_MODERN_PRESET_ID: MonopolyRuleProfile(
        preset_id=JUNIOR_MODERN_PRESET_ID,
        starting_cash=get_junior_ruleset(JUNIOR_MODERN_PRESET_ID).starting_cash,
        pass_go_cash=get_junior_ruleset(JUNIOR_MODERN_PRESET_ID).pass_go_cash,
        bail_amount=get_junior_ruleset(JUNIOR_MODERN_PRESET_ID).bail_amount,
        doubles_grant_extra_roll=False,
    ),
    JUNIOR_LEGACY_PRESET_ID: MonopolyRuleProfile(
        preset_id=JUNIOR_LEGACY_PRESET_ID,
        starting_cash=get_junior_ruleset(JUNIOR_LEGACY_PRESET_ID).starting_cash,
        pass_go_cash=get_junior_ruleset(JUNIOR_LEGACY_PRESET_ID).pass_go_cash,
        bail_amount=get_junior_ruleset(JUNIOR_LEGACY_PRESET_ID).bail_amount,
        doubles_grant_extra_roll=False,
    ),
    "free_parking_jackpot": MonopolyRuleProfile(
        preset_id="free_parking_jackpot",
        enable_free_parking_jackpot=True,
    ),
    "sore_losers": MonopolyRuleProfile(
        preset_id="sore_losers",
        sore_loser_rebate_on_payment=10,
    ),
    "speed": MonopolyRuleProfile(
        preset_id="speed",
        starting_cash=1000,
        pass_go_cash=100,
        allow_manual_property_buy=False,
        auto_auction_unowned_property=True,
        doubles_grant_extra_roll=False,
    ),
    "builder": MonopolyRuleProfile(
        preset_id="builder",
        require_full_set_for_build=False,
        builder_blocks_per_purchase=1,
        builder_block_required_for_build=True,
    ),
}


@dataclass
class MonopolyPlayer(Player):
    """Player state for Monopoly scaffold."""

    position: int = 0
    cash: int = STARTING_CASH
    owned_space_ids: list[str] = field(default_factory=list)
    bankrupt: bool = False
    in_jail: bool = False
    jail_turns: int = 0
    get_out_of_jail_cards: int = 0
    builder_blocks: int = 0


@dataclass
class MonopolyTradeOffer:
    """Pending trade offer between two players."""

    proposer_id: str = ""
    target_id: str = ""
    give_cash: int = 0
    give_property_id: str = ""
    give_jail_cards: int = 0
    receive_cash: int = 0
    receive_property_id: str = ""
    receive_jail_cards: int = 0
    summary: str = ""


@dataclass
class MonopolyOptions(GameOptions):
    """Lobby options for Monopoly scaffold."""

    preset_id: str = option_field(
        MenuOption(
            default=DEFAULT_PRESET_ID,
            choices=lambda game, player: game.get_available_preset_ids(),
            value_key="preset",
            choice_labels=PRESET_LABEL_KEYS,
            label="monopoly-set-preset",
            prompt="monopoly-select-preset",
            change_msg="monopoly-option-changed-preset",
        )
    )
    board_id: str = option_field(
        MenuOption(
            default=DEFAULT_BOARD_ID,
            choices=lambda game, player: game.get_available_board_ids(),
            value_key="board",
            choice_labels=BOARD_LABEL_KEYS,
            label="monopoly-set-board",
            prompt="monopoly-select-board",
            change_msg="monopoly-option-changed-board",
        )
    )
    board_rules_mode: str = option_field(
        MenuOption(
            default=DEFAULT_BOARD_RULES_MODE,
            choices=lambda game, player: game.get_available_board_rules_modes(),
            value_key="mode",
            choice_labels=BOARD_RULES_MODE_LABEL_KEYS,
            label="monopoly-set-board-rules-mode",
            prompt="monopoly-select-board-rules-mode",
            change_msg="monopoly-option-changed-board-rules-mode",
        )
    )


@dataclass
@register_game
class MonopolyGame(ActionGuardMixin, Game):
    """Catalog-backed Monopoly scaffold.

    This class intentionally wires preset selection and metadata loading first.
    Gameplay mechanics are added incrementally in later milestones.
    """

    players: list[MonopolyPlayer] = field(default_factory=list)
    options: MonopolyOptions = field(default_factory=MonopolyOptions)

    active_preset_id: str = DEFAULT_PRESET_ID
    active_preset_name: str = ""
    active_family_key: str = ""
    active_edition_ids: list[str] = field(default_factory=list)
    active_anchor_edition_id: str = ""
    active_board_id: str = DEFAULT_BOARD_ID
    active_board_anchor_edition_id: str = ""
    active_board_rules_mode: str = DEFAULT_BOARD_RULES_MODE
    active_board_effective_mode: str = "skin_only"
    active_board_rule_pack_id: str = ""
    active_board_rule_pack_status: str = "none"
    active_board_auto_fixed_from_preset_id: str = ""
    active_board_deck_mode: str = "classic"
    active_board_parity_fidelity_status: str = "none"
    active_board_hardware_capability_ids: tuple[str, ...] = ()
    active_manual_rule_set: ManualRuleSet | None = None
    active_board_spaces: list[MonopolySpace] = field(
        default_factory=lambda: CLASSIC_STANDARD_BOARD.copy()
    )
    active_space_by_id: dict[str, MonopolySpace] = field(default_factory=lambda: SPACE_BY_ID.copy())
    active_color_group_to_space_ids: dict[str, list[str]] = field(
        default_factory=lambda: {
            key: values.copy() for key, values in COLOR_GROUP_TO_SPACE_IDS.items()
        }
    )
    active_board_size: int = BOARD_SIZE
    active_sound_mode: str = "none"
    last_hardware_event_id: str = ""
    last_hardware_event_status: str = "none"
    last_hardware_event_details: str = ""
    junior_ruleset: JuniorRuleset | None = None
    cheaters_profile: CheatersProfile | None = None
    cheaters_engine: CheatersEngine | None = None
    city_profile: CityProfile | None = None
    city_engine: CityEngine | None = None
    voice_banking_profile: VoiceBankingProfile | None = None
    banking_profile: ElectronicBankingProfile | None = None
    banking_state: BankingState | None = None
    voice_last_response_by_player_id: dict[str, str] = field(default_factory=dict)
    voice_pending_transfer_by_player_id: dict[str, tuple[str, int]] = field(default_factory=dict)
    rule_profile: MonopolyRuleProfile = field(
        default_factory=lambda: RULE_PROFILES[DEFAULT_PRESET_ID]
    )
    property_owners: dict[str, str] = field(default_factory=dict)
    mortgaged_space_ids: list[str] = field(default_factory=list)
    building_levels: dict[str, int] = field(default_factory=dict)
    pending_trade_offer: MonopolyTradeOffer | None = None
    free_parking_pool: int = 0
    pending_auction_space_id: str = ""
    pending_auction_bidder_ids: list[str] = field(default_factory=list)
    pending_auction_turn_index: int = 0
    pending_auction_high_bidder_id: str = ""
    pending_auction_current_bid: int = 0

    turn_has_rolled: bool = False
    turn_last_roll: list[int] = field(default_factory=list)
    turn_pending_purchase_space_id: str = ""
    turn_doubles_count: int = 0
    turn_can_roll_again: bool = False
    junior_endgame_evaluating: bool = False
    city_endgame_evaluating: bool = False

    chance_deck_order: list[str] = field(default_factory=lambda: CHANCE_CARD_IDS.copy())
    chance_deck_index: int = 0
    community_chest_deck_order: list[str] = field(
        default_factory=lambda: COMMUNITY_CHEST_CARD_IDS.copy()
    )
    community_chest_deck_index: int = 0

    @classmethod
    def get_name(cls) -> str:
        return "Monopoly"

    @classmethod
    def get_type(cls) -> str:
        return "monopoly"

    @classmethod
    def get_category(cls) -> str:
        return "category-uncategorized"

    @classmethod
    def get_min_players(cls) -> int:
        return 2

    @classmethod
    def get_max_players(cls) -> int:
        return 6

    def create_player(
        self, player_id: str, name: str, is_bot: bool = False
    ) -> MonopolyPlayer:
        """Create a Monopoly player."""
        return MonopolyPlayer(id=player_id, name=name, is_bot=is_bot)

    def _add_turn_roll_and_purchase_actions(self, action_set: ActionSet, locale: str) -> None:
        action_set.add(
            Action(
                id="roll_dice",
                label=Localization.get(locale, "monopoly-roll-dice"),
                handler="_action_roll_dice",
                is_enabled="_is_roll_dice_enabled",
                is_hidden="_is_roll_dice_hidden",
            )
        )
        action_set.add(
            Action(
                id="buy_property",
                label=Localization.get(locale, "monopoly-buy-property"),
                handler="_action_buy_property",
                is_enabled="_is_buy_property_enabled",
                is_hidden="_is_buy_property_hidden",
            )
        )

    def _add_turn_auction_actions(self, action_set: ActionSet, locale: str) -> None:
        action_set.add(
            Action(
                id="auction_property",
                label=Localization.get(locale, "monopoly-auction-property"),
                handler="_action_auction_property",
                is_enabled="_is_auction_property_enabled",
                is_hidden="_is_auction_property_hidden",
            )
        )
        action_set.add(
            Action(
                id="auction_bid",
                label=Localization.get(locale, "monopoly-auction-bid"),
                handler="_action_auction_bid",
                is_enabled="_is_auction_bid_enabled",
                is_hidden="_is_auction_bid_hidden",
                input_request=MenuInput(
                    prompt="monopoly-select-auction-bid",
                    options="_options_for_auction_bid",
                    bot_select="_bot_select_auction_bid",
                ),
            )
        )
        action_set.add(
            Action(
                id="auction_pass",
                label=Localization.get(locale, "monopoly-auction-pass"),
                handler="_action_auction_pass",
                is_enabled="_is_auction_pass_enabled",
                is_hidden="_is_auction_pass_hidden",
            )
        )

    def _add_turn_property_management_actions(
        self, action_set: ActionSet, locale: str
    ) -> None:
        action_set.add(
            Action(
                id="mortgage_property",
                label=Localization.get(locale, "monopoly-mortgage-property"),
                handler="_action_mortgage_property",
                is_enabled="_is_mortgage_property_enabled",
                is_hidden="_is_mortgage_property_hidden",
                input_request=MenuInput(
                    prompt="monopoly-select-property-mortgage",
                    options="_options_for_mortgage_property",
                    bot_select="_bot_select_mortgage_property",
                ),
            )
        )
        action_set.add(
            Action(
                id="unmortgage_property",
                label=Localization.get(locale, "monopoly-unmortgage-property"),
                handler="_action_unmortgage_property",
                is_enabled="_is_unmortgage_property_enabled",
                is_hidden="_is_unmortgage_property_hidden",
                input_request=MenuInput(
                    prompt="monopoly-select-property-unmortgage",
                    options="_options_for_unmortgage_property",
                    bot_select="_bot_select_unmortgage_property",
                ),
            )
        )
        action_set.add(
            Action(
                id="build_house",
                label=Localization.get(locale, "monopoly-build-house"),
                handler="_action_build_house",
                is_enabled="_is_build_house_enabled",
                is_hidden="_is_build_house_hidden",
                input_request=MenuInput(
                    prompt="monopoly-select-property-build",
                    options="_options_for_build_house",
                    bot_select="_bot_select_build_house",
                ),
            )
        )
        action_set.add(
            Action(
                id="sell_house",
                label=Localization.get(locale, "monopoly-sell-house"),
                handler="_action_sell_house",
                is_enabled="_is_sell_house_enabled",
                is_hidden="_is_sell_house_hidden",
                input_request=MenuInput(
                    prompt="monopoly-select-property-sell",
                    options="_options_for_sell_house",
                ),
            )
        )

    def _add_turn_trade_actions(self, action_set: ActionSet, locale: str) -> None:
        action_set.add(
            Action(
                id="offer_trade",
                label=Localization.get(locale, "monopoly-offer-trade"),
                handler="_action_offer_trade",
                is_enabled="_is_offer_trade_enabled",
                is_hidden="_is_offer_trade_hidden",
                input_request=MenuInput(
                    prompt="monopoly-select-trade-offer",
                    options="_options_for_offer_trade",
                ),
            )
        )
        action_set.add(
            Action(
                id="accept_trade",
                label=Localization.get(locale, "monopoly-accept-trade"),
                handler="_action_accept_trade",
                is_enabled="_is_accept_trade_enabled",
                is_hidden="_is_accept_trade_hidden",
            )
        )
        action_set.add(
            Action(
                id="decline_trade",
                label=Localization.get(locale, "monopoly-decline-trade"),
                handler="_action_decline_trade",
                is_enabled="_is_decline_trade_enabled",
                is_hidden="_is_decline_trade_hidden",
            )
        )

    def _add_turn_jail_actions(self, action_set: ActionSet, locale: str) -> None:
        action_set.add(
            Action(
                id="pay_bail",
                label=Localization.get(locale, "monopoly-pay-bail"),
                handler="_action_pay_bail",
                is_enabled="_is_pay_bail_enabled",
                is_hidden="_is_pay_bail_hidden",
            )
        )
        action_set.add(
            Action(
                id="use_jail_card",
                label=Localization.get(locale, "monopoly-use-jail-card"),
                handler="_action_use_jail_card",
                is_enabled="_is_use_jail_card_enabled",
                is_hidden="_is_use_jail_card_hidden",
            )
        )

    def _add_turn_banking_actions(self, action_set: ActionSet, locale: str) -> None:
        action_set.add(
            Action(
                id="banking_balance",
                label=Localization.get(locale, "monopoly-banking-balance"),
                handler="_action_banking_balance",
                is_enabled="_is_banking_balance_enabled",
                is_hidden="_is_banking_balance_hidden",
            )
        )
        action_set.add(
            Action(
                id="banking_transfer",
                label=Localization.get(locale, "monopoly-banking-transfer"),
                handler="_action_banking_transfer",
                is_enabled="_is_banking_transfer_enabled",
                is_hidden="_is_banking_transfer_hidden",
                input_request=MenuInput(
                    prompt="monopoly-select-banking-transfer",
                    options="_options_for_banking_transfer",
                ),
            )
        )
        action_set.add(
            Action(
                id="banking_ledger",
                label=Localization.get(locale, "monopoly-banking-ledger"),
                handler="_action_banking_ledger",
                is_enabled="_is_banking_ledger_enabled",
                is_hidden="_is_banking_ledger_hidden",
            )
        )
        action_set.add(
            Action(
                id="voice_command",
                label=Localization.get(locale, "monopoly-voice-command"),
                handler="_action_voice_command",
                is_enabled="_is_voice_command_enabled",
                is_hidden="_is_voice_command_hidden",
                input_request=EditboxInput(
                    prompt="monopoly-select-voice-command",
                ),
            )
        )

    def _add_turn_end_actions(self, action_set: ActionSet, locale: str) -> None:
        action_set.add(
            Action(
                id="claim_cheat_reward",
                label=Localization.get(locale, "monopoly-cheaters-claim-reward"),
                handler="_action_claim_cheat_reward",
                is_enabled="_is_claim_cheat_reward_enabled",
                is_hidden="_is_claim_cheat_reward_hidden",
            )
        )
        action_set.add(
            Action(
                id="end_turn",
                label=Localization.get(locale, "monopoly-end-turn"),
                handler="_action_end_turn",
                is_enabled="_is_end_turn_enabled",
                is_hidden="_is_end_turn_hidden",
            )
        )

    def create_turn_action_set(self, player: MonopolyPlayer) -> ActionSet:
        """Create the turn action set for Monopoly."""
        user = self.get_user(player)
        locale = user.locale if user else "en"

        action_set = ActionSet(name="turn")
        self._add_turn_roll_and_purchase_actions(action_set, locale)
        self._add_turn_auction_actions(action_set, locale)
        self._add_turn_property_management_actions(action_set, locale)
        self._add_turn_trade_actions(action_set, locale)
        self._add_turn_jail_actions(action_set, locale)
        self._add_turn_banking_actions(action_set, locale)
        self._add_turn_end_actions(action_set, locale)
        return action_set

    def _define_roll_auction_property_keybinds(self) -> None:
        self.define_keybind("r", "Roll dice", ["roll_dice"], state=KeybindState.ACTIVE)
        self.define_keybind("b", "Buy property", ["buy_property"], state=KeybindState.ACTIVE)
        self.define_keybind("a", "Auction property", ["auction_property"], state=KeybindState.ACTIVE)
        self.define_keybind("shift+a", "Auction bid", ["auction_bid"], state=KeybindState.ACTIVE)
        self.define_keybind("ctrl+a", "Auction pass", ["auction_pass"], state=KeybindState.ACTIVE)

    def _define_property_trade_jail_keybinds(self) -> None:
        self.define_keybind("m", "Mortgage property", ["mortgage_property"], state=KeybindState.ACTIVE)
        self.define_keybind(
            "shift+m",
            "Unmortgage property",
            ["unmortgage_property"],
            state=KeybindState.ACTIVE,
        )
        self.define_keybind("h", "Build house", ["build_house"], state=KeybindState.ACTIVE)
        self.define_keybind("shift+h", "Sell house", ["sell_house"], state=KeybindState.ACTIVE)
        self.define_keybind("t", "Offer trade", ["offer_trade"], state=KeybindState.ACTIVE)
        self.define_keybind("shift+t", "Accept trade", ["accept_trade"], state=KeybindState.ACTIVE)
        self.define_keybind("ctrl+t", "Decline trade", ["decline_trade"], state=KeybindState.ACTIVE)
        self.define_keybind("j", "Pay bail", ["pay_bail"], state=KeybindState.ACTIVE)

    def _define_banking_and_voice_keybinds(self) -> None:
        self.define_keybind("ctrl+b", "Bank balance", ["banking_balance"], state=KeybindState.ACTIVE)
        self.define_keybind(
            "shift+b", "Bank transfer", ["banking_transfer"], state=KeybindState.ACTIVE
        )
        self.define_keybind("alt+b", "Bank ledger", ["banking_ledger"], state=KeybindState.ACTIVE)
        self.define_keybind("v", "Voice command", ["voice_command"], state=KeybindState.ACTIVE)
        self.define_keybind("e", "End turn", ["end_turn"], state=KeybindState.ACTIVE)

    def _define_preset_announcement_keybind(self) -> None:
        self.define_keybind(
            "p",
            "Announce current preset",
            ["announce_preset"],
            state=KeybindState.ACTIVE,
            include_spectators=True,
        )

    def setup_keybinds(self) -> None:
        """Define keybinds for lobby + scaffold status checks."""
        super().setup_keybinds()
        self._define_roll_auction_property_keybinds()
        self._define_property_trade_jail_keybinds()
        self._define_banking_and_voice_keybinds()
        self._define_preset_announcement_keybind()

    def _add_standard_monopoly_actions(self, action_set: ActionSet, locale: str) -> None:
        action_set.add(
            Action(
                id="announce_preset",
                label=Localization.get(locale, "monopoly-announce-preset"),
                handler="_action_announce_preset",
                is_enabled="_is_announce_preset_enabled",
                is_hidden="_is_announce_preset_hidden",
            )
        )

    def create_standard_action_set(self, player: MonopolyPlayer) -> ActionSet:
        """Add preset announcement action to standard action set."""
        action_set = super().create_standard_action_set(player)
        user = self.get_user(player)
        locale = user.locale if user else "en"
        self._add_standard_monopoly_actions(action_set, locale)
        return action_set

    def get_available_preset_ids(self) -> list[str]:
        """Return selectable preset ids from generated catalog artifacts."""
        preset_ids = list(_catalog_preset_ids())
        for preset_id in PRESET_LABEL_KEYS:
            if preset_id not in preset_ids:
                preset_ids.append(preset_id)
        return preset_ids

    def get_available_board_ids(self) -> list[str]:
        """Return selectable board ids from board profile registry."""
        return _board_profile_ids()

    def get_available_board_rules_modes(self) -> list[str]:
        """Return selectable board rules mode ids."""
        return _board_rules_modes()

    def _fallback_preset(self) -> MonopolyPreset:
        """Return a safe fallback preset if artifacts are missing."""
        fallback_id = _catalog_default_preset_id()
        fallback = _catalog_get_preset(fallback_id)
        if fallback:
            return fallback
        return MonopolyPreset(
            preset_id=DEFAULT_PRESET_ID,
            family_key="classic_and_themed_standard",
            name="Classic and Themed Standard",
            description="Fallback preset when catalog artifacts are unavailable.",
            anchor_edition_id="",
            edition_ids=(),
        )

    def _resolve_selected_preset(self) -> MonopolyPreset:
        """Resolve currently selected lobby preset, applying fallback when needed."""
        if is_junior_ruleset_preset(self.options.preset_id):
            junior_base = _catalog_get_preset("junior")
            base = junior_base or _catalog_get_preset(DEFAULT_PRESET_ID) or self._fallback_preset()
            ruleset = get_junior_ruleset(self.options.preset_id)
            alias_name = (
                "Monopoly Junior (Modern)"
                if self.options.preset_id == JUNIOR_MODERN_PRESET_ID
                else "Monopoly Junior (Legacy)"
            )
            return MonopolyPreset(
                preset_id=self.options.preset_id,
                family_key="junior",
                name=alias_name,
                description="Junior rules profile anchored to curated manual editions.",
                anchor_edition_id=ruleset.anchor_edition_id,
                edition_ids=tuple(base.edition_ids),
            )
        if self.options.preset_id in PRESET_LABEL_KEYS and not _catalog_get_preset(
            self.options.preset_id
        ):
            base = _catalog_get_preset(DEFAULT_PRESET_ID) or self._fallback_preset()
            alias_name = self.options.preset_id.replace("_", " ").title()
            if self.options.preset_id == "free_parking_jackpot":
                alias_name = "Free Parking Jackpot"
            return MonopolyPreset(
                preset_id=self.options.preset_id,
                family_key=base.family_key,
                name=alias_name,
                description="Classic rules profile for preset scaffolding.",
                anchor_edition_id=base.anchor_edition_id,
                edition_ids=tuple(base.edition_ids),
            )
        selected = _catalog_get_preset(self.options.preset_id)
        if selected:
            return selected
        fallback = self._fallback_preset()
        self.options.preset_id = fallback.preset_id
        return fallback

    def _resolve_rule_profile(self, preset_id: str) -> MonopolyRuleProfile:
        """Resolve gameplay rules for the selected preset."""
        return RULE_PROFILES.get(preset_id, RULE_PROFILES[DEFAULT_PRESET_ID])

    def _is_junior_preset(self) -> bool:
        """Return True when the active preset uses Junior ruleset flow."""
        return self.junior_ruleset is not None

    def _is_electronic_banking_preset(self) -> bool:
        """Return True when active preset uses simulator-backed banking."""
        return self.active_preset_id in {"electronic_banking", "voice_banking"}

    def _is_city_preset(self) -> bool:
        """Return True when active preset uses Monopoly City rules."""
        return self.active_preset_id == "city"

    def _sync_player_cash_from_banking(self, player: MonopolyPlayer) -> int:
        """Mirror simulator balance into player.cash for compatibility checks."""
        state = self.banking_state
        if not state or not self._is_electronic_banking_preset():
            return player.cash
        player.cash = bank_get_balance(state, player.id)
        return player.cash

    def _sync_all_player_cash_from_banking(self) -> None:
        """Mirror all simulator balances into players."""
        if not self._is_electronic_banking_preset() or not self.banking_state:
            return
        for player in self.players:
            if isinstance(player, MonopolyPlayer):
                self._sync_player_cash_from_banking(player)

    def _bank_balance(self, player: MonopolyPlayer) -> int:
        """Return simulator-backed balance when electronic banking is active."""
        if self._is_electronic_banking_preset() and self.banking_state:
            return bank_get_balance(self.banking_state, player.id)
        return player.cash

    def _current_liquid_balance(self, player: MonopolyPlayer) -> int:
        """Return current spendable balance for decision and validation logic."""
        return self._bank_balance(player)

    def _credit_player(self, player: MonopolyPlayer, amount: int, reason: str) -> int:
        """Credit player funds and return actual amount credited."""
        if amount <= 0:
            return 0
        if self._is_electronic_banking_preset() and self.banking_state:
            tx = bank_credit(self.banking_state, player.id, amount, reason)
            self._sync_player_cash_from_banking(player)
            if tx.status != "success":
                return 0
            return tx.amount
        player.cash += amount
        return amount

    def _debit_player_to_bank(
        self,
        player: MonopolyPlayer,
        amount: int,
        reason: str,
        *,
        allow_partial: bool = False,
    ) -> int:
        """Debit funds from a player to bank and return amount paid."""
        if amount <= 0:
            return 0
        if self._is_electronic_banking_preset() and self.banking_state:
            max_available = self._bank_balance(player)
            charge = min(amount, max_available) if allow_partial else amount
            if charge <= 0:
                bank_debit(self.banking_state, player.id, amount, reason, to_id=BANK_ACCOUNT_ID)
                return 0
            tx = bank_debit(self.banking_state, player.id, charge, reason, to_id=BANK_ACCOUNT_ID)
            self._sync_player_cash_from_banking(player)
            if tx.status != "success":
                return 0
            return tx.amount
        paid = min(player.cash, amount) if allow_partial else amount
        if not allow_partial and player.cash < amount:
            return 0
        player.cash -= paid
        return paid

    def _transfer_between_players(
        self,
        from_player: MonopolyPlayer,
        to_player: MonopolyPlayer,
        amount: int,
        reason: str,
        *,
        allow_partial: bool = False,
    ) -> int:
        """Transfer funds between players and return amount transferred."""
        if amount <= 0:
            return 0
        if self._is_electronic_banking_preset() and self.banking_state:
            max_available = self._bank_balance(from_player)
            transfer_amount = min(amount, max_available) if allow_partial else amount
            if transfer_amount <= 0:
                bank_transfer(self.banking_state, from_player.id, to_player.id, amount, reason)
                return 0
            tx = bank_transfer(
                self.banking_state,
                from_player.id,
                to_player.id,
                transfer_amount,
                reason,
            )
            self._sync_player_cash_from_banking(from_player)
            self._sync_player_cash_from_banking(to_player)
            if tx.status != "success":
                return 0
            return tx.amount

        paid = min(from_player.cash, amount) if allow_partial else amount
        if not allow_partial and from_player.cash < amount:
            return 0
        from_player.cash -= paid
        to_player.cash += paid
        return paid

    def _close_bank_account(
        self, player: MonopolyPlayer, *, creditor: MonopolyPlayer | None = None
    ) -> None:
        """Deactivate bankrupt player account in simulator mode."""
        if not self._is_electronic_banking_preset() or not self.banking_state:
            return
        account = self.banking_state.accounts.get(player.id)
        if account is None:
            return
        if account.balance > 0 and creditor and creditor.id != player.id:
            bank_transfer(
                self.banking_state,
                player.id,
                creditor.id,
                account.balance,
                "bankruptcy_settlement",
            )
            self._sync_player_cash_from_banking(creditor)
        elif account.balance > 0:
            bank_debit(
                self.banking_state,
                player.id,
                account.balance,
                "bankruptcy_settlement",
                to_id=BANK_ACCOUNT_ID,
            )
        account.is_active = False
        self._sync_player_cash_from_banking(player)

    def _localize_preset_name(self, locale: str, preset_id: str, fallback: str) -> str:
        """Resolve localized preset label for speech."""
        preset_key = PRESET_LABEL_KEYS.get(preset_id)
        if not preset_key:
            return fallback
        text = Localization.get(locale, preset_key)
        if text == preset_key:
            return fallback
        return text

    def _is_announce_preset_enabled(self, player: Player) -> str | None:
        """Enable preset announcements during active play."""
        return self.guard_game_active()

    def _is_announce_preset_hidden(self, player: Player) -> Visibility:
        """Hide announce action from menus (keybind only)."""
        return Visibility.HIDDEN

    def _action_announce_preset(self, player: Player, action_id: str) -> None:
        """Speak current preset details to one player."""
        user = self.get_user(player)
        if not user:
            return
        preset_name = self._localize_preset_name(
            user.locale, self.active_preset_id, self.active_preset_name
        )
        user.speak_l(
            "monopoly-current-preset",
            preset=preset_name,
            count=len(self.active_edition_ids),
        )

    def _build_space_from_manual_row(self, row: dict[str, object], fallback_index: int) -> MonopolySpace:
        """Build one MonopolySpace from a manual rule artifact row."""
        index = int(row.get("position", fallback_index))
        space_id = str(row.get("space_id", f"space_{index}"))
        name = str(row.get("name", space_id.replace("_", " ").title()))
        kind = str(row.get("kind", "property"))
        price = int(row.get("price", 0))
        rent = int(row.get("rent", 0))
        color_group = str(row.get("color_group", ""))
        house_cost = int(row.get("house_cost", 0))
        rents_raw = row.get("rents", ())
        rents: tuple[int, ...]
        if isinstance(rents_raw, list):
            rents = tuple(int(value) for value in rents_raw)
        else:
            rents = ()
        return MonopolySpace(
            index=index,
            space_id=space_id,
            name=name,
            kind=kind,
            price=price,
            rent=rent,
            color_group=color_group,
            house_cost=house_cost,
            rents=rents,
        )

    def _resolve_active_board_structures(
        self,
    ) -> tuple[list[MonopolySpace], dict[str, MonopolySpace], dict[str, list[str]]]:
        """Resolve active board maps from manual rule set when available."""
        if self.active_manual_rule_set is None:
            return (
                CLASSIC_STANDARD_BOARD.copy(),
                SPACE_BY_ID.copy(),
                {key: values.copy() for key, values in COLOR_GROUP_TO_SPACE_IDS.items()},
            )

        board_payload = self.active_manual_rule_set.board
        spaces_payload = board_payload.get("spaces", [])
        if not isinstance(spaces_payload, list):
            spaces_payload = []

        spaces: list[MonopolySpace] = []
        for idx, row in enumerate(spaces_payload):
            if not isinstance(row, dict):
                continue
            spaces.append(self._build_space_from_manual_row(row, idx))

        if not spaces:
            return (
                CLASSIC_STANDARD_BOARD.copy(),
                SPACE_BY_ID.copy(),
                {key: values.copy() for key, values in COLOR_GROUP_TO_SPACE_IDS.items()},
            )

        spaces.sort(key=lambda space: space.index)
        space_by_id = {space.space_id: space for space in spaces}
        color_groups: dict[str, list[str]] = {}
        for space in spaces:
            if not self._is_street_property(space):
                continue
            color_groups.setdefault(space.color_group, []).append(space.space_id)
        return spaces, space_by_id, color_groups

    def _manual_deck_ids(self, deck_type: str) -> list[str]:
        """Return ordered manual deck ids for one deck type when available."""
        if self.active_manual_rule_set is None:
            return []
        cards_payload = self.active_manual_rule_set.cards
        deck_rows = cards_payload.get(deck_type, [])
        if not isinstance(deck_rows, list):
            return []
        deck_ids: list[str] = []
        for row in deck_rows:
            if not isinstance(row, dict):
                continue
            card_id = row.get("id")
            if not isinstance(card_id, str):
                continue
            if not card_id:
                continue
            deck_ids.append(card_id)
        return deck_ids

    def _manual_card_definition(self, deck_type: str, card_id: str) -> dict[str, object] | None:
        """Resolve one manual card definition by deck type and id."""
        if self.active_manual_rule_set is None:
            return None
        cards_payload = self.active_manual_rule_set.cards
        deck_rows = cards_payload.get(deck_type, [])
        if not isinstance(deck_rows, list):
            return None
        for row in deck_rows:
            if not isinstance(row, dict):
                continue
            row_id = row.get("id")
            if isinstance(row_id, str) and row_id == card_id:
                return row
        return None

    def _apply_manual_card_effect(
        self,
        player: MonopolyPlayer,
        effect_spec: dict[str, object],
        *,
        depth: int,
        dice_total: int | None,
    ) -> str | None:
        """Apply one manual card effect spec and return resolution state when handled."""
        effect_type = effect_spec.get("type")
        if not isinstance(effect_type, str):
            return None

        if effect_type == "credit":
            amount = max(0, int(effect_spec.get("amount", 0)))
            credited = self._credit_player(player, amount, "manual_card_credit")
            self.broadcast_l(
                "monopoly-card-collect",
                player=player.name,
                amount=credited,
                cash=player.cash,
            )
            return "resolved"

        if effect_type == "debit":
            amount = max(0, int(effect_spec.get("amount", 0)))
            if not self._apply_bank_payment(player, amount, card_reason_key="monopoly-card-pay"):
                return "bankrupt"
            return "resolved"

        if effect_type == "go_to_jail":
            self._send_to_jail(player)
            return "forced_end"

        if effect_type == "move_relative":
            steps = int(effect_spec.get("steps", 0))
            collect_pass_go = bool(effect_spec.get("collect_pass_go", steps > 0))
            landed_space = self._move_player(player, steps, collect_pass_go=collect_pass_go)
            return self._resolve_space(player, landed_space, depth=depth + 1, dice_total=dice_total)

        if effect_type == "move_absolute":
            destination = int(effect_spec.get("position", player.position))
            old_position = player.position
            player.position = destination % self.active_board_size
            collect_pass_go = bool(effect_spec.get("collect_pass_go", False))
            if collect_pass_go and player.position < old_position:
                pass_go_cash = max(0, self.rule_profile.pass_go_cash)
                credited = self._credit_player(player, pass_go_cash, "manual_card_move_absolute_pass_go")
                self.broadcast_l(
                    "monopoly-pass-go",
                    player=player.name,
                    amount=credited,
                    cash=player.cash,
                )
            landed_space = self._space_at(player.position)
            return self._resolve_space(player, landed_space, depth=depth + 1, dice_total=dice_total)

        if effect_type in {"grant_jail_free", "get_out_of_jail_free"}:
            return self._grant_get_out_of_jail_card(player)

        return None

    def _grant_get_out_of_jail_card(self, player: MonopolyPlayer) -> str:
        """Grant one get-out-of-jail card using classic Monopoly behavior."""
        if self._is_junior_preset():
            credited = self._credit_player(player, 1, "community_chest_junior_bonus")
            self.broadcast_l(
                "monopoly-card-collect",
                player=player.name,
                amount=credited,
                cash=player.cash,
            )
            return "resolved"
        player.get_out_of_jail_cards += 1
        self.broadcast_l(
            "monopoly-card-jail-free",
            player=player.name,
            cards=player.get_out_of_jail_cards,
        )
        return "resolved"

    def _space_at(self, position: int) -> MonopolySpace:
        """Get board space by board index."""
        return self.active_board_spaces[position % self.active_board_size]

    def _space_label(self, space_id: str) -> str:
        """Return display label for a space id."""
        space = self.active_space_by_id.get(space_id)
        return space.name if space else space_id

    def _mortgage_value(self, space: MonopolySpace) -> int:
        """Get mortgage value for a space."""
        return max(1, space.price // 2)

    def _unmortgage_cost(self, space: MonopolySpace) -> int:
        """Get unmortgage cost for a space."""
        mortgage_value = self._mortgage_value(space)
        return (mortgage_value * 11 + 9) // 10

    def _is_space_mortgaged(self, space_id: str) -> bool:
        """Check whether a space is currently mortgaged."""
        return space_id in self.mortgaged_space_ids

    def _building_level(self, space_id: str) -> int:
        """Get building level for a street property (0-5)."""
        return self.building_levels.get(space_id, 0)

    def _set_building_level(self, space_id: str, level: int) -> None:
        """Set building level for a street property (0-5)."""
        if space_id not in self.active_space_by_id:
            return
        clamped = max(0, min(5, level))
        self.building_levels[space_id] = clamped

    def _is_street_property(self, space: MonopolySpace) -> bool:
        """Return True for color-group street properties."""
        return space.kind == "property" and bool(space.color_group)

    def _owner_has_full_color_set(self, owner_id: str, color_group: str) -> bool:
        """Check whether owner controls an entire color set."""
        group_ids = self.active_color_group_to_space_ids.get(color_group, [])
        if not group_ids:
            return False
        return all(self.property_owners.get(space_id) == owner_id for space_id in group_ids)

    def _group_space_ids(self, color_group: str) -> list[str]:
        """Get all board space ids in one color group."""
        return self.active_color_group_to_space_ids.get(color_group, [])

    def _group_levels(self, color_group: str, owner_id: str | None = None) -> list[int]:
        """Get building levels for one color group, optionally filtered by owner."""
        levels: list[int] = []
        for space_id in self._group_space_ids(color_group):
            if owner_id is not None and self.property_owners.get(space_id) != owner_id:
                continue
            levels.append(self._building_level(space_id))
        return levels

    def _group_has_mortgage(self, color_group: str, owner_id: str | None = None) -> bool:
        """Return True if any matching property in the group is mortgaged."""
        return any(
            space_id in self.mortgaged_space_ids
            and (owner_id is None or self.property_owners.get(space_id) == owner_id)
            for space_id in self._group_space_ids(color_group)
        )

    def _group_has_any_buildings(self, color_group: str) -> bool:
        """Return True if any property in the group has buildings."""
        return any(self._building_level(space_id) > 0 for space_id in self._group_space_ids(color_group))

    def _building_supply_in_use(self) -> tuple[int, int]:
        """Return (houses_in_use, hotels_in_use) from board state."""
        houses = 0
        hotels = 0
        for level in self.building_levels.values():
            if level >= 5:
                hotels += 1
            else:
                houses += max(0, level)
        return houses, hotels

    def _available_houses(self) -> int:
        """Return houses currently available in bank supply."""
        houses_in_use, _ = self._building_supply_in_use()
        return max(0, TOTAL_HOUSES - houses_in_use)

    def _available_hotels(self) -> int:
        """Return hotels currently available in bank supply."""
        _, hotels_in_use = self._building_supply_in_use()
        return max(0, TOTAL_HOTELS - hotels_in_use)

    def _can_raise_building_level(self, space_id: str) -> bool:
        """Check supply constraints for +1 building level."""
        level = self._building_level(space_id)
        if level < 0 or level >= 5:
            return False
        if level <= 3:
            return self._available_houses() >= 1
        return self._available_hotels() >= 1

    def _can_lower_building_level(self, space_id: str) -> bool:
        """Check supply constraints for -1 building level."""
        level = self._building_level(space_id)
        if level <= 0:
            return False
        if level <= 4:
            return True
        return self._available_houses() >= 4

    def _pick_best_building_sale(self, space_ids: list[str]) -> str | None:
        """Pick the sale that usually raises cash fastest."""
        if not space_ids:
            return None
        ranked = sorted(
            space_ids,
            key=lambda space_id: (
                self.active_space_by_id[space_id].house_cost,
                self._building_level(space_id),
                self._space_label(space_id),
            ),
            reverse=True,
        )
        return ranked[0]

    def _pick_best_mortgage(self, space_ids: list[str]) -> str | None:
        """Pick the mortgage that usually raises cash fastest."""
        if not space_ids:
            return None
        ranked = sorted(
            space_ids,
            key=lambda space_id: (
                self._mortgage_value(self.active_space_by_id[space_id]),
                self.active_space_by_id[space_id].price,
                self._space_label(space_id),
            ),
            reverse=True,
        )
        return ranked[0]

    def _liquidate_assets_for_debt(self, player: MonopolyPlayer, amount_due: int) -> None:
        """Auto-liquidate: sell buildings first, then mortgage, until debt is covered."""
        if amount_due <= 0 or self._current_liquid_balance(player) >= amount_due:
            return

        attempts = 0
        max_attempts = max(8, len(player.owned_space_ids) * 8)
        while self._current_liquid_balance(player) < amount_due and attempts < max_attempts:
            attempts += 1

            sell_choice = self._pick_best_building_sale(self._options_for_sell_house(player))
            if sell_choice:
                cash_before = self._current_liquid_balance(player)
                self._action_sell_house(player, sell_choice, "sell_house")
                if self._current_liquid_balance(player) > cash_before:
                    continue

            mortgage_choice = self._pick_best_mortgage(self._options_for_mortgage_property(player))
            if mortgage_choice:
                cash_before = self._current_liquid_balance(player)
                self._action_mortgage_property(player, mortgage_choice, "mortgage_property")
                if self._current_liquid_balance(player) > cash_before:
                    continue

            break

    def _property_trade_value(self, space_id: str) -> int:
        """Estimate trade value for a property."""
        space = self.active_space_by_id.get(space_id)
        if not space:
            return 100
        return max(1, space.price)

    def _is_property_tradable_for_trade(self, space_id: str, owner_id: str) -> bool:
        """Return True when a property can be traded in a private deal."""
        if self.property_owners.get(space_id) != owner_id:
            return False
        space = self.active_space_by_id.get(space_id)
        if not space or space.kind not in PURCHASABLE_KINDS:
            return False
        if self._is_street_property(space) and self._group_has_any_buildings(space.color_group):
            return False
        return True

    def _transfer_property(
        self,
        space_id: str,
        from_player: MonopolyPlayer,
        to_player: MonopolyPlayer,
    ) -> bool:
        """Transfer one property between players."""
        if not self._is_property_tradable_for_trade(space_id, from_player.id):
            return False
        self.property_owners[space_id] = to_player.id
        if space_id in from_player.owned_space_ids:
            from_player.owned_space_ids.remove(space_id)
        if space_id not in to_player.owned_space_ids:
            to_player.owned_space_ids.append(space_id)
        return True

    def _encode_trade_option(self, summary: str, offer: MonopolyTradeOffer) -> str:
        """Encode trade metadata into one menu option string."""
        return (
            f"{summary} ## target={offer.target_id};gc={offer.give_cash};"
            f"gp={offer.give_property_id or '-'};gj={offer.give_jail_cards};"
            f"rc={offer.receive_cash};rp={offer.receive_property_id or '-'};"
            f"rj={offer.receive_jail_cards}"
        )

    def _parse_trade_option(self, option: str) -> MonopolyTradeOffer | None:
        """Parse a trade option string from the menu."""
        if "##" not in option:
            return None
        summary, raw_meta = option.split("##", 1)
        meta: dict[str, str] = {}
        for part in raw_meta.strip().split(";"):
            if "=" not in part:
                continue
            key, value = part.split("=", 1)
            meta[key.strip()] = value.strip()

        target_id = meta.get("target", "")
        if not target_id:
            return None
        try:
            give_cash = max(0, int(meta.get("gc", "0")))
            give_jail_cards = max(0, int(meta.get("gj", "0")))
            receive_cash = max(0, int(meta.get("rc", "0")))
            receive_jail_cards = max(0, int(meta.get("rj", "0")))
        except ValueError:
            return None

        give_property_id = meta.get("gp", "")
        if give_property_id == "-":
            give_property_id = ""
        receive_property_id = meta.get("rp", "")
        if receive_property_id == "-":
            receive_property_id = ""

        return MonopolyTradeOffer(
            target_id=target_id,
            give_cash=give_cash,
            give_property_id=give_property_id,
            give_jail_cards=give_jail_cards,
            receive_cash=receive_cash,
            receive_property_id=receive_property_id,
            receive_jail_cards=receive_jail_cards,
            summary=summary.strip(),
        )

    def _is_trade_offer_valid(
        self,
        proposer: MonopolyPlayer,
        target: MonopolyPlayer,
        offer: MonopolyTradeOffer,
    ) -> bool:
        """Validate that both sides can still perform an offered trade."""
        if proposer.bankrupt or target.bankrupt:
            return False
        if offer.target_id != target.id:
            return False
        if offer.give_cash < 0 or offer.receive_cash < 0:
            return False
        if offer.give_jail_cards < 0 or offer.receive_jail_cards < 0:
            return False

        proposer_gives_any = bool(
            offer.give_cash > 0 or offer.give_property_id or offer.give_jail_cards > 0
        )
        proposer_gets_any = bool(
            offer.receive_cash > 0 or offer.receive_property_id or offer.receive_jail_cards > 0
        )
        if not proposer_gives_any or not proposer_gets_any:
            return False

        if self._current_liquid_balance(proposer) < offer.give_cash:
            return False
        if self._current_liquid_balance(target) < offer.receive_cash:
            return False
        if proposer.get_out_of_jail_cards < offer.give_jail_cards:
            return False
        if target.get_out_of_jail_cards < offer.receive_jail_cards:
            return False

        if offer.give_property_id and not self._is_property_tradable_for_trade(
            offer.give_property_id, proposer.id
        ):
            return False
        if offer.receive_property_id and not self._is_property_tradable_for_trade(
            offer.receive_property_id, target.id
        ):
            return False
        return True

    def _apply_trade_offer(
        self,
        proposer: MonopolyPlayer,
        target: MonopolyPlayer,
        offer: MonopolyTradeOffer,
    ) -> bool:
        """Apply a validated trade offer."""
        if not self._is_trade_offer_valid(proposer, target, offer):
            return False

        if offer.give_property_id and not self._transfer_property(offer.give_property_id, proposer, target):
            return False
        if offer.receive_property_id and not self._transfer_property(
            offer.receive_property_id, target, proposer
        ):
            return False

        if offer.give_cash > 0 and (
            self._transfer_between_players(
                proposer,
                target,
                offer.give_cash,
                "trade_cash",
            )
            != offer.give_cash
        ):
            return False
        if offer.receive_cash > 0 and (
            self._transfer_between_players(
                target,
                proposer,
                offer.receive_cash,
                "trade_cash",
            )
            != offer.receive_cash
        ):
            return False

        proposer.get_out_of_jail_cards -= offer.give_jail_cards
        target.get_out_of_jail_cards += offer.give_jail_cards

        target.get_out_of_jail_cards -= offer.receive_jail_cards
        proposer.get_out_of_jail_cards += offer.receive_jail_cards
        return True

    def _bot_accepts_trade_offer(
        self,
        proposer: MonopolyPlayer,
        target: MonopolyPlayer,
        offer: MonopolyTradeOffer,
    ) -> bool:
        """Simple heuristic for bot trade acceptance."""
        if not self._is_trade_offer_valid(proposer, target, offer):
            return False

        target_gain = (
            offer.give_cash
            + (self._property_trade_value(offer.give_property_id) if offer.give_property_id else 0)
            + (offer.give_jail_cards * JAIL_CARD_TRADE_CASH)
        )
        target_cost = (
            offer.receive_cash
            + (self._property_trade_value(offer.receive_property_id) if offer.receive_property_id else 0)
            + (offer.receive_jail_cards * JAIL_CARD_TRADE_CASH)
        )
        return target_gain >= target_cost

    def _pending_trade_for_target(self, player: MonopolyPlayer) -> MonopolyTradeOffer | None:
        """Return pending trade offer when player is the offer target."""
        offer = self.pending_trade_offer
        if not offer or offer.target_id != player.id:
            return None
        return offer

    def _pending_trade_for_proposer(self, player: MonopolyPlayer) -> MonopolyTradeOffer | None:
        """Return pending trade offer when player is the offer proposer."""
        offer = self.pending_trade_offer
        if not offer or offer.proposer_id != player.id:
            return None
        return offer

    def _append_trade_offer_option(
        self,
        options: list[str],
        summary: str,
        offer: MonopolyTradeOffer,
    ) -> None:
        """Encode and append one trade option."""
        options.append(self._encode_trade_option(summary, offer))

    def _trade_price_points(self, base_price: int) -> list[int]:
        """Return canonical low/base/high pricing points for trade menus."""
        return sorted({max(1, base_price // 2), base_price, base_price + 100})

    def _tradable_properties_for_player(self, player: MonopolyPlayer) -> list[str]:
        """Return sorted tradable property ids currently owned by player."""
        return sorted(
            [
                space_id
                for space_id in player.owned_space_ids
                if self._is_property_tradable_for_trade(space_id, player.id)
            ]
        )

    def _append_buy_property_trade_offers(
        self,
        options: list[str],
        target: MonopolyPlayer,
        proposer_cash: int,
        target_props: list[str],
    ) -> None:
        """Add cash-for-property purchase offers where proposer buys from target."""
        for space_id in target_props:
            price = self._property_trade_value(space_id)
            if proposer_cash < price:
                continue
            summary = f"Buy {self._space_label(space_id)} from {target.name} for {price}"
            offer = MonopolyTradeOffer(
                target_id=target.id,
                give_cash=price,
                receive_property_id=space_id,
                summary=summary,
            )
            self._append_trade_offer_option(options, summary, offer)

            for bid in self._trade_price_points(price):
                if bid <= 0 or bid > proposer_cash:
                    continue
                custom_summary = f"Offer {bid} to {target.name} for {self._space_label(space_id)}"
                custom_offer = MonopolyTradeOffer(
                    target_id=target.id,
                    give_cash=bid,
                    receive_property_id=space_id,
                    summary=custom_summary,
                )
                self._append_trade_offer_option(options, custom_summary, custom_offer)

    def _append_sell_property_trade_offers(
        self,
        options: list[str],
        target: MonopolyPlayer,
        target_cash: int,
        proposer_props: list[str],
    ) -> None:
        """Add property-for-cash sale offers where proposer sells to target."""
        for space_id in proposer_props:
            price = self._property_trade_value(space_id)
            if target_cash < price:
                continue
            summary = f"Sell {self._space_label(space_id)} to {target.name} for {price}"
            offer = MonopolyTradeOffer(
                target_id=target.id,
                give_property_id=space_id,
                receive_cash=price,
                summary=summary,
            )
            self._append_trade_offer_option(options, summary, offer)

            for ask in self._trade_price_points(price):
                if ask <= 0 or ask > target_cash:
                    continue
                custom_summary = f"Offer {self._space_label(space_id)} to {target.name} for {ask}"
                custom_offer = MonopolyTradeOffer(
                    target_id=target.id,
                    give_property_id=space_id,
                    receive_cash=ask,
                    summary=custom_summary,
                )
                self._append_trade_offer_option(options, custom_summary, custom_offer)

    def _append_swap_trade_offers(
        self,
        options: list[str],
        target: MonopolyPlayer,
        proposer_cash: int,
        target_cash: int,
        proposer_props: list[str],
        target_props: list[str],
    ) -> None:
        """Add property swap offers with optional balancing cash."""
        for give_space_id in proposer_props:
            give_value = self._property_trade_value(give_space_id)
            give_label = self._space_label(give_space_id)
            for receive_space_id in target_props:
                receive_value = self._property_trade_value(receive_space_id)
                receive_label = self._space_label(receive_space_id)

                swap_summary = f"Swap {give_label} with {target.name} for {receive_label}"
                swap_offer = MonopolyTradeOffer(
                    target_id=target.id,
                    give_property_id=give_space_id,
                    receive_property_id=receive_space_id,
                    summary=swap_summary,
                )
                self._append_trade_offer_option(options, swap_summary, swap_offer)

                diff = receive_value - give_value
                if diff > 0 and proposer_cash >= diff:
                    plus_cash_summary = (
                        f"Swap {give_label} + {diff} with {target.name} for {receive_label}"
                    )
                    plus_cash_offer = MonopolyTradeOffer(
                        target_id=target.id,
                        give_cash=diff,
                        give_property_id=give_space_id,
                        receive_property_id=receive_space_id,
                        summary=plus_cash_summary,
                    )
                    self._append_trade_offer_option(options, plus_cash_summary, plus_cash_offer)
                elif diff < 0 and target_cash >= abs(diff):
                    plus_cash_summary = (
                        f"Swap {give_label} for {receive_label} + {abs(diff)} from {target.name}"
                    )
                    plus_cash_offer = MonopolyTradeOffer(
                        target_id=target.id,
                        give_property_id=give_space_id,
                        receive_cash=abs(diff),
                        receive_property_id=receive_space_id,
                        summary=plus_cash_summary,
                    )
                    self._append_trade_offer_option(options, plus_cash_summary, plus_cash_offer)

    def _append_jail_card_trade_offers(
        self,
        options: list[str],
        proposer: MonopolyPlayer,
        target: MonopolyPlayer,
        proposer_cash: int,
        target_cash: int,
    ) -> None:
        """Add cash-for-jail-card buy/sell offers."""
        if target.get_out_of_jail_cards > 0 and proposer_cash >= JAIL_CARD_TRADE_CASH:
            for price in sorted({JAIL_CARD_TRADE_CASH, JAIL_CARD_TRADE_CASH * 2}):
                if price > proposer_cash:
                    continue
                summary = f"Buy jail card from {target.name} for {price}"
                offer = MonopolyTradeOffer(
                    target_id=target.id,
                    give_cash=price,
                    receive_jail_cards=1,
                    summary=summary,
                )
                self._append_trade_offer_option(options, summary, offer)
        if proposer.get_out_of_jail_cards > 0 and target_cash >= JAIL_CARD_TRADE_CASH:
            for price in sorted({JAIL_CARD_TRADE_CASH, JAIL_CARD_TRADE_CASH * 2}):
                if price > target_cash:
                    continue
                summary = f"Sell jail card to {target.name} for {price}"
                offer = MonopolyTradeOffer(
                    target_id=target.id,
                    give_jail_cards=1,
                    receive_cash=price,
                    summary=summary,
                )
                self._append_trade_offer_option(options, summary, offer)

    def _append_trade_offers_for_target(
        self,
        options: list[str],
        proposer: MonopolyPlayer,
        target: MonopolyPlayer,
        proposer_props: list[str],
    ) -> None:
        """Add all canonical trade offer variants against one target player."""
        proposer_cash = self._current_liquid_balance(proposer)
        target_cash = self._current_liquid_balance(target)
        target_props = self._tradable_properties_for_player(target)
        self._append_buy_property_trade_offers(
            options,
            target,
            proposer_cash,
            target_props,
        )
        self._append_sell_property_trade_offers(
            options,
            target,
            target_cash,
            proposer_props,
        )
        self._append_swap_trade_offers(
            options,
            target,
            proposer_cash,
            target_cash,
            proposer_props,
            target_props,
        )
        self._append_jail_card_trade_offers(
            options,
            proposer,
            target,
            proposer_cash,
            target_cash,
        )

    def _options_for_offer_trade(self, player: Player) -> list[str]:
        """Menu options for private trades from current player to others."""
        mono_player: MonopolyPlayer = player  # type: ignore
        if self._is_junior_preset():
            return []
        options: list[str] = []

        other_players = [
            p
            for p in self.turn_players
            if isinstance(p, MonopolyPlayer) and p.id != mono_player.id and not p.bankrupt
        ]
        proposer_props = self._tradable_properties_for_player(mono_player)
        for other in other_players:
            self._append_trade_offers_for_target(
                options,
                mono_player,
                other,
                proposer_props,
            )

        # Keep list stable and reasonably sized for menu navigation.
        deduped = sorted(dict.fromkeys(options))
        return deduped[:220]

    def _bot_select_mortgage_property(
        self, player: MonopolyPlayer, options: list[str]
    ) -> str | None:
        """Pick the mortgage option that raises the most cash."""
        return action_options.bot_select_mortgage_property(self, player, options)

    def _bot_select_unmortgage_property(
        self, player: MonopolyPlayer, options: list[str]
    ) -> str | None:
        """Pick the cheapest affordable unmortgage option."""
        return action_options.bot_select_unmortgage_property(self, player, options)

    def _bot_select_build_house(
        self, player: MonopolyPlayer, options: list[str]
    ) -> str | None:
        """Pick the build option with strongest rent gain for cost."""
        return action_options.bot_select_build_house(self, player, options)

    def _count_owned_kind(self, owner_id: str, kind: str) -> int:
        """Count how many properties of a kind the owner controls."""
        total = 0
        for space_id, space_owner_id in self.property_owners.items():
            if space_owner_id != owner_id:
                continue
            space = self.active_space_by_id.get(space_id)
            if space and space.kind == kind:
                total += 1
        return total

    def _calculate_junior_rent_due(
        self, space: MonopolySpace, owner_id: str, dice_total: int | None
    ) -> int:
        """Compute Junior rent using active ruleset profile."""
        ruleset = self.junior_ruleset
        if ruleset is None:
            return max(0, space.rent)

        if ruleset.rent_mode == "modern_tier":
            if self._is_street_property(space):
                base = max(1, space.rent)
                if self._owner_has_full_color_set(owner_id, space.color_group):
                    return base + 1
                return base
            if space.kind == "railroad":
                return max(2, 2 * self._count_owned_kind(owner_id, "railroad"))
            if space.kind == "utility":
                roll_value = dice_total if dice_total is not None else sum(self.turn_last_roll)
                return max(2, max(1, roll_value // 2))
            return max(1, space.rent)

        if self._is_street_property(space):
            if space.rents:
                base = space.rents[0]
            else:
                base = space.rent
            if self._owner_has_full_color_set(owner_id, space.color_group):
                return base * 2
            return base

        if space.kind == "railroad":
            owned = max(1, self._count_owned_kind(owner_id, "railroad"))
            return 5 * owned

        if space.kind == "utility":
            owned = max(1, self._count_owned_kind(owner_id, "utility"))
            roll_value = dice_total if dice_total is not None else sum(self.turn_last_roll)
            return max(2, owned * max(1, roll_value // 2))

        return max(1, space.rent)

    def _calculate_rent_due(
        self, space: MonopolySpace, owner_id: str, dice_total: int | None
    ) -> int:
        """Compute official-ish rent for a landed space."""
        if self._is_junior_preset():
            return self._calculate_junior_rent_due(space, owner_id, dice_total)
        if self._is_street_property(space):
            level = self._building_level(space.space_id)
            if space.rents:
                if level > 0:
                    return space.rents[min(level, len(space.rents) - 1)]
                base = space.rents[0]
            else:
                base = space.rent
            if self._owner_has_full_color_set(owner_id, space.color_group):
                return base * 2
            return base

        if space.kind == "railroad":
            owned = max(1, self._count_owned_kind(owner_id, "railroad"))
            return 25 * (2 ** (owned - 1))

        if space.kind == "utility":
            owned = max(1, self._count_owned_kind(owner_id, "utility"))
            factor = 10 if owned >= 2 else 4
            roll_value = dice_total if dice_total is not None else sum(self.turn_last_roll)
            return factor * max(0, roll_value)

        return space.rent

    def _pending_purchase_space(self) -> MonopolySpace | None:
        """Get the currently pending purchasable space for this turn."""
        if not self.turn_pending_purchase_space_id:
            return None
        return self.active_space_by_id.get(self.turn_pending_purchase_space_id)

    def _pending_auction_space(self) -> MonopolySpace | None:
        """Get active auction space when an interactive auction is running."""
        if not self.pending_auction_space_id:
            return None
        return self.active_space_by_id.get(self.pending_auction_space_id)

    def _is_auction_active(self) -> bool:
        """Return True when an interactive property auction is running."""
        return bool(self.pending_auction_space_id and self.pending_auction_bidder_ids)

    def _clear_pending_auction(self) -> None:
        """Clear transient interactive auction state."""
        self.pending_auction_space_id = ""
        self.pending_auction_bidder_ids.clear()
        self.pending_auction_turn_index = 0
        self.pending_auction_high_bidder_id = ""
        self.pending_auction_current_bid = 0

    def _current_auction_bidder(self) -> MonopolyPlayer | None:
        """Return the player whose turn it is in the interactive auction."""
        if not self._is_auction_active():
            return None
        bidder_ids = self.pending_auction_bidder_ids
        if not bidder_ids:
            return None
        bidder_id = bidder_ids[self.pending_auction_turn_index % len(bidder_ids)]
        bidder = self.get_player_by_id(bidder_id)
        if bidder and isinstance(bidder, MonopolyPlayer) and not bidder.bankrupt:
            return bidder
        return None

    def _auction_bidders_in_turn_order(self, declined_by: MonopolyPlayer) -> list[MonopolyPlayer]:
        """Get eligible auction bidders in order starting after the declining player."""
        ordered_players = [p for p in self.turn_players if isinstance(p, MonopolyPlayer)]
        if not ordered_players:
            return []
        try:
            start_index = ordered_players.index(declined_by)
        except ValueError:
            start_index = 0

        rotated = ordered_players[start_index + 1 :] + ordered_players[: start_index + 1]
        bidders: list[MonopolyPlayer] = []
        for bidder in rotated:
            if bidder.bankrupt:
                continue
            if self._current_liquid_balance(bidder) < MIN_AUCTION_INCREMENT:
                continue
            bidders.append(bidder)
        return bidders

    def _auction_min_bid(self) -> int:
        """Return minimum legal next bid for the active interactive auction."""
        return max(MIN_AUCTION_INCREMENT, self.pending_auction_current_bid + MIN_AUCTION_INCREMENT)

    def _next_auction_turn_index(self, start_index: int) -> int | None:
        """Find next bidder index after start_index, skipping high bidder when possible."""
        bidder_ids = self.pending_auction_bidder_ids
        if not bidder_ids:
            return None
        high_bidder_id = self.pending_auction_high_bidder_id
        for offset in range(1, len(bidder_ids) + 1):
            idx = (start_index + offset) % len(bidder_ids)
            if (
                high_bidder_id
                and len(bidder_ids) > 1
                and bidder_ids[idx] == high_bidder_id
            ):
                continue
            return idx
        return None

    def _advance_pending_auction_turn(self, start_index: int) -> None:
        """Advance interactive auction to the next bidder or resolve winner."""
        if not self._is_auction_active():
            return
        bidder_ids = self.pending_auction_bidder_ids
        if not bidder_ids:
            self._finish_pending_auction()
            return
        if (
            len(bidder_ids) == 1
            and self.pending_auction_high_bidder_id
            and bidder_ids[0] == self.pending_auction_high_bidder_id
        ):
            self._finish_pending_auction(
                winner_id=self.pending_auction_high_bidder_id,
                winning_bid=self.pending_auction_current_bid,
            )
            return

        next_index = self._next_auction_turn_index(start_index)
        if next_index is None:
            winner_id = self.pending_auction_high_bidder_id or None
            winning_bid = self.pending_auction_current_bid
            self._finish_pending_auction(winner_id=winner_id, winning_bid=winning_bid)
            return

        self.pending_auction_turn_index = next_index
        bidder = self._current_auction_bidder()
        space = self._pending_auction_space()
        if bidder and space:
            self.broadcast_l(
                "monopoly-auction-turn",
                player=bidder.name,
                property=space.name,
                amount=self.pending_auction_current_bid,
            )
            if bidder.is_bot:
                BotHelper.jolt_bot(bidder, ticks=random.randint(8, 14))

    def _complete_auction_sale(
        self, space: MonopolySpace, winner: MonopolyPlayer, winning_bid: int
    ) -> None:
        """Transfer auctioned property to winner and announce outcome."""
        bid = max(1, min(self._current_liquid_balance(winner), winning_bid))
        paid = self._debit_player_to_bank(winner, bid, f"auction:{space.space_id}")
        if paid <= 0:
            return
        if space.space_id not in winner.owned_space_ids:
            winner.owned_space_ids.append(space.space_id)
        self.property_owners[space.space_id] = winner.id
        if space.space_id in self.mortgaged_space_ids:
            self.mortgaged_space_ids.remove(space.space_id)

        self.broadcast_l(
            "monopoly-auction-won",
            player=winner.name,
            property=space.name,
            amount=paid,
            cash=winner.cash,
        )
        self._award_builder_blocks(winner)

    def _finish_pending_auction(
        self,
        *,
        winner_id: str | None = None,
        winning_bid: int = 0,
    ) -> None:
        """Resolve and clear the active interactive auction state."""
        space = self._pending_auction_space()
        self._clear_pending_auction()
        self.turn_pending_purchase_space_id = ""

        winner: MonopolyPlayer | None = None
        if winner_id and space:
            maybe_winner = self.get_player_by_id(winner_id)
            if (
                maybe_winner
                and isinstance(maybe_winner, MonopolyPlayer)
                and not maybe_winner.bankrupt
                and self._current_liquid_balance(maybe_winner) > 0
            ):
                winner = maybe_winner

        if winner and space and winning_bid > 0:
            self._complete_auction_sale(space, winner, winning_bid)
        elif space:
            self.broadcast_l("monopoly-auction-no-bids", property=space.name)

        current = self.current_player
        if (
            self.turn_can_roll_again
            and current
            and isinstance(current, MonopolyPlayer)
            and not current.bankrupt
        ):
            self._prepare_next_roll_after_doubles(current)

        self._sync_cash_scores()
        self.rebuild_all_menus()

    def _start_property_auction(self, space: MonopolySpace, declined_by: MonopolyPlayer) -> None:
        """Start an interactive auction for a pending unpurchased property."""
        bidders = self._auction_bidders_in_turn_order(declined_by)
        if not bidders:
            self.broadcast_l("monopoly-auction-no-bids", property=space.name)
            self.turn_pending_purchase_space_id = ""
            if self.turn_can_roll_again and not declined_by.bankrupt:
                self._prepare_next_roll_after_doubles(declined_by)
            self._sync_cash_scores()
            self.rebuild_all_menus()
            return

        if len(bidders) == 1:
            winner = bidders[0]
            reserve = max(1, space.price // 2)
            winning_bid = min(self._current_liquid_balance(winner), reserve)
            self.turn_pending_purchase_space_id = ""
            self._complete_auction_sale(space, winner, winning_bid)
            if self.turn_can_roll_again and not declined_by.bankrupt:
                self._prepare_next_roll_after_doubles(declined_by)
            self._sync_cash_scores()
            self.rebuild_all_menus()
            return

        self.pending_auction_space_id = space.space_id
        self.pending_auction_bidder_ids = [bidder.id for bidder in bidders]
        self.pending_auction_turn_index = 0
        self.pending_auction_high_bidder_id = ""
        self.pending_auction_current_bid = 0

        self.broadcast_l(
            "monopoly-auction-started",
            property=space.name,
            amount=MIN_AUCTION_INCREMENT,
        )
        self._advance_pending_auction_turn(-1)

    def _is_free_parking_jackpot_enabled(self) -> bool:
        """Return True when current preset enables jackpot on Free Parking."""
        return self.rule_profile.enable_free_parking_jackpot

    def _bail_amount(self) -> int:
        """Return active bail amount from the current rule profile."""
        return max(0, self.rule_profile.bail_amount)

    def _apply_sore_loser_rebate(self, player: MonopolyPlayer, amount_paid: int) -> int:
        """Grant profile-configured consolation cash after a forced payment."""
        rebate = max(0, self.rule_profile.sore_loser_rebate_on_payment)
        if rebate <= 0 or amount_paid <= 0:
            return 0
        granted = min(rebate, amount_paid)
        granted = self._credit_player(player, granted, "sore_loser_rebate")
        self.broadcast_l(
            "monopoly-sore-loser-rebate",
            player=player.name,
            amount=granted,
            cash=player.cash,
        )
        return granted

    def _award_builder_blocks(self, player: MonopolyPlayer) -> int:
        """Award builder blocks after a successful property acquisition."""
        blocks = max(0, self.rule_profile.builder_blocks_per_purchase)
        if blocks <= 0:
            return 0
        player.builder_blocks += blocks
        self.broadcast_l(
            "monopoly-builder-blocks-awarded",
            player=player.name,
            amount=blocks,
            blocks=player.builder_blocks,
        )
        return blocks

    def _can_buy_pending_space(self, player: MonopolyPlayer) -> bool:
        """Return True if the active player can buy pending space now."""
        if not self.rule_profile.allow_manual_property_buy:
            return False
        space = self._pending_purchase_space()
        if not space:
            return False
        if space.kind not in PURCHASABLE_KINDS:
            return False
        if space.space_id in self.property_owners:
            return False
        return self._current_liquid_balance(player) >= space.price > 0

    def _buy_property_for_player(self, player: MonopolyPlayer, space: MonopolySpace) -> bool:
        """Buy one unowned property for a player and broadcast the result."""
        if space.space_id in self.property_owners:
            return False
        if space.price <= 0:
            return False
        if self._current_liquid_balance(player) < space.price:
            return False

        paid = self._debit_player_to_bank(player, space.price, f"buy_property:{space.space_id}")
        if paid < space.price:
            return False

        if space.space_id not in player.owned_space_ids:
            player.owned_space_ids.append(space.space_id)
        self.property_owners[space.space_id] = player.id
        if space.space_id in self.mortgaged_space_ids:
            self.mortgaged_space_ids.remove(space.space_id)

        self.broadcast_l(
            "monopoly-property-bought",
            player=player.name,
            property=space.name,
            price=paid,
            cash=player.cash,
        )
        self._award_builder_blocks(player)
        return True

    def _reset_turn_state(self, *, reset_doubles: bool = True) -> None:
        """Reset transient per-turn state."""
        self.turn_has_rolled = False
        self.turn_last_roll.clear()
        self.turn_pending_purchase_space_id = ""
        self.turn_can_roll_again = False
        if reset_doubles:
            self.turn_doubles_count = 0

    def _start_cheaters_turn(self, player: Player | None = None) -> None:
        """Initialize per-turn cheaters detector state for the active player."""
        if self.cheaters_engine is None:
            return
        turn_player: MonopolyPlayer | None = None
        if isinstance(player, MonopolyPlayer):
            turn_player = player
        elif isinstance(self.current_player, MonopolyPlayer):
            turn_player = self.current_player
        if turn_player is None or turn_player.bankrupt:
            return
        self.cheaters_engine.on_turn_start(turn_player.id, turn_index=self.turn_index)

    def _start_city_turn(self, player: Player | None = None) -> None:
        """Initialize per-turn City engine state for the active player."""
        if self.city_engine is None:
            return
        turn_player: MonopolyPlayer | None = None
        if isinstance(player, MonopolyPlayer):
            turn_player = player
        elif isinstance(self.current_player, MonopolyPlayer):
            turn_player = self.current_player
        if turn_player is None or turn_player.bankrupt:
            return
        self.city_engine.on_turn_start(turn_player.id, turn_index=self.turn_index)

    def _apply_cheaters_outcome(
        self,
        player: MonopolyPlayer,
        outcome: CheaterOutcome,
        *,
        reason: str,
        block_action_on_penalty: bool = False,
    ) -> bool:
        """Apply a cheaters outcome and return whether normal flow should continue."""
        if outcome.status == "allow":
            return True

        amount = 0
        penalty_due = 0
        if outcome.cash_delta < 0:
            penalty_due = max(0, -outcome.cash_delta)
            if penalty_due > 0 and self._current_liquid_balance(player) < penalty_due:
                self._liquidate_assets_for_debt(player, penalty_due)
            amount = self._debit_player_to_bank(
                player,
                penalty_due,
                f"cheaters:{outcome.reason_code or reason}",
                allow_partial=True,
            )
        elif outcome.cash_delta > 0:
            amount = self._credit_player(
                player,
                outcome.cash_delta,
                f"cheaters:{outcome.reason_code or reason}",
            )

        if outcome.message_key:
            self.broadcast_l(
                outcome.message_key,
                player=player.name,
                amount=amount,
                cash=player.cash,
            )

        if penalty_due > 0 and amount < penalty_due:
            self._declare_bankrupt(player)
            self._sync_cash_scores()
            return False

        self._sync_cash_scores()
        if outcome.status == "block":
            return False
        if block_action_on_penalty and outcome.status == "penalty":
            return False
        return True

    def _prepare_next_roll_after_doubles(self, player: MonopolyPlayer) -> None:
        """Unlock another roll for doubles chain turns."""
        self.turn_has_rolled = False
        self.turn_last_roll.clear()
        self.turn_pending_purchase_space_id = ""
        self.turn_can_roll_again = False
        self.broadcast_l("monopoly-roll-again", player=player.name)

    def _resolve_board_pass_go_credit(self, base_credit: int) -> int:
        """Resolve pass-GO credit with board rule-pack override when active."""
        if self.active_board_effective_mode != "board_rules":
            return max(0, base_credit)
        rule_pack_id = self.active_board_rule_pack_id
        if not rule_pack_id:
            return max(0, base_credit)
        if not supports_capability(rule_pack_id, "pass_go_credit_override"):
            return max(0, base_credit)
        override = get_pass_go_credit_override(rule_pack_id)
        if override is None:
            return max(0, base_credit)
        return max(0, override)

    def _load_active_manual_rule_set(self) -> ManualRuleSet | None:
        """Load active board manual rules when board-rules mode is enabled."""
        if self.active_board_effective_mode != "board_rules":
            return None
        if not self.active_board_rule_pack_id:
            return None
        try:
            return load_manual_rule_set(self.active_board_id)
        except (FileNotFoundError, ValueError):
            return None

    def _ensure_valid_board_specific_deck_mode(self) -> bool:
        """Validate board-specific deck mode against current rule-pack state."""
        if self.active_board_deck_mode != "board_specific":
            return True
        rule_pack_id = self.active_board_rule_pack_id
        if not rule_pack_id or get_rule_pack(rule_pack_id) is None:
            self.active_board_deck_mode = "classic"
            return False
        return True

    def _resolve_manual_deck_native_card_id(self, deck_type: str, card_id: str) -> str:
        """Resolve canonical compatibility card ids to native manual deck ids by index."""
        manual_deck_ids = self._manual_deck_ids(deck_type)
        if not manual_deck_ids:
            return card_id
        if card_id in manual_deck_ids:
            return card_id

        canonical_ids: list[str]
        if deck_type == "chance":
            canonical_ids = CHANCE_CARD_IDS
        elif deck_type == "community_chest":
            canonical_ids = COMMUNITY_CHEST_CARD_IDS
        else:
            return card_id

        if len(manual_deck_ids) != len(canonical_ids):
            return card_id
        try:
            card_index = canonical_ids.index(card_id)
        except ValueError:
            return card_id
        return manual_deck_ids[card_index]

    def _resolve_board_card_id(self, deck_type: str, card_id: str) -> str:
        """Resolve board-specific remap for one drawn card id."""
        if self.active_board_effective_mode != "board_rules":
            return card_id
        if self.active_board_deck_mode != "board_specific":
            return card_id
        if not self._ensure_valid_board_specific_deck_mode():
            return card_id
        rule_pack_id = self.active_board_rule_pack_id
        if not rule_pack_id:
            return card_id
        if not supports_capability(rule_pack_id, "card_id_remap"):
            return self._resolve_manual_deck_native_card_id(deck_type, card_id)
        remapped_card_id = get_card_id_remap(rule_pack_id, deck_type, card_id)
        return self._resolve_manual_deck_native_card_id(deck_type, remapped_card_id)

    def _resolve_board_card_cash(self, card_id: str, default_amount: int) -> int:
        """Resolve board-specific card cash override when active."""
        amount = max(0, default_amount)
        if self.active_board_effective_mode != "board_rules":
            return amount
        if self.active_board_deck_mode != "board_specific":
            return amount
        if not self._ensure_valid_board_specific_deck_mode():
            return amount
        rule_pack_id = self.active_board_rule_pack_id
        if not rule_pack_id:
            return amount
        if not supports_capability(rule_pack_id, "card_cash_override"):
            return amount
        override = get_card_cash_override(rule_pack_id, card_id)
        if override is None:
            return amount
        return max(0, override)

    def _is_junior_super_mario_manual_core_active(self) -> bool:
        """Return True when junior Super Mario manual-core behavior is active."""
        if self.active_board_id != "junior_super_mario":
            return False
        if self.active_board_effective_mode != "board_rules":
            return False
        if not self.active_board_rule_pack_id:
            return False
        return supports_capability(self.active_board_rule_pack_id, "junior_manual_core")

    def _junior_super_mario_starting_cash(self) -> int:
        """Return manual-core starting cash based on active player count."""
        player_count = len([player for player in self.turn_players if isinstance(player, MonopolyPlayer)])
        if player_count <= 2:
            return 20
        if player_count == 3:
            return 18
        return 16

    def _apply_junior_super_mario_starting_cash(self) -> None:
        """Apply manual-core starting cash table to active Monopoly players."""
        if not self._is_junior_super_mario_manual_core_active():
            return
        starting_cash = self._junior_super_mario_starting_cash()
        for player in self.turn_players:
            if isinstance(player, MonopolyPlayer):
                player.cash = starting_cash

    def _resolve_board_hardware_event(
        self,
        event_id: str,
        payload: dict[str, object] | None = None,
    ) -> HardwareResult:
        """Resolve one board hardware event through global emulation framework."""
        event = HardwareEvent(
            board_id=self.active_board_id,
            event_id=event_id,
            payload=payload or {},
        )
        return resolve_hardware_event(event, sound_mode=self.active_sound_mode)

    def _emit_board_hardware_event(
        self,
        event_id: str,
        payload: dict[str, object] | None = None,
    ) -> HardwareResult | None:
        """Resolve and record one board hardware event when hardware capabilities are active."""
        if self.active_board_effective_mode != "board_rules":
            return None
        if self.active_board_rule_pack_id and get_rule_pack(self.active_board_rule_pack_id) is None:
            self.active_board_hardware_capability_ids = ()
            return None
        if not self.active_board_hardware_capability_ids:
            return None
        result = self._resolve_board_hardware_event(event_id, payload)
        self.last_hardware_event_id = event_id
        self.last_hardware_event_status = result.status
        self.last_hardware_event_details = result.details
        if result.status == "emulated" and result.sound_asset:
            self.play_sound(result.sound_asset)
        return result

    def _resolve_card_hardware_event_id(self, deck_type: str) -> str | None:
        """Map card draws to optional board hardware events."""
        if deck_type not in {"chance", "community_chest"}:
            return None
        if self.active_board_id.startswith("star_wars"):
            return "star_wars_theme"
        return None

    def _resolve_jurassic_park_gate_outcome(self) -> tuple[str, int] | None:
        """Resolve Jurassic Park Electronic Gate outcome on pass-GO.

        Returns None when the gate mechanic is not active.
        Otherwise returns (event_id, cash) — 50/50 theme ($200) vs roar ($100).
        """
        if self.active_board_id != "jurassic_park":
            return None
        if not self.active_board_rule_pack_id:
            return None
        if not supports_capability(self.active_board_rule_pack_id, "electronic_gate_sound_unit"):
            return None
        if random.random() < 0.5:
            return ("jurassic_park_gate_theme", 200)
        return ("jurassic_park_gate_roar", 100)

    def _resolve_pride_rock_celebration(self) -> str | None:
        """Resolve Disney Lion King Pride Rock celebration on pass-GO.

        Returns the event_id when the Pride Rock mechanic is active, else None.
        Pure celebration — does not affect pass-GO cash.
        """
        if self.active_board_id != "disney_lion_king":
            return None
        if not self.active_board_rule_pack_id:
            return None
        if not supports_capability(self.active_board_rule_pack_id, "pride_rock_sound_unit"):
            return None
        return "pride_rock_celebration"

    def _resolve_question_block_outcome(self) -> tuple[str, str, int] | None:
        """Resolve Mario Celebration Question Block outcome.

        Returns None when the Question Block mechanic is not active.
        Otherwise returns (event_id, outcome_type, amount).
        """
        if self.active_board_id != "mario_celebration":
            return None
        if self.active_board_effective_mode != "board_rules":
            return None
        if not self.active_board_rule_pack_id:
            return None
        if not supports_capability(self.active_board_rule_pack_id, "question_block_sound_unit"):
            return None
        roll = random.randint(1, 6)
        if roll <= 2:
            return ("mario_question_block_coin_ping", "coin_ping", random.randint(1, 4) * 100)
        if roll <= 4:
            return ("mario_question_block_bowser", "bowser", 500)
        if roll == 5:
            return ("mario_question_block_power_up", "power_up", 0)
        return ("mario_question_block_game_over", "game_over", 1000)

    def _apply_question_block_outcome(
        self,
        player: MonopolyPlayer,
        outcome: tuple[str, str, int],
        *,
        depth: int,
        dice_total: int | None,
    ) -> str:
        """Apply a resolved Question Block outcome in place of a Chance card draw."""
        event_id, outcome_type, amount = outcome
        self._emit_board_hardware_event(event_id, payload={"outcome": outcome_type, "amount": amount})

        if outcome_type == "coin_ping":
            self._credit_player(player, amount, "question_block_coin_ping")
            self.broadcast_l("monopoly-card-collect", player=player.name, amount=amount, cash=player.cash)
            return "resolved"

        if outcome_type in ("bowser", "game_over"):
            if not self._apply_bank_payment(player, amount, card_reason_key="monopoly-card-pay"):
                return "bankrupt"
            return "resolved"

        if outcome_type == "power_up":
            extra_steps = random.randint(1, 6)
            landed_space = self._move_player(player, extra_steps, collect_pass_go=True)
            self.broadcast_l(
                "monopoly-roll-result",
                player=player.name,
                die1=extra_steps,
                die2=0,
                total=extra_steps,
                space=landed_space.name,
            )
            return self._resolve_space(player, landed_space, depth=depth + 1, dice_total=extra_steps)

        return "resolved"

    def _resolve_junior_super_mario_powerup_sound_outcome(self, power_up_die: int) -> str | None:
        """Resolve sound-specific power-up outcome when future sound mode is enabled."""
        if not self._is_junior_super_mario_manual_core_active():
            return None
        if not self.active_board_rule_pack_id:
            return None
        if not supports_capability(self.active_board_rule_pack_id, "junior_powerup_sound_ready"):
            return None
        return None

    def _resolve_junior_super_mario_hardware_event_id(self) -> str | None:
        """Map junior power-up flow to optional hardware coin-sound events."""
        if not self._is_junior_super_mario_manual_core_active():
            return None
        if not self.active_board_rule_pack_id:
            return None
        if not supports_capability(self.active_board_rule_pack_id, "junior_powerup_sound_ready"):
            return None
        return "junior_coin_sound_powerup"

    def _resolve_junior_super_mario_powerup_outcome(self, power_up_die: int) -> str:
        """Resolve no-sound power-up outcome for junior Super Mario board."""
        sound_outcome = self._resolve_junior_super_mario_powerup_sound_outcome(power_up_die)
        if isinstance(sound_outcome, str) and sound_outcome:
            return sound_outcome
        default_map = {
            1: "roll_numbered_die_again",
            2: "collect_1",
            3: "collect_2",
            4: "collect_2",
            5: "collect_3",
            6: "nothing",
        }
        return default_map.get(power_up_die, "nothing")

    def _apply_junior_super_mario_powerup(
        self,
        player: MonopolyPlayer,
        power_up_die: int,
    ) -> str:
        """Apply one junior Super Mario power-up die outcome."""
        if not self._is_junior_super_mario_manual_core_active():
            return "resolved"

        outcome = self._resolve_junior_super_mario_powerup_outcome(power_up_die)
        hardware_event_id = self._resolve_junior_super_mario_hardware_event_id()
        if hardware_event_id is not None:
            self._emit_board_hardware_event(
                hardware_event_id,
                payload={
                    "power_up_die": power_up_die,
                    "outcome": outcome,
                },
            )
        if outcome == "nothing":
            return "resolved"

        if outcome == "roll_numbered_die_again":
            extra_steps = random.randint(1, 6)
            landed_space = self._move_player(player, extra_steps, collect_pass_go=True)
            self.broadcast_l(
                "monopoly-roll-result",
                player=player.name,
                die1=extra_steps,
                die2=0,
                total=extra_steps,
                space=landed_space.name,
            )
            return self._resolve_space(player, landed_space, dice_total=extra_steps)

        if outcome.startswith("collect_"):
            try:
                amount = max(0, int(outcome.split("_", 1)[1]))
            except (TypeError, ValueError):
                return "resolved"
            credited = self._credit_player(player, amount, "junior_super_mario_powerup_collect")
            self.broadcast_l(
                "monopoly-card-collect",
                player=player.name,
                amount=credited,
                cash=player.cash,
            )
            return "resolved"

        return "resolved"

    def _move_player(
        self, player: MonopolyPlayer, steps: int, *, collect_pass_go: bool
    ) -> MonopolySpace:
        """Move player by steps and return landed space."""
        old_position = player.position
        absolute_position = old_position + steps
        player.position = absolute_position % self.active_board_size

        if collect_pass_go and absolute_position >= self.active_board_size:
            pass_go_cash = max(0, self.rule_profile.pass_go_cash)
            if self._is_electronic_banking_preset() and self.banking_profile:
                pass_go_cash = max(0, self.banking_profile.pass_go_credit)
            pass_go_cash = self._resolve_board_pass_go_credit(pass_go_cash)
            gate_outcome = self._resolve_jurassic_park_gate_outcome()
            if gate_outcome is not None:
                gate_event_id, pass_go_cash = gate_outcome
                self._emit_board_hardware_event(
                    gate_event_id,
                    payload={"pass_go_cash": pass_go_cash},
                )
            credited = self._credit_player(player, pass_go_cash, "pass_go")
            if self.city_engine is not None and credited > 0:
                self.city_engine.record_progress(player.id, credited)
            pride_rock_event = self._resolve_pride_rock_celebration()
            if pride_rock_event is not None:
                self._emit_board_hardware_event(
                    pride_rock_event,
                    payload={"pass_go_cash": pass_go_cash},
                )
            self.broadcast_l(
                "monopoly-pass-go",
                player=player.name,
                amount=credited,
                cash=player.cash,
            )
        return self._space_at(player.position)

    def _draw_card(self, deck_type: str) -> str:
        """Draw the next card from a deck in cyclic order."""
        if deck_type == "chance":
            if not self.chance_deck_order:
                self.chance_deck_order = self._manual_deck_ids("chance") or CHANCE_CARD_IDS.copy()
                if self.chance_deck_order == CHANCE_CARD_IDS:
                    random.shuffle(self.chance_deck_order)
            card = self.chance_deck_order[self.chance_deck_index % len(self.chance_deck_order)]
            self.chance_deck_index += 1
            return card

        if not self.community_chest_deck_order:
            self.community_chest_deck_order = (
                self._manual_deck_ids("community_chest") or COMMUNITY_CHEST_CARD_IDS.copy()
            )
            if self.community_chest_deck_order == COMMUNITY_CHEST_CARD_IDS:
                random.shuffle(self.community_chest_deck_order)
        card = self.community_chest_deck_order[
            self.community_chest_deck_index % len(self.community_chest_deck_order)
        ]
        self.community_chest_deck_index += 1
        return card

    def _send_to_jail(self, player: MonopolyPlayer, *, by_triple_doubles: bool = False) -> None:
        """Send a player to jail and clear unresolved landing state."""
        player.position = 10
        player.in_jail = True
        player.jail_turns = 0
        self.turn_pending_purchase_space_id = ""
        self.turn_can_roll_again = False

        if by_triple_doubles:
            self.broadcast_l("monopoly-three-doubles-jail", player=player.name)
        else:
            jail_space = self._space_at(10)
            self.broadcast_l(
                "monopoly-go-to-jail",
                player=player.name,
                space=jail_space.name,
            )

    def _payment_context(self, payment_type: str, **details: str | None) -> dict[str, str | None]:
        """Build shared payment context payload for cheaters engine hooks."""
        context: dict[str, str | None] = {"payment_type": payment_type}
        context.update(details)
        return context

    def _apply_cheaters_payment_required(
        self,
        player: MonopolyPlayer,
        reason: str,
        amount: int,
        context: dict[str, str | None],
    ) -> bool:
        """Apply cheaters pre-payment hook and return whether play should continue."""
        if self.cheaters_engine is None:
            return True
        required_outcome = self.cheaters_engine.on_payment_required(
            player.id,
            reason,
            amount,
            context=context,
        )
        return self._apply_cheaters_outcome(
            player,
            required_outcome,
            reason="payment_required",
        )

    def _apply_cheaters_payment_result(
        self,
        player: MonopolyPlayer,
        paid: int,
        required: int,
        context: dict[str, str | None],
    ) -> bool:
        """Apply cheaters post-payment hook and return whether play should continue."""
        if self.cheaters_engine is None or player.bankrupt:
            return True
        result_outcome = self.cheaters_engine.on_payment_result(
            player.id,
            paid,
            required,
            context=context,
        )
        return self._apply_cheaters_outcome(
            player,
            result_outcome,
            reason="payment_result",
        )

    def _bank_payment_reason(self, tax_name: str | None, card_reason_key: str | None) -> str:
        """Resolve bank-payment reason key for transaction hooks."""
        if tax_name:
            return f"tax:{tax_name}"
        if card_reason_key:
            return f"card:{card_reason_key}"
        return "bank_payment"

    def _broadcast_bank_payment(
        self,
        player: MonopolyPlayer,
        paid: int,
        tax_name: str | None,
        card_reason_key: str | None,
    ) -> None:
        """Broadcast canonical bank-payment messages for taxes/cards."""
        if tax_name:
            self.broadcast_l(
                "monopoly-tax-paid",
                player=player.name,
                amount=paid,
                tax=tax_name,
                cash=player.cash,
            )
        elif card_reason_key:
            self.broadcast_l(
                card_reason_key,
                player=player.name,
                amount=paid,
                cash=player.cash,
            )

    def _apply_bank_payment(
        self,
        player: MonopolyPlayer,
        amount: int,
        *,
        tax_name: str | None = None,
        card_reason_key: str | None = None,
    ) -> bool:
        """Charge player money to bank; return False if player bankrupt."""
        if amount <= 0:
            return True

        reason = self._bank_payment_reason(tax_name, card_reason_key)
        payment_context = self._payment_context(
            "bank",
            tax_name=tax_name,
            card_reason_key=card_reason_key,
        )
        manual_core = self._is_junior_super_mario_manual_core_active()

        if not self._apply_cheaters_payment_required(
            player,
            reason,
            amount,
            payment_context,
        ):
            return False

        if not manual_core and self._current_liquid_balance(player) < amount:
            self._liquidate_assets_for_debt(player, amount)

        paid = self._debit_player_to_bank(player, amount, reason, allow_partial=True)
        if self._is_free_parking_jackpot_enabled():
            self.free_parking_pool += paid

        self._broadcast_bank_payment(player, paid, tax_name, card_reason_key)
        self._apply_sore_loser_rebate(player, paid)

        if not self._apply_cheaters_payment_result(
            player,
            paid,
            amount,
            payment_context,
        ):
            return False

        if player.bankrupt:
            return False
        if paid < amount:
            if manual_core:
                return True
            self._declare_bankrupt(player)
            return False
        return True

    def _sync_cash_scores(self) -> None:
        """Mirror player cash into team scores for score actions."""
        if self._team_manager.team_mode != "individual":
            return
        self._sync_all_player_cash_from_banking()
        for team in self._team_manager.teams:
            if not team.members:
                continue
            player = self.get_player_by_name(team.members[0])
            team.total_score = player.cash if player else 0
            team.round_score = 0
        if self._is_junior_preset() and not self.junior_endgame_evaluating:
            self._check_junior_endgame()
        if self._is_city_preset() and not self.city_endgame_evaluating:
            self._check_city_endgame()

    def _city_rent_value_total(self, player: MonopolyPlayer) -> int:
        """Return summed City rent value for all currently owned districts."""
        total = 0
        for space_id in player.owned_space_ids:
            if self.property_owners.get(space_id) != player.id:
                continue
            if space_id in self.mortgaged_space_ids:
                continue
            space = self.active_space_by_id.get(space_id)
            if not space or not self._is_street_property(space):
                continue
            total += max(0, self._calculate_rent_due(space, player.id, dice_total=None))
        return total

    def _city_final_value(self, player: MonopolyPlayer) -> int:
        """Return City final value used by anchor-backed winner resolution."""
        return max(0, self._current_liquid_balance(player)) + self._city_rent_value_total(player)

    def _finish_city_game_by_value(
        self,
        winner: MonopolyPlayer,
        totals: dict[str, int],
    ) -> bool:
        """Finish City game selecting richest player by final value."""
        self.status = "finished"
        self.game_active = False
        self.set_turn_players([winner])
        self.turn_index = 0
        self.broadcast_l(
            "monopoly-city-winner-by-value",
            player=winner.name,
            total=totals.get(winner.id, self._city_final_value(winner)),
        )
        return True

    def _check_city_endgame(self) -> bool:
        """Evaluate City-specific win condition when threshold is reached."""
        if not self._is_city_preset() or self.city_engine is None or self.city_profile is None:
            return False
        if self.status != "playing" or not self.game_active:
            return False

        self.city_endgame_evaluating = True
        try:
            contenders = [
                player
                for player in self.turn_players
                if isinstance(player, MonopolyPlayer) and not player.bankrupt
            ]
            if len(contenders) <= 1:
                if contenders:
                    totals = {contenders[0].id: self._city_final_value(contenders[0])}
                    return self._finish_city_game_by_value(contenders[0], totals)
                return False

            contender_ids = tuple(player.id for player in contenders)
            threshold_trigger = self.city_engine.evaluate_winner(contender_ids)
            if threshold_trigger is None:
                return False

            totals = {player.id: self._city_final_value(player) for player in contenders}
            winner_id = self.city_engine.evaluate_richest(contender_ids, totals)
            if winner_id is None:
                return False
            winner = next((player for player in contenders if player.id == winner_id), None)
            if winner is None:
                return False
            return self._finish_city_game_by_value(winner, totals)
        finally:
            self.city_endgame_evaluating = False

    def _junior_property_pool_limit(self) -> int:
        """Return purchasable property count for junior completion checks."""
        return sum(1 for space in self.active_board_spaces if space.kind in PURCHASABLE_KINDS)

    def _owned_property_count(self, player: MonopolyPlayer) -> int:
        """Return how many currently owned board spaces belong to a player."""
        return sum(
            1
            for owner_id in self.property_owners.values()
            if owner_id == player.id
        )

    def _finish_junior_game_by_cash(self, contenders: list[MonopolyPlayer]) -> bool:
        """Finish junior game selecting highest-cash player as winner."""
        if not contenders:
            return False
        if self._is_junior_super_mario_manual_core_active():
            winner = max(
                contenders,
                key=lambda item: (
                    self._current_liquid_balance(item),
                    self._owned_property_count(item),
                    item.name,
                ),
            )
        else:
            winner = max(
                contenders,
                key=lambda item: (self._current_liquid_balance(item), -item.position, item.name),
            )
        self.status = "finished"
        self.game_active = False
        self.set_turn_players([winner])
        self.turn_index = 0
        self.broadcast_l(
            "monopoly-winner-by-cash",
            player=winner.name,
            cash=self._current_liquid_balance(winner),
        )
        return True

    def _check_junior_endgame(self) -> bool:
        """Evaluate junior-specific win conditions."""
        if not self._is_junior_preset() or not self.junior_ruleset:
            return False
        if self.status != "playing" or not self.game_active:
            return False

        self.junior_endgame_evaluating = True
        try:
            contenders = [
                player
                for player in self.turn_players
                if isinstance(player, MonopolyPlayer) and not player.bankrupt
            ]
            if len(contenders) <= 1:
                if contenders:
                    return self._finish_junior_game_by_cash(contenders)
                return False

            if self.junior_ruleset.game_end_mode == "property_pool_exhausted":
                if len(self.property_owners) >= self._junior_property_pool_limit():
                    return self._finish_junior_game_by_cash(contenders)
                if (
                    not self._is_junior_super_mario_manual_core_active()
                    and self.round >= self.junior_ruleset.max_rounds
                ):
                    return self._finish_junior_game_by_cash(contenders)
            return False
        finally:
            self.junior_endgame_evaluating = False

    def _resolve_bankruptcy_creditor(
        self,
        player: MonopolyPlayer,
        creditor_id: str | None,
    ) -> MonopolyPlayer | None:
        """Resolve valid bankruptcy creditor player when one is provided."""
        if not creditor_id:
            return None
        maybe_creditor = self.get_player_by_id(creditor_id)
        if (
            maybe_creditor
            and isinstance(maybe_creditor, MonopolyPlayer)
            and not maybe_creditor.bankrupt
            and maybe_creditor.id != player.id
        ):
            return maybe_creditor
        return None

    def _transfer_bankrupt_holdings(
        self,
        player: MonopolyPlayer,
        creditor: MonopolyPlayer | None,
    ) -> None:
        """Transfer/release all player holdings during bankruptcy."""
        for space_id in list(player.owned_space_ids):
            if self.property_owners.get(space_id) == player.id:
                if creditor:
                    self.property_owners[space_id] = creditor.id
                    if space_id not in creditor.owned_space_ids:
                        creditor.owned_space_ids.append(space_id)
                else:
                    del self.property_owners[space_id]
            if not creditor and space_id in self.mortgaged_space_ids:
                self.mortgaged_space_ids.remove(space_id)
            # Buildings are liquidated during bankruptcy transfer/release.
            if space_id in self.building_levels:
                self.building_levels[space_id] = 0

    def _clear_bankrupt_player_state(
        self,
        player: MonopolyPlayer,
        creditor: MonopolyPlayer | None,
    ) -> None:
        """Zero all transferable state and close banking account for bankrupt player."""
        if creditor and player.get_out_of_jail_cards > 0:
            creditor.get_out_of_jail_cards += player.get_out_of_jail_cards
        player.get_out_of_jail_cards = 0
        self._close_bank_account(player, creditor=creditor)
        player.cash = 0
        player.builder_blocks = 0
        player.owned_space_ids.clear()
        player.in_jail = False
        player.jail_turns = 0

    def _cancel_pending_trade_for_bankrupt_player(self, player: MonopolyPlayer) -> None:
        """Cancel pending trade when bankrupt player is involved."""
        pending = self.pending_trade_offer
        if pending and (pending.proposer_id == player.id or pending.target_id == player.id):
            self.broadcast_l("monopoly-trade-cancelled", offer=pending.summary)
            self.pending_trade_offer = None

    def _finalize_turn_order_after_bankruptcy(self, player: MonopolyPlayer) -> None:
        """Finalize winner/turn-order state after one player is marked bankrupt."""
        ordered_before = self.turn_players
        try:
            old_index = ordered_before.index(player)
        except ValueError:
            old_index = 0

        remaining = [turn_player for turn_player in ordered_before if not turn_player.bankrupt]
        if len(remaining) <= 1:
            self.status = "finished"
            self.game_active = False
            self.set_turn_players(remaining)
            if remaining:
                winner = remaining[0]
                self.broadcast_l(
                    "monopoly-winner-by-bankruptcy",
                    player=winner.name,
                    cash=self._current_liquid_balance(winner),
                )
            return

        self.set_turn_players(remaining, reset_index=False)
        self.turn_index = old_index % len(remaining)
        self._reset_turn_state()
        self._start_cheaters_turn(self.current_player)
        self._start_city_turn(self.current_player)
        self.announce_turn(turn_sound="game_pig/turn.ogg")
        current = self.current_player
        if current and current.is_bot:
            BotHelper.jolt_bot(current, ticks=random.randint(8, 14))

    def _declare_bankrupt(
        self,
        player: MonopolyPlayer,
        *,
        creditor_name: str | None = None,
        creditor_id: str | None = None,
    ) -> None:
        """Mark a player bankrupt, release their holdings, and check winner."""
        if player.bankrupt:
            return

        player.bankrupt = True
        creditor = self._resolve_bankruptcy_creditor(player, creditor_id)
        self._transfer_bankrupt_holdings(player, creditor)
        self._clear_bankrupt_player_state(player, creditor)
        self._cancel_pending_trade_for_bankrupt_player(player)

        self.broadcast_l(
            "monopoly-player-bankrupt",
            player=player.name,
            creditor=creditor_name or (creditor.name if creditor else "Bank"),
        )
        self._finalize_turn_order_after_bankruptcy(player)

    def _resolve_card_draw_text(
        self,
        manual_card: dict[str, object] | None,
        card_id: str,
    ) -> str:
        """Resolve display text for one drawn card."""
        if isinstance(manual_card, dict):
            literal_text = manual_card.get("text")
            if isinstance(literal_text, str):
                normalized = literal_text.strip()
                if normalized:
                    return normalized

            manual_text_key = manual_card.get("text_key")
            if isinstance(manual_text_key, str):
                resolved_manual = Localization.get("en", manual_text_key)
                # When a manual-specific key is missing, fall back to classic card text.
                if resolved_manual and resolved_manual != manual_text_key:
                    return resolved_manual

        default_text_key = CARD_DESCRIPTION_KEYS.get(card_id, card_id)
        return Localization.get("en", default_text_key)

    def _resolve_card_deck_label(self, deck_type: str) -> str:
        """Resolve deck label for card draw announcements."""
        default_label = "Chance" if deck_type == "chance" else "Community Chest"
        if deck_type not in {"chance", "community_chest"}:
            return default_label
        if self.active_manual_rule_set is None:
            return default_label
        mechanics = self.active_manual_rule_set.mechanics
        decks = mechanics.get("decks") if isinstance(mechanics, dict) else None
        if not isinstance(decks, dict):
            return default_label
        label = decks.get(deck_type)
        if not isinstance(label, str):
            return default_label
        normalized = label.strip()
        if not normalized:
            return default_label
        return normalized

    def _resolve_card_collect_effect(
        self,
        player: MonopolyPlayer,
        amount: int,
        reason: str,
    ) -> str:
        credited = self._credit_player(player, amount, reason)
        self.broadcast_l(
            "monopoly-card-collect",
            player=player.name,
            amount=credited,
            cash=player.cash,
        )
        return "resolved"

    def _resolve_card_pay_effect(self, player: MonopolyPlayer, amount: int) -> str:
        if not self._apply_bank_payment(
            player,
            amount,
            card_reason_key="monopoly-card-pay",
        ):
            return "bankrupt"
        return "resolved"

    def _resolve_card_advance_to_go_effect(self, player: MonopolyPlayer) -> str:
        player.position = 0
        pass_go_cash = max(0, self.rule_profile.pass_go_cash)
        if self._is_electronic_banking_preset() and self.banking_profile:
            pass_go_cash = max(0, self.banking_profile.pass_go_credit)
        credited = self._credit_player(player, pass_go_cash, "chance_advance_to_go")
        self.broadcast_l(
            "monopoly-pass-go",
            player=player.name,
            amount=credited,
            cash=player.cash,
        )
        return "resolved"

    def _resolve_card_go_back_three_effect(
        self,
        player: MonopolyPlayer,
        *,
        depth: int,
        dice_total: int | None,
    ) -> str:
        player.position = (player.position - 3) % self.active_board_size
        landed_space = self._space_at(player.position)
        self.broadcast_l(
            "monopoly-card-move",
            player=player.name,
            space=landed_space.name,
        )
        return self._resolve_space(
            player,
            landed_space,
            depth=depth + 1,
            dice_total=dice_total,
        )

    def _resolve_card_known_effect(
        self,
        player: MonopolyPlayer,
        card_id: str,
        *,
        depth: int,
        dice_total: int | None,
    ) -> str | None:
        if card_id == "advance_to_go":
            return self._resolve_card_advance_to_go_effect(player)

        if card_id == "bank_dividend_50":
            amount = self._resolve_board_card_cash(card_id, 50)
            return self._resolve_card_collect_effect(
                player,
                amount,
                "chance_bank_dividend_50",
            )

        if card_id == "go_back_three":
            return self._resolve_card_go_back_three_effect(
                player,
                depth=depth,
                dice_total=dice_total,
            )

        if card_id == "go_to_jail":
            self._send_to_jail(player)
            return "forced_end"

        if card_id == "poor_tax_15":
            amount = self._resolve_board_card_cash(card_id, 15)
            return self._resolve_card_pay_effect(player, amount)

        if card_id == "bank_error_collect_200":
            amount = self._resolve_board_card_cash(card_id, 200)
            return self._resolve_card_collect_effect(
                player,
                amount,
                "community_chest_bank_error_collect_200",
            )

        if card_id == "doctor_fee_pay_50":
            amount = self._resolve_board_card_cash(card_id, 50)
            return self._resolve_card_pay_effect(player, amount)

        if card_id == "income_tax_refund_20":
            amount = self._resolve_board_card_cash(card_id, 20)
            return self._resolve_card_collect_effect(
                player,
                amount,
                "community_chest_income_tax_refund_20",
            )

        if card_id == "get_out_of_jail_free":
            return self._grant_get_out_of_jail_card(player)

        return None

    def _resolve_card_effect(
        self,
        player: MonopolyPlayer,
        deck_type: str,
        card_id: str,
        *,
        depth: int,
        dice_total: int | None,
    ) -> str:
        """Apply one Chance/Community Chest card and return resolution state."""
        card_id = self._resolve_board_card_id(deck_type, card_id)
        manual_card = self._manual_card_definition(deck_type, card_id)
        deck_label = self._resolve_card_deck_label(deck_type)
        card_text = self._resolve_card_draw_text(manual_card, card_id)
        self.broadcast_l(
            "monopoly-card-drawn",
            player=player.name,
            deck=deck_label,
            card=card_text,
        )
        hardware_event_id = self._resolve_card_hardware_event_id(deck_type)
        if hardware_event_id is not None:
            self._emit_board_hardware_event(
                hardware_event_id,
                payload={"deck_type": deck_type, "card_id": card_id},
            )

        if manual_card is not None:
            effect_spec = manual_card.get("effect")
            if isinstance(effect_spec, dict):
                manual_result = self._apply_manual_card_effect(
                    player,
                    effect_spec,
                    depth=depth,
                    dice_total=dice_total,
                )
                if manual_result is not None:
                    return manual_result

        known_result = self._resolve_card_known_effect(
            player,
            card_id,
            depth=depth,
            dice_total=dice_total,
        )
        if known_result is not None:
            return known_result

        return "resolved"

    def _resolve_unowned_purchasable_space(
        self,
        player: MonopolyPlayer,
        landed_space: MonopolySpace,
    ) -> str:
        if self._is_junior_super_mario_manual_core_active():
            self.turn_pending_purchase_space_id = ""
            self._buy_property_for_player(player, landed_space)
            return "resolved"
        if self.rule_profile.auto_auction_unowned_property:
            self.broadcast_l(
                "monopoly-property-available",
                player=player.name,
                property=landed_space.name,
                price=landed_space.price,
            )
            self._run_property_auction(landed_space, player)
            return "resolved"
        self.turn_pending_purchase_space_id = landed_space.space_id
        self.broadcast_l(
            "monopoly-property-available",
            player=player.name,
            property=landed_space.name,
            price=landed_space.price,
        )
        return "pending_purchase"

    def _resolve_owned_space_no_rent_case(
        self,
        player: MonopolyPlayer,
        landed_space: MonopolySpace,
        owner_id: str,
    ) -> str | None:
        """Resolve owned-space outcomes where no rent transfer is required."""
        if owner_id == player.id:
            self.broadcast_l(
                "monopoly-landed-owned",
                player=player.name,
                property=landed_space.name,
            )
            return "resolved"

        if self._is_space_mortgaged(landed_space.space_id):
            self.broadcast_l(
                "monopoly-mortgaged-no-rent",
                player=player.name,
                property=landed_space.name,
            )
            return "resolved"
        return None

    def _pay_rent_to_owner_or_bank(
        self,
        player: MonopolyPlayer,
        owner: Player | None,
        rent_due: int,
        rent_reason: str,
    ) -> int:
        """Collect rent from player and route funds to owner or bank."""
        if owner and isinstance(owner, MonopolyPlayer):
            return self._transfer_between_players(
                player,
                owner,
                rent_due,
                rent_reason,
                allow_partial=True,
            )
        return self._debit_player_to_bank(
            player,
            rent_due,
            rent_reason,
            allow_partial=True,
        )

    def _finalize_rent_payment(
        self,
        player: MonopolyPlayer,
        owner: Player | None,
        paid: int,
        rent_due: int,
        manual_core: bool,
    ) -> str:
        """Finalize player state after rent transfer and settle bankruptcy path."""
        if player.bankrupt:
            return "bankrupt"
        if paid < rent_due:
            if manual_core:
                return "resolved"
            creditor_name = owner.name if owner else "Bank"
            creditor_id = owner.id if owner and isinstance(owner, MonopolyPlayer) else None
            self._declare_bankrupt(
                player,
                creditor_name=creditor_name,
                creditor_id=creditor_id,
            )
            return "bankrupt"
        return "resolved"

    def _resolve_owned_purchasable_space(
        self,
        player: MonopolyPlayer,
        landed_space: MonopolySpace,
        owner_id: str,
        dice_total: int | None,
    ) -> str:
        no_rent_result = self._resolve_owned_space_no_rent_case(player, landed_space, owner_id)
        if no_rent_result is not None:
            return no_rent_result

        owner = self.get_player_by_id(owner_id)
        rent_due = self._calculate_rent_due(landed_space, owner_id, dice_total)
        rent_reason = f"rent:{landed_space.space_id}"
        payment_context = self._payment_context(
            "rent",
            space_id=landed_space.space_id,
            owner_id=owner_id,
        )
        manual_core = self._is_junior_super_mario_manual_core_active()
        if not self._apply_cheaters_payment_required(
            player,
            rent_reason,
            rent_due,
            payment_context,
        ):
            return "bankrupt" if player.bankrupt else "resolved"
        if not manual_core and self._current_liquid_balance(player) < rent_due:
            self._liquidate_assets_for_debt(player, rent_due)
        paid = self._pay_rent_to_owner_or_bank(player, owner, rent_due, rent_reason)

        self.broadcast_l(
            "monopoly-rent-paid",
            player=player.name,
            owner=owner.name if owner else "Bank",
            amount=paid,
            property=landed_space.name,
        )
        self._apply_sore_loser_rebate(player, paid)
        if not self._apply_cheaters_payment_result(
            player,
            paid,
            rent_due,
            payment_context,
        ):
            return "bankrupt" if player.bankrupt else "resolved"
        return self._finalize_rent_payment(player, owner, paid, rent_due, manual_core)

    def _resolve_purchasable_space(
        self,
        player: MonopolyPlayer,
        landed_space: MonopolySpace,
        dice_total: int | None,
    ) -> str:
        owner_id = self.property_owners.get(landed_space.space_id)
        if owner_id is None:
            return self._resolve_unowned_purchasable_space(player, landed_space)
        return self._resolve_owned_purchasable_space(
            player,
            landed_space,
            owner_id,
            dice_total,
        )

    def _resolve_tax_space(self, player: MonopolyPlayer, landed_space: MonopolySpace) -> str:
        if not self._apply_bank_payment(
            player,
            TAX_AMOUNTS[landed_space.space_id],
            tax_name=landed_space.name,
        ):
            return "bankrupt"
        return "resolved"

    def _resolve_go_to_jail_space(self, player: MonopolyPlayer) -> str:
        if self._is_junior_super_mario_manual_core_active() and self._current_liquid_balance(player) <= 0:
            return "resolved"
        self._send_to_jail(player)
        return "forced_end"

    def _resolve_chance_space(
        self,
        player: MonopolyPlayer,
        *,
        depth: int,
        dice_total: int | None,
    ) -> str:
        qb_outcome = self._resolve_question_block_outcome()
        if qb_outcome is not None:
            return self._apply_question_block_outcome(
                player,
                qb_outcome,
                depth=depth,
                dice_total=dice_total,
            )
        card = self._draw_card("chance")
        return self._resolve_card_effect(
            player,
            "chance",
            card,
            depth=depth,
            dice_total=dice_total,
        )

    def _resolve_community_chest_space(
        self,
        player: MonopolyPlayer,
        *,
        depth: int,
        dice_total: int | None,
    ) -> str:
        card = self._draw_card("community_chest")
        return self._resolve_card_effect(
            player,
            "community_chest",
            card,
            depth=depth,
            dice_total=dice_total,
        )

    def _resolve_free_parking_space(self, player: MonopolyPlayer) -> str:
        if self._is_free_parking_jackpot_enabled() and self.free_parking_pool > 0:
            payout = self.free_parking_pool
            self.free_parking_pool = 0
            payout = self._credit_player(player, payout, "free_parking_jackpot")
            self.broadcast_l(
                "monopoly-free-parking-jackpot",
                player=player.name,
                amount=payout,
                cash=player.cash,
            )
        return "resolved"

    def _resolve_space(
        self,
        player: MonopolyPlayer,
        landed_space: MonopolySpace,
        *,
        depth: int = 0,
        dice_total: int | None = None,
    ) -> str:
        """Resolve effects for the landed space.

        Returns:
            "pending_purchase" when buy/auction decision is required,
            "forced_end" when player was sent to jail,
            "bankrupt" when player went bankrupt,
            "resolved" otherwise.
        """
        if depth > 4:
            return "resolved"

        if landed_space.kind in PURCHASABLE_KINDS:
            return self._resolve_purchasable_space(player, landed_space, dice_total)

        if landed_space.space_id in TAX_AMOUNTS:
            return self._resolve_tax_space(player, landed_space)

        if landed_space.kind == "go_to_jail":
            return self._resolve_go_to_jail_space(player)

        if landed_space.kind == "chance":
            return self._resolve_chance_space(
                player,
                depth=depth,
                dice_total=dice_total,
            )

        if landed_space.kind == "community_chest":
            return self._resolve_community_chest_space(
                player,
                depth=depth,
                dice_total=dice_total,
            )

        if landed_space.kind == "free_parking":
            return self._resolve_free_parking_space(player)

        return "resolved"

    def _run_property_auction(self, space: MonopolySpace, declined_by: MonopolyPlayer) -> None:
        """Run a simple automatic auction for an unpurchased space."""
        bidders: list[tuple[MonopolyPlayer, int]] = []
        order = [p for p in self.turn_players if isinstance(p, MonopolyPlayer)]
        for bidder in order:
            if bidder.bankrupt:
                continue
            weight = 0.75 if bidder.id == declined_by.id else 0.9
            max_bid = min(space.price, int(self._current_liquid_balance(bidder) * weight))
            if max_bid >= MIN_AUCTION_INCREMENT:
                bidders.append((bidder, max_bid))

        if not bidders:
            self.broadcast_l("monopoly-auction-no-bids", property=space.name)
            return

        bidders.sort(key=lambda row: row[1], reverse=True)
        winner, winner_cap = bidders[0]
        second_cap = bidders[1][1] if len(bidders) > 1 else 0
        reserve = max(1, space.price // 2)
        if len(bidders) == 1:
            winning_bid = min(winner_cap, reserve)
        else:
            winning_bid = min(winner_cap, second_cap + MIN_AUCTION_INCREMENT)
        winning_bid = max(1, winning_bid)

        self._complete_auction_sale(space, winner, winning_bid)

    def _is_roll_dice_enabled(self, player: Player) -> str | None:
        """Enable roll action for active player before rolling."""
        return action_guards.is_roll_dice_enabled(self, player)

    def _is_roll_dice_hidden(self, player: Player) -> Visibility:
        """Hide roll once a roll has been made this turn."""
        return action_guards.is_roll_dice_hidden(self, player)

    def _is_buy_property_enabled(self, player: Player) -> str | None:
        """Enable buy action when current player can buy landed property."""
        return action_guards.is_buy_property_enabled(self, player)

    def _is_buy_property_hidden(self, player: Player) -> Visibility:
        """Show buy action only after a roll when a property is pending."""
        return action_guards.is_buy_property_hidden(self, player)

    def _is_auction_property_enabled(self, player: Player) -> str | None:
        """Enable auction action for pending unpurchased property."""
        return action_guards.is_auction_property_enabled(self, player)

    def _is_auction_property_hidden(self, player: Player) -> Visibility:
        """Show auction only when property purchase is pending."""
        return action_guards.is_auction_property_hidden(self, player)

    def _options_for_auction_bid(self, player: Player) -> list[str]:
        """Menu options for bidding in the active interactive auction."""
        return action_options.options_for_auction_bid(self, player)

    def _bot_select_auction_bid(
        self, player: MonopolyPlayer, options: list[str]
    ) -> str | None:
        """Pick a practical bid for bots in interactive auctions."""
        return action_options.bot_select_auction_bid(self, player, options)

    def _is_auction_bid_enabled(self, player: Player) -> str | None:
        """Enable placing a bid when it is this player's auction turn."""
        return action_guards.is_auction_bid_enabled(self, player)

    def _is_auction_bid_hidden(self, player: Player) -> Visibility:
        """Show bid action only to the active auction bidder."""
        return action_guards.is_auction_bid_hidden(self, player)

    def _is_auction_pass_enabled(self, player: Player) -> str | None:
        """Enable passing in an active interactive auction."""
        return action_guards.is_auction_pass_enabled(self, player)

    def _is_auction_pass_hidden(self, player: Player) -> Visibility:
        """Show pass action only to the active auction bidder."""
        return action_guards.is_auction_pass_hidden(self, player)

    def _options_for_mortgage_property(self, player: Player) -> list[str]:
        """Menu options for unmortgaged owned properties."""
        return action_options.options_for_mortgage_property(self, player)

    def _options_for_unmortgage_property(self, player: Player) -> list[str]:
        """Menu options for mortgaged owned properties."""
        return action_options.options_for_unmortgage_property(self, player)

    def _options_for_build_house(self, player: Player) -> list[str]:
        """Menu options for buildable street properties."""
        return action_options.options_for_build_house(self, player)

    def _options_for_sell_house(self, player: Player) -> list[str]:
        """Menu options for sellable street properties."""
        return action_options.options_for_sell_house(self, player)

    def _is_mortgage_property_enabled(self, player: Player) -> str | None:
        """Enable mortgage action when player owns eligible properties."""
        return action_guards.is_mortgage_property_enabled(self, player)

    def _is_mortgage_property_hidden(self, player: Player) -> Visibility:
        """Show mortgage action when options exist."""
        return action_guards.is_mortgage_property_hidden(self, player)

    def _is_unmortgage_property_enabled(self, player: Player) -> str | None:
        """Enable unmortgage action when player has mortgaged properties."""
        return action_guards.is_unmortgage_property_enabled(self, player)

    def _is_unmortgage_property_hidden(self, player: Player) -> Visibility:
        """Show unmortgage action only when options exist."""
        return action_guards.is_unmortgage_property_hidden(self, player)

    def _is_build_house_enabled(self, player: Player) -> str | None:
        """Enable house-building when at least one valid build exists."""
        return action_guards.is_build_house_enabled(self, player)

    def _is_build_house_hidden(self, player: Player) -> Visibility:
        """Show build action when options exist."""
        return action_guards.is_build_house_hidden(self, player)

    def _is_sell_house_enabled(self, player: Player) -> str | None:
        """Enable house selling when at least one valid sell exists."""
        return action_guards.is_sell_house_enabled(self, player)

    def _is_sell_house_hidden(self, player: Player) -> Visibility:
        """Show sell action when options exist."""
        return action_guards.is_sell_house_hidden(self, player)

    def _is_offer_trade_enabled(self, player: Player) -> str | None:
        """Enable trade offers for active players with at least one valid option."""
        return action_guards.is_offer_trade_enabled(self, player)

    def _is_offer_trade_hidden(self, player: Player) -> Visibility:
        """Show offer-trade when player can open a new trade."""
        return action_guards.is_offer_trade_hidden(self, player)

    def _is_accept_trade_enabled(self, player: Player) -> str | None:
        """Enable accepting a pending trade for the addressed target player."""
        return action_guards.is_accept_trade_enabled(self, player)

    def _is_accept_trade_hidden(self, player: Player) -> Visibility:
        """Show accept-trade only to the targeted player."""
        return action_guards.is_accept_trade_hidden(self, player)

    def _is_decline_trade_enabled(self, player: Player) -> str | None:
        """Enable declining a pending trade for the addressed target player."""
        return action_guards.is_decline_trade_enabled(self, player)

    def _is_decline_trade_hidden(self, player: Player) -> Visibility:
        """Show decline-trade only to the targeted player."""
        return action_guards.is_decline_trade_hidden(self, player)

    def _is_pay_bail_enabled(self, player: Player) -> str | None:
        """Enable paying bail while in jail before rolling."""
        return action_guards.is_pay_bail_enabled(self, player)

    def _is_pay_bail_hidden(self, player: Player) -> Visibility:
        """Show pay bail only while player is jailed and has not rolled."""
        return action_guards.is_pay_bail_hidden(self, player)

    def _is_use_jail_card_enabled(self, player: Player) -> str | None:
        """Enable jail-card use while in jail before rolling."""
        return action_guards.is_use_jail_card_enabled(self, player)

    def _is_use_jail_card_hidden(self, player: Player) -> Visibility:
        """Show jail-card action only while usable."""
        return action_guards.is_use_jail_card_hidden(self, player)

    def _is_banking_balance_enabled(self, player: Player) -> str | None:
        """Enable bank balance checks only for electronic banking preset."""
        return action_guards.is_banking_balance_enabled(self, player)

    def _is_banking_balance_hidden(self, player: Player) -> Visibility:
        """Show bank balance action only in electronic banking mode."""
        return action_guards.is_banking_balance_hidden(self, player)

    def _encode_banking_transfer_option(self, target: MonopolyPlayer, amount: int) -> str:
        """Encode one banking transfer option for menu selection."""
        return action_options.encode_banking_transfer_option(self, target, amount)

    def _parse_banking_transfer_option(self, option: str) -> tuple[str, int] | None:
        """Parse one banking transfer option from menu input."""
        return action_options.parse_banking_transfer_option(self, option)

    def _options_for_banking_transfer(self, player: Player) -> list[str]:
        """Menu options for player-to-player transfers in electronic mode."""
        return action_options.options_for_banking_transfer(self, player)

    def _is_banking_transfer_enabled(self, player: Player) -> str | None:
        """Enable manual transfer only when options are available."""
        return action_guards.is_banking_transfer_enabled(self, player)

    def _is_banking_transfer_hidden(self, player: Player) -> Visibility:
        """Show transfer action only when electronic transfer options exist."""
        return action_guards.is_banking_transfer_hidden(self, player)

    def _is_banking_ledger_enabled(self, player: Player) -> str | None:
        """Enable ledger announcements in electronic banking mode."""
        return action_guards.is_banking_ledger_enabled(self, player)

    def _is_banking_ledger_hidden(self, player: Player) -> Visibility:
        """Show ledger action only in electronic banking mode."""
        return action_guards.is_banking_ledger_hidden(self, player)

    def _is_voice_command_enabled(self, player: Player) -> str | None:
        """Enable voice command entry only for voice banking preset."""
        return action_guards.is_voice_command_enabled(self, player)

    def _is_voice_command_hidden(self, player: Player) -> Visibility:
        """Show voice command entry only during voice banking games."""
        return action_guards.is_voice_command_hidden(self, player)

    def _is_claim_cheat_reward_enabled(self, player: Player) -> str | None:
        """Enable reward claim action only during cheaters preset turns."""
        return action_guards.is_claim_cheat_reward_enabled(self, player)

    def _is_claim_cheat_reward_hidden(self, player: Player) -> Visibility:
        """Show reward claim only while the cheaters engine is active."""
        return action_guards.is_claim_cheat_reward_hidden(self, player)

    def _is_end_turn_enabled(self, player: Player) -> str | None:
        """Enable end-turn after rolling."""
        return action_guards.is_end_turn_enabled(self, player)

    def _is_end_turn_hidden(self, player: Player) -> Visibility:
        """Hide end-turn when turn state cannot accept an end-turn attempt."""
        return action_guards.is_end_turn_hidden(self, player)

    def _action_roll_dice(self, player: Player, action_id: str) -> None:
        """Handle rolling and landing logic for classic scaffold."""
        action_handlers.action_roll_dice(self, player, action_id)

    def _action_buy_property(self, player: Player, action_id: str) -> None:
        """Buy currently pending property."""
        action_handlers.action_buy_property(self, player, action_id)

    def _action_auction_property(self, player: Player, action_id: str) -> None:
        """Start an interactive auction for the pending unpurchased property."""
        action_handlers.action_auction_property(self, player, action_id)

    def _action_auction_bid(self, player: Player, option: str, action_id: str) -> None:
        """Place a bid in the active interactive auction."""
        action_handlers.action_auction_bid(self, player, option, action_id)

    def _action_auction_pass(self, player: Player, action_id: str) -> None:
        """Pass on bidding in the active interactive auction."""
        action_handlers.action_auction_pass(self, player, action_id)

    def _action_mortgage_property(
        self, player: Player, space_id: str, action_id: str
    ) -> None:
        """Mortgage one owned property to raise cash."""
        action_handlers.action_mortgage_property(self, player, space_id, action_id)

    def _action_unmortgage_property(
        self, player: Player, space_id: str, action_id: str
    ) -> None:
        """Unmortgage one owned property."""
        action_handlers.action_unmortgage_property(self, player, space_id, action_id)

    def _action_build_house(self, player: Player, space_id: str, action_id: str) -> None:
        """Build one house/hotel on an owned eligible street property."""
        action_handlers.action_build_house(self, player, space_id, action_id)

    def _action_sell_house(self, player: Player, space_id: str, action_id: str) -> None:
        """Sell one house/hotel from an owned eligible street property."""
        action_handlers.action_sell_house(self, player, space_id, action_id)

    def _action_offer_trade(self, player: Player, option: str, action_id: str) -> None:
        """Create a pending trade offer for another player."""
        action_handlers.action_offer_trade(self, player, option, action_id)

    def _action_accept_trade(self, player: Player, action_id: str) -> None:
        """Accept the currently pending trade for this player."""
        action_handlers.action_accept_trade(self, player, action_id)

    def _action_decline_trade(self, player: Player, action_id: str) -> None:
        """Decline the currently pending trade for this player."""
        action_handlers.action_decline_trade(self, player, action_id)

    def _action_pay_bail(self, player: Player, action_id: str) -> None:
        """Pay bail to leave jail before rolling."""
        action_handlers.action_pay_bail(self, player, action_id)

    def _action_use_jail_card(self, player: Player, action_id: str) -> None:
        """Use a get-out-of-jail-free card."""
        action_handlers.action_use_jail_card(self, player, action_id)

    def _action_banking_balance(self, player: Player, action_id: str) -> None:
        """Announce current electronic bank balance to the requesting player."""
        action_handlers.action_banking_balance(self, player, action_id)

    def _action_banking_transfer(self, player: Player, option: str, action_id: str) -> None:
        """Execute one manual bank transfer between players."""
        action_handlers.action_banking_transfer(self, player, option, action_id)

    def _action_banking_ledger(self, player: Player, action_id: str) -> None:
        """Announce recent banking ledger events to the requesting player."""
        action_handlers.action_banking_ledger(self, player, action_id)

    def _action_voice_command(self, player: Player, text: str, action_id: str) -> None:
        """Parse and execute one voice-style command in voice banking preset."""
        action_handlers.action_voice_command(self, player, text, action_id)

    def _action_claim_cheat_reward(self, player: Player, action_id: str) -> None:
        """Apply cheaters reward claim outcome for the active player."""
        action_handlers.action_claim_cheat_reward(self, player, action_id)

    def _action_end_turn(self, player: Player, action_id: str) -> None:
        """End current player's turn and advance."""
        action_handlers.action_end_turn(self, player, action_id)

    def on_tick(self) -> None:
        """Run per-tick updates (bot actions)."""
        super().on_tick()
        if self._run_auction_bot_tick():
            return
        BotHelper.on_tick(self)

    def _run_auction_bot_tick(self) -> bool:
        """Handle the dedicated per-tick bot path while an interactive auction is active."""
        if not self._is_auction_active():
            return False

        bidder = self._current_auction_bidder()
        if bidder and bidder.is_bot:
            if bidder.bot_think_ticks > 0:
                bidder.bot_think_ticks -= 1
                return True
            action_id = self.bot_think(bidder)
            if action_id:
                self.execute_action(bidder, action_id)
        return True

    def _bot_think_active_auction(self, player: MonopolyPlayer) -> str | None:
        if not self._is_auction_active():
            return None
        current_bidder = self._current_auction_bidder()
        if current_bidder and current_bidder.id == player.id:
            bid_options = self._options_for_auction_bid(player)
            if not bid_options:
                return "auction_pass"
            space = self._pending_auction_space()
            min_bid = int(bid_options[0])
            cap = (
                min(space.price, int(self._current_liquid_balance(player) * 0.85))
                if space
                else min_bid
            )
            if cap >= min_bid:
                return "auction_bid"
            return "auction_pass"
        return None

    def _bot_think_pending_purchase(
        self,
        player: MonopolyPlayer,
        *,
        reserve: int,
    ) -> str | None:
        pending_space = self._pending_purchase_space()
        if not pending_space:
            return None
        if self._can_buy_pending_space(player) and (
            self._current_liquid_balance(player) - pending_space.price >= reserve
        ):
            return "buy_property"
        return "auction_property"

    def _bot_think_junior_preset(self, player: MonopolyPlayer, bail_amount: int) -> str:
        if player.in_jail and not self.turn_has_rolled:
            if self._current_liquid_balance(player) >= bail_amount and player.jail_turns >= 1:
                return "pay_bail"
        if not self.turn_has_rolled:
            return "roll_dice"
        pending_action = self._bot_think_pending_purchase(
            player,
            reserve=max(2, self.rule_profile.starting_cash // 6),
        )
        if pending_action is not None:
            return pending_action
        if self.turn_can_roll_again:
            return "roll_dice"
        return "end_turn"

    def _bot_think_pending_trade(self, player: MonopolyPlayer) -> str | None:
        pending_offer = self._pending_trade_for_target(player)
        if not pending_offer:
            return None
        proposer = self.get_player_by_id(pending_offer.proposer_id)
        if proposer and isinstance(proposer, MonopolyPlayer):
            if self._bot_accepts_trade_offer(proposer, player, pending_offer):
                return "accept_trade"
        return "decline_trade"

    def _bot_think_jail_pre_roll(self, player: MonopolyPlayer, bail_amount: int) -> str | None:
        if not (player.in_jail and not self.turn_has_rolled):
            return None
        if player.get_out_of_jail_cards > 0:
            return "use_jail_card"
        if self._current_liquid_balance(player) >= bail_amount and player.jail_turns >= 2:
            return "pay_bail"
        return None

    def _bot_think_pre_roll_economy(self, player: MonopolyPlayer) -> str | None:
        if self.turn_has_rolled or self.turn_pending_purchase_space_id:
            return None
        liquid_balance = self._current_liquid_balance(player)
        if liquid_balance < 100 and self._options_for_mortgage_property(player):
            return "mortgage_property"
        if liquid_balance >= 800 and self._options_for_unmortgage_property(player):
            return "unmortgage_property"
        if liquid_balance >= 450 and self._options_for_build_house(player):
            return "build_house"
        return None

    def bot_think(self, player: MonopolyPlayer) -> str | None:
        """Simple scaffold bot logic."""
        bail_amount = self._bail_amount()
        auction_action = self._bot_think_active_auction(player)
        if auction_action is not None:
            return auction_action

        if self._is_junior_preset():
            return self._bot_think_junior_preset(player, bail_amount)

        pending_trade_action = self._bot_think_pending_trade(player)
        if pending_trade_action is not None:
            return pending_trade_action

        jail_action = self._bot_think_jail_pre_roll(player, bail_amount)
        if jail_action is not None:
            return jail_action

        pre_roll_economy_action = self._bot_think_pre_roll_economy(player)
        if pre_roll_economy_action is not None:
            return pre_roll_economy_action

        if not self.turn_has_rolled:
            return "roll_dice"
        pending_action = self._bot_think_pending_purchase(player, reserve=200)
        if pending_action is not None:
            return pending_action
        if self.turn_can_roll_again:
            return "roll_dice"
        if self._current_liquid_balance(player) >= 450 and self._options_for_build_house(player):
            return "build_house"
        if self._current_liquid_balance(player) >= 900 and self._options_for_unmortgage_property(player):
            return "unmortgage_property"
        return "end_turn"

    def _initialize_start_runtime(self) -> list[Player]:
        """Initialize generic game runtime state and return active players."""
        self.status = "playing"
        self.game_active = True
        self.round = 1

        active_players = self.get_active_players()
        self._team_manager.team_mode = "individual"
        self._team_manager.setup_teams([player.name for player in active_players])
        self.set_turn_players(active_players)
        return active_players

    def _resolve_start_board_plan(self):
        """Resolve board/preset compatibility and persist normalized options."""
        board_plan = resolve_board_plan(
            self.options.preset_id,
            self.options.board_id,
            self.options.board_rules_mode,
        )
        if board_plan.auto_fixed_from_preset_id is not None:
            self.options.preset_id = board_plan.effective_preset_id
        self.options.board_id = board_plan.effective_board_id
        self.options.board_rules_mode = board_plan.requested_mode
        return board_plan

    def _apply_start_selection(self, board_plan) -> MonopolyPreset:
        """Resolve preset, board metadata, and board structures for startup."""
        preset = self._resolve_selected_preset()
        self.active_preset_id = preset.preset_id
        self.active_preset_name = preset.name
        self.active_family_key = preset.family_key
        self.active_edition_ids = list(preset.edition_ids)
        self.active_anchor_edition_id = preset.anchor_edition_id
        active_board_profile = get_board_profile(board_plan.effective_board_id)
        self.active_board_id = board_plan.effective_board_id
        self.active_board_anchor_edition_id = active_board_profile.anchor_edition_id
        self.active_board_rules_mode = board_plan.requested_mode
        self.active_board_effective_mode = board_plan.effective_mode
        self.active_board_rule_pack_id = board_plan.rule_pack_id or ""
        self.active_board_rule_pack_status = board_plan.rule_pack_status
        self.active_board_auto_fixed_from_preset_id = (
            board_plan.auto_fixed_from_preset_id or ""
        )
        parity_profile = get_board_parity_profile(self.active_board_id)
        if parity_profile is not None:
            self.active_board_deck_mode = parity_profile.deck_mode
            self.active_board_parity_fidelity_status = parity_profile.fidelity_status
            self.active_board_hardware_capability_ids = parity_profile.hardware_capability_ids
        else:
            self.active_board_deck_mode = "classic"
            self.active_board_parity_fidelity_status = "none"
            self.active_board_hardware_capability_ids = ()
        self.active_board_deck_mode = resolve_deck_provider(
            self.active_board_id,
            self.active_board_deck_mode,
        ).mode
        self.active_manual_rule_set = self._load_active_manual_rule_set()
        (
            self.active_board_spaces,
            self.active_space_by_id,
            self.active_color_group_to_space_ids,
        ) = self._resolve_active_board_structures()
        self.active_board_size = len(self.active_board_spaces)
        self.active_sound_mode = "none"
        self.last_hardware_event_id = ""
        self.last_hardware_event_status = "none"
        self.last_hardware_event_details = ""
        return preset

    def _apply_start_profiles(self) -> None:
        """Resolve preset-specific runtime profiles and clear voice/banking caches."""
        self.junior_ruleset = (
            get_junior_ruleset(self.active_preset_id)
            if is_junior_ruleset_preset(self.active_preset_id)
            else None
        )
        self.cheaters_profile = (
            resolve_cheaters_profile(self.active_preset_id)
            if self.active_preset_id == "cheaters"
            else None
        )
        self.cheaters_engine = (
            CheatersEngine(self.cheaters_profile)
            if self.cheaters_profile is not None
            else None
        )
        self.city_profile = (
            resolve_city_profile(self.active_preset_id)
            if self._is_city_preset()
            else None
        )
        self.city_engine = (
            CityEngine(self.city_profile)
            if self.city_profile is not None
            else None
        )
        self.voice_banking_profile = (
            resolve_voice_banking_profile(self.active_preset_id)
            if self.active_preset_id == "voice_banking"
            else None
        )
        if self.active_preset_id == "electronic_banking":
            self.banking_profile = resolve_electronic_banking_profile(self.active_preset_id)
        elif self.voice_banking_profile is not None:
            self.banking_profile = ElectronicBankingProfile(
                preset_id=self.voice_banking_profile.preset_id,
                anchor_edition_id=self.voice_banking_profile.anchor_edition_id,
                source_policy=self.voice_banking_profile.source_policy,
                starting_balance=self.voice_banking_profile.starting_balance,
                pass_go_credit=self.voice_banking_profile.pass_go_credit,
                allow_manual_transfers=True,
                overdraft_policy="no_overdraft",
                provenance_notes=self.voice_banking_profile.provenance_notes,
            )
        else:
            self.banking_profile = None
        self.banking_state = None
        self.voice_last_response_by_player_id.clear()
        self.voice_pending_transfer_by_player_id.clear()

    def _reset_start_state(self) -> None:
        """Reset board, turn, and deck state for a fresh match start."""
        self.rule_profile = self._resolve_rule_profile(self.active_preset_id)
        self.property_owners.clear()
        self.mortgaged_space_ids.clear()
        self.building_levels = {
            space.space_id: 0 for space in self.active_board_spaces if self._is_street_property(space)
        }
        self.pending_trade_offer = None
        self.free_parking_pool = 0
        self._clear_pending_auction()
        self.junior_endgame_evaluating = False
        self.city_endgame_evaluating = False
        self._reset_turn_state()
        self.turn_doubles_count = 0

        self.chance_deck_order = self._manual_deck_ids("chance") or CHANCE_CARD_IDS.copy()
        self.community_chest_deck_order = (
            self._manual_deck_ids("community_chest") or COMMUNITY_CHEST_CARD_IDS.copy()
        )
        if self.chance_deck_order == CHANCE_CARD_IDS:
            random.shuffle(self.chance_deck_order)
        if self.community_chest_deck_order == COMMUNITY_CHEST_CARD_IDS:
            random.shuffle(self.community_chest_deck_order)
        self.chance_deck_index = 0
        self.community_chest_deck_index = 0

    def _reset_players_for_start(self, active_players: list[Player]) -> None:
        """Reset per-player Monopoly runtime fields for startup."""
        for player in active_players:
            if isinstance(player, MonopolyPlayer):
                player.position = 0
                player.cash = (
                    self.banking_profile.starting_balance
                    if self.banking_profile is not None
                    else self.rule_profile.starting_cash
                )
                player.owned_space_ids.clear()
                player.bankrupt = False
                player.in_jail = False
                player.jail_turns = 0
                player.get_out_of_jail_cards = 0
                player.builder_blocks = 0

        self._apply_junior_super_mario_starting_cash()

    def _initialize_banking_for_start(self, active_players: list[Player]) -> None:
        """Create banking simulator accounts when preset uses electronic cash."""
        if self.banking_profile is None:
            return
        player_ids = [
            player.id for player in active_players if isinstance(player, MonopolyPlayer)
        ]
        self.banking_state = init_bank_accounts(player_ids, self.banking_profile)
        self._sync_all_player_cash_from_banking()

    def _announce_start_configuration(self, preset: MonopolyPreset) -> None:
        """Broadcast active startup configuration messages to the table."""
        self.broadcast_l(
            "monopoly-scaffold-started",
            preset=preset.name,
            count=len(self.active_edition_ids),
        )
        if self.active_board_auto_fixed_from_preset_id:
            self.broadcast_l(
                "monopoly-board-preset-autofixed",
                board=self.active_board_id,
                from_preset=self.active_board_auto_fixed_from_preset_id,
                to_preset=self.active_preset_id,
            )
        self.broadcast_l(
            "monopoly-board-active",
            board=self.active_board_id,
            mode=self.active_board_effective_mode,
        )
        if (
            self.active_board_effective_mode == "board_rules"
            and self.active_board_rule_pack_status == "partial"
        ):
            self.broadcast_l(
                "monopoly-board-rules-simplified",
                board=self.active_board_id,
            )

    def on_start(self) -> None:
        """Start scaffold mode using the selected preset metadata."""
        active_players = self._initialize_start_runtime()
        board_plan = self._resolve_start_board_plan()
        preset = self._apply_start_selection(board_plan)
        self._apply_start_profiles()
        self._reset_start_state()
        self._reset_players_for_start(active_players)
        self._initialize_banking_for_start(active_players)

        self._sync_cash_scores()
        self._start_cheaters_turn(self.current_player)
        self._start_city_turn(self.current_player)

        self._announce_start_configuration(preset)

        self.announce_turn(turn_sound="game_pig/turn.ogg")
        BotHelper.jolt_bots(self, ticks=random.randint(12, 20))
        self.rebuild_all_menus()
