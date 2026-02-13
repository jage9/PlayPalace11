# Rules Of Toss Up
PlayPalace team, 2026.

## TL;DR
Toss Up is a push-your-luck dice game where you roll a handful of colored dice. Each die lands on green, yellow, or red. Green dice score you points and are removed. Yellow dice are not removed but otherwise do nothing. Red dice also stick around, and but you have them (exact conditions depending on variant) you could bust and lose all your turn points.

The concept is simple: keep rolling to accumulate points, or bank what you have and pass the turn. First player to reach the target score wins.

## Gameplay
The game is played in rounds, with each player taking one turn per round. On your turn, you start with a pool of dice (10 by default, though this can be configured between 5 and 20).

When you roll, each die lands on one of three colors:

* **Green:** You score 1 point per green die, and those dice are removed from your pool.
* **Yellow:** These dice do nothing, staying in your pool for the next roll. They are safe, but not always helpful.
* **Red:** These dice stay in your pool. They do not score, and they do not go away, so you have to roll them again.

After a roll, if you are not busted (see below), you can choose to **roll again** with your remaining dice, or **bank** your accumulated turn points, adding them to your total score.

If all of your dice are removed (that is, they've all come up green), you receive a fresh set of dice at the starting count and can keep going. This is similar to "hot dice" in other games and can lead to very large turns if fortune favors you.

### Bust Conditions
How you bust depends on which rules variant you are playing:

* **Standard (default):** You bust if you roll **no green dice and at least one red die**. In other words, you need at least one green to stay alive, unless the roll is entirely yellow.
* **PlayPalace:** You bust only if **every single die lands on red** (no greens and no yellows at all). This is more forgiving, as even a single yellow die will keep you in the game.

When you bust, all the points you accumulated during the current turn are lost, and your turn ends immediately.

### Dice Probabilities
The odds of each color differ between variants:

* **Standard:** Each die has a 3-in-6 (50%) chance of green, 2-in-6 (33.3%) chance of yellow, and 1-in-6 (16.7%) chance of red.
* **PlayPalace:** Each die has an equal 1-in-3 (33.3%) chance of each color.

This means Standard gives you better odds of scoring greens, but it is easier to bust since even a single red with no greens ends your turn. PlayPalace gives fewer greens on average, but busting requires every die to land red, which becomes increasingly unlikely with more dice.

### Winning
At the end of each round, the game checks whether any player has reached or exceeded the target score (default 100, configurable from 20 to 500). If exactly one player has, that player wins. If multiple players are tied at or above the target, those players enter a **tiebreaker round** where only they participate. Non-tied players sit out as spectators until the tie is resolved.

### Example Turn
It is Round 1 and you are up first with 10 dice.

You roll: 5 green, 3 yellow, 2 red. You score 5 points, and the 5 green dice are removed. You now have 5 dice remaining (the yellows and reds).

You decide to push your luck and roll again: 3 green, 1 yellow, 1 red. You pick up 3 more points (8 total for the turn), and the green dice are removed. You now have 4 dice left.

Things are looking risky with only 2 dice in your pool. In Standard rules, you need at least one green to survive a roll, and with only 2 dice, the odds are not great. You decide to bank your 6 points and end your turn safely.


### Scoring
Scoring in Toss Up is straightforward:

* Each **green die** is worth **1 point**.
* Yellow and red dice are worth nothing.
* Points accumulate across rolls within a turn, but are only added to your total score when you **bank**.
* **Busting** forfeits all points earned during the current turn (your banked total is unaffected).

## Keyboard Shortcuts
Shortcuts specific to the game of Toss Up:
* R: Roll the dice.
* B: Bank your points.

## Game Theory / Tips
* With more dice in your pool, the odds of busting are lower. In Standard rules, busting with 10 dice is extremely unlikely since you need all dice to avoid green while at least one hits red. The danger ramps up sharply as your pool shrinks to 3 dice or fewer.
* In Standard rules, a pool of 1 die has a 1-in-6 chance of busting (landing red), while 2 dice have roughly a 1-in-12 chance of busting (both non-green with at least one red). Consider banking when you are down to 2 or 3 dice, especially if you have a decent haul.
* In PlayPalace rules, busting requires every die to be red. With 2 dice that is a 1-in-9 chance; with 3 dice it is 1-in-27. You can afford to be more aggressive, but do not get overconfident with very small pools.
* Getting a fresh set of dice when your pool empties is quite common in this game; turns of twenty or even more points are really not that rare. Don't be afraid to take risks.
