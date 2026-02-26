"""Tests for Wave 3 Monopoly board rule-pack modules."""

import pytest

from server.games.monopoly.board_rules import (
    black_panther,
    deadpool_collectors,
    disney_legacy,
    disney_star_wars_dark_side,
    disney_the_edition,
    fortnite_collectors,
    fortnite_flip,
    game_of_thrones,
    ghostbusters,
    lord_of_the_rings_trilogy,
    marvel_avengers_legacy,
    marvel_eternals,
    marvel_falcon_winter_soldier,
    marvel_flip,
    pokemon,
    star_wars_classic_edition,
    star_wars_legacy,
    star_wars_mandalorian_s2,
    star_wars_saga,
    star_wars_solo,
    stranger_things_collectors,
    stranger_things_netflix,
    toy_story,
    transformers,
    transformers_beast_wars,
)

WAVE3_MODULES = [
    (disney_star_wars_dark_side, "disney_star_wars_dark_side", "monopoly-f6167"),
    (disney_legacy, "disney_legacy", "monopoly-19643"),
    (disney_the_edition, "disney_the_edition", "monopoly-40224"),
    (lord_of_the_rings_trilogy, "lord_of_the_rings_trilogy", "monopoly-41603"),
    (star_wars_saga, "star_wars_saga", "monopoly-42452"),
    (marvel_avengers_legacy, "marvel_avengers_legacy", "monopoly-b0323"),
    (star_wars_legacy, "star_wars_legacy", "monopoly-b0324"),
    (star_wars_classic_edition, "star_wars_classic_edition", "monopoly-b8613"),
    (star_wars_solo, "star_wars_solo", "monopoly-e1702"),
    (game_of_thrones, "game_of_thrones", "monopoly-e3278"),
    (deadpool_collectors, "deadpool_collectors", "monopoly-e4833"),
    (toy_story, "toy_story", "monopoly-e5065"),
    (black_panther, "black_panther", "monopoly-e5797"),
    (stranger_things_collectors, "stranger_things_collectors", "monopoly-e8194"),
    (ghostbusters, "ghostbusters", "monopoly-e9479"),
    (marvel_eternals, "marvel_eternals", "monopoly-f1659"),
    (transformers, "transformers", "monopoly-f1660"),
    (stranger_things_netflix, "stranger_things_netflix", "monopoly-f2544"),
    (fortnite_collectors, "fortnite_collectors", "monopoly-f2546"),
    (star_wars_mandalorian_s2, "star_wars_mandalorian_s2", "monopoly-f4257"),
    (transformers_beast_wars, "transformers_beast_wars", "monopoly-f5269"),
    (marvel_falcon_winter_soldier, "marvel_falcon_winter_soldier", "monopoly-f5851"),
    (fortnite_flip, "fortnite_flip", "monopoly-f7774"),
    (marvel_flip, "marvel_flip", "monopoly-f9931"),
    (pokemon, "pokemon", "monopoly-g0716"),
]


@pytest.mark.parametrize(("module", "rule_pack_id", "anchor_id"), WAVE3_MODULES)
def test_wave3_stub_exposes_anchor_and_status(module, rule_pack_id: str, anchor_id: str):
    assert module.RULE_PACK_ID == rule_pack_id
    assert module.ANCHOR_EDITION_ID == anchor_id
    assert module.RULE_PACK_STATUS == "partial"
    assert isinstance(module.PASS_GO_CREDIT_OVERRIDE, int)
    assert module.CAPABILITY_IDS == ("pass_go_credit_override", "startup_board_announcement")
