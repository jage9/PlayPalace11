# Roulette round verification

The automated play check in `server/tests/test_roulette_round_completion.py`
starts every game through a real table and Roulette wheel, with each game's
unchanged default options and a supported player count. It drives ordinary bot
actions and ticks to completion; it never calls a finish method to force a result.
Two seeds (734 and 2026) run in both rounds and score modes: 140 simulations.

The checks verify the expected completion hook, a single round result, awards,
aggregate persistence when the session ends, and no additional awards or new
rounds after completion. Separate regressions cover Pusoy Dos instant wins and
Backgammon's mandatory-die move restriction.

## Round boundaries

Games without a shorter scored unit use one complete game, as agreed. A normal
win can end a game before every player completes a turn cycle; draws retain the
game's normal outcome.

| Game | One Roulette round |
| --- | --- |
| Age of Heroes | One complete day; score mode counts cities gained |
| Backgammon | One scored game |
| Battleship | One complete game |
| Blackjack | One dealt hand, including dealer settlement |
| Cards Against Humanity | One prompt, submissions, and judging cycle |
| Chaos Bear | One complete game |
| Chess | One complete game, including a normal draw |
| Coup | One complete game |
| Crazy Eights | One hand |
| Dominos | One hand, ending on an empty hand or blocked board |
| Farkle | One turn per active player |
| Five Card Draw | One hand, ending in showdown or an uncontested pot |
| Hold'em | One hand, ending in showdown or an uncontested pot |
| Last Card | One hand, including a deadlock outcome |
| Left Right Center | One complete game |
| Light Turret | One turn cycle, or earlier natural elimination |
| Ludo | One complete game |
| Metal Pipe | One complete game (a single bonk with default rules) |
| Midnight | One turn per active player |
| Mile by Mile | One race |
| Nine | One complete hand |
| Ninety Nine | One round ending in its normal bust or hand resolution |
| Pig | One turn per active player |
| Pirates | One turn cycle, or earlier collection of the final gem |
| Pusoy Dos | One hand, including an instant-win deal |
| Rolling Balls | One turn cycle, or earlier exhaustion of the pipe |
| Scopa | One complete deck, followed by round scoring |
| Senet | One complete game |
| Snakes and Ladders | One complete game |
| Sorry | One complete game |
| Threes | One completed turn/score per player |
| Toss Up | One turn per active player |
| Tradeoff | One completed turn per player, with round scores committed |
| Twenty One | One duel round through damage resolution |
| Yahtzee | One scored category per player |

This verifies default-rule bot play, not every possible deal, player count,
nondefault preset, or human interaction. Client focus, speech, and audio still
need real-client play testing.
