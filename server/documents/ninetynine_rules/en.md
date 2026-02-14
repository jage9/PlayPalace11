# Rules Of Ninety Nine
PlayPalace team, 2026.

## TL;DR
Ninety Nine is a classic card game of survival and strategy. Players take turns playing cards that add to (or sometimes subtract from) a shared running total, and the goal is simple: don't be the one to push it over 99.

The game has been a staple in the blind gaming community for years, appearing in both the Quentin C Playroom and RS Games platforms. Each platform brought its own twist to the rules, and PlayPalace supports both variants. At its core, Ninety Nine is an elimination game: every player starts with a set of tokens, loses them for making mistakes, and is knocked out when they run dry. The last player standing wins.

## Gameplay
Ninety Nine is played in rounds. At the start of each round, the running count resets to 0, and every surviving player is dealt a fresh hand of cards (3 by default, though the host can adjust this from 1 to 13).

On your turn, you play one card from your hand. That card modifies the running count in some way -- most cards simply add their face value, but certain special cards do something different. After you play a card, you draw a replacement from the deck (this happens automatically by default, but the host can switch to manual draw mode). Then the turn passes to the next player.

The round continues until someone pushes the count over 99 (a "bust"), or until someone has no cards left and thus cannot play. When a round ends, the offending player loses tokens, a new round begins, and everyone who still has tokens is dealt a fresh hand.

Players who lose all their tokens are eliminated. The game continues until only one player remains.

### Card Values
The cards behave differently depending on which variant you're playing.

#### Quentin C Variant (default)
This variant uses a standard 52-card deck (Ace through King in four suits). Here is what each card does:

* **Ace**: Adds 1 or 11 to the count. You choose which. However, if the count is above 88, the game automatically plays it as +1 (since +11 would bust you).
* **2**: A wildcard. If the count is even and above 49, the 2 divides the count in half. Otherwise, it doubles the count. This card can be incredibly powerful or incredibly dangerous.
* **3 through 8**: Add their face value to the count. A 3 adds 3, a 7 adds 7, and so on.
* **9**: A pass card. It adds 0 to the count -- your turn ends without changing anything. Very valuable in tight spots.
* **10**: Adds 10 or subtracts 10 from the count. You choose which. If the count is 90 or above, the game automatically plays it as -10.
* **Jack**: Adds 10 to the count and skips the next player's turn.
* **Queen**: Adds 10 to the count.
* **King**: Adds 10 to the count.
* **4**: Adds 4 to the count and reverses the turn direction (in games with more than 2 players).

#### RS Games Variant
This variant uses a special 60-card deck with number cards (1-9) and six types of special cards, four copies of each:

* **1 through 9**: Add their face value to the count.
* **+10**: Adds 10 to the count.
* **-10**: Subtracts 10 from the count.
* **Pass**: Adds 0 to the count. Your turn ends without changing anything.
* **Reverse**: Adds 0 to the count and reverses the turn direction (in games with more than 2 players).
* **Skip**: Adds 0 to the count and skips the next player's turn.
* **Ninety Nine**: Sets the count to exactly 99, regardless of what it was before.

### Milestones and Penalties (Quentin C Variant)
In the Quentin C variant, the numbers 33, 66, and 99 are milestones, and they add a layer of strategy that the RS Games variant doesn't have.

* **Landing exactly on 33 or 66** (with a card that increases the count): Every other player loses 1 token. This is great for you.
* **Passing through 33 or 66** (your card takes the count from below to above the milestone without landing on it): You lose 1 token. This is bad.
* **Landing exactly on 99** (with a card that increases the count): Every other player loses 2 tokens, and the round ends. This is the best move in the game.
* **Going over 99** (busting): You lose 2 tokens and the round ends.

In the RS Games variant, milestones don't exist. Going over 99 simply costs the offending player 1 token.

### Running Out of Cards
If the deck runs out, the discard pile is reshuffled into a new deck. If you end up with no cards in your hand on your turn (because you forgot to draw more when auto-draw was disabled), you lose 3 tokens and a new round begins.

### Example Turn
You're playing Quentin C rules. The count is at 27, and your hand is a 6, a 9, and a King.

Playing the 6 would bring the count to 33 -- that's a milestone! Every other player would lose 1 token, and you'd have pulled off a very nice move.

Playing the King would bring the count to 37. That means you just passed through 33 (going from 27 to 37 without landing on it), so you'd lose 1 token yourself. Bad idea.

Playing the 9 would leave the count at 27, which is safe but doesn't accomplish anything special.

You play the 6. The count is now 33, and each of your opponents loses 1 token. You draw a replacement card, and the turn passes to the next player -- who now has to deal with a count of 33.

### Scoring
This game doesn't use a point-based scoring system. Instead, each player starts with a pool of tokens (9 by default, configurable from 1 to 50). Tokens are lost as penalties:

#### Quentin C Variant
* **Busting (going over 99):** Lose 2 tokens
* **Passing through 33 or 66:** Lose 1 token
* **Landing on 33 or 66:** Every other player loses 1 token
* **Landing on 99:** Every other player loses 2 tokens
* **Running out of cards:** Lose 3 tokens

#### RS Games Variant
* **Busting (going over 99):** Lose 1 token
* **Having no safe card to play:** Lose 1 token (the game detects this automatically and ends the round)
* **Running out of cards:** Lose 3 tokens

When a player reaches 0 tokens, they are eliminated. The last player with tokens wins.

## Keyboard Shortcuts
Shortcuts specific to the game of Ninety Nine:
* Space or D: Draw a card (when manual draw mode is enabled).
* C: Check the current count.
* H: Check the cards in your hand.

## Game Theory / Tips
* **Hoard your special cards.** Aces, 9s, 10s, and 2s (Quentin C) or Pass, Skip, -10, and Reverse cards (RS Games) are your lifelines. Don't waste them early when the count is low and safe. Save them for when the count is in dangerous territory and you need an escape.
* **Aim for milestones in Quentin C.** Landing on 33, 66, or 99 punishes your opponents. If you can engineer a play that hits one of these numbers, do it. Conversely, be very careful not to pass through them -- that costs you a token.
* **Set traps at 31 or 97.** In a 2-player Quentin C game, leaving the count at 31 or 97 is devastating. Your opponent has almost no way to avoid either passing through 33 or busting over 99. Only a 9, an Ace played as +1, or a 10 played as -10 can save them.
* **Be careful with the 2 card.** In Quentin C, the 2 either doubles or halves the count. If the count is even and above 49, it divides by 2 (potentially a huge relief). Otherwise, it multiplies by 2 (potentially catastrophic). Make sure you know which one will happen before you play it.
* As an additional note, you can play a 2 when the count is 33 to take it immediately to 66 (thus causing everyone else to lose a token).
* **Watch the 4 and Jack carefully.** The 4 reverses direction and the Jack skips a player (Quentin C). In a 2-player game, the Jack's skip effectively gives you another turn -- which means you're also responsible for the next play. Don't play a Jack into a position that traps yourself.
* **Pay attention to what others are holding.** You can't see their cards, but you can count how many special cards have been played.
