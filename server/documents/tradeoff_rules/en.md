# Rules Of Tradeoff
PlayPalace team, 2026.

## TL;DR
Tradeoff is a dice trading game for 2 to 8 players. Think of it as a blend of set collection and negotiation by way of a shared pool -- you roll dice, decide which ones you do not want, toss them into a communal pot, and then take replacements back out, one at a time, trying to assemble the best combinations you can.

Each round consists of three iterations of rolling, trading, and taking. After the third iteration every player has accumulated exactly 15 dice, and those dice are scored based on the sets they form. The first player to reach the target score (60 points by default) wins.

It was created by Rory Michie in 2026 with help from the PlayPalace team, particularly Zarvox, and not much is known for certain about how exactly to play the game optimally.
## Gameplay
A game of Tradeoff is played over multiple rounds. Each round has three iterations, and every iteration follows the same two-phase structure: a **trading phase** and a **taking phase**.

### The Trading Phase
At the start of each iteration every player simultaneously rolls 5 dice. All five of your dice are marked for trading by default, so you need to decide which ones you actually want to **keep**. Toggle dice between "keeping" and "trading" until you are happy with your selection, then confirm your trades.

Once every player has confirmed, the game reveals what each person traded. All traded dice are tossed into a shared **pool**. The dice you chose to keep go straight into your **hand**, which carries over across all three iterations of the round.

You are free to trade anywhere from zero to all five of your rolled dice -- but keep in mind that however many you trade, you will take back exactly that many from the pool.

### The Taking Phase
Players take dice from the pool one at a time, in a round-robin order. The turn order is determined by total score -- the player with the **lowest** score picks first, with ties broken by the sum of dice already in hand (lower goes first). If there is still a tie, it is broken randomly.

On your turn you choose any single die from the pool (by its face value) and it is added to your hand. Play then passes to the next eligible player, wrapping around until everyone has taken back the same number of dice they traded.

### After Three Iterations
Once the third iteration's taking phase is complete, every player will have accumulated exactly 15 dice in their hand. The game then scores each player's hand automatically, finding the best possible combination of non-overlapping sets (see Scoring below). The points earned are added to the player's running total.

If nobody has reached the target score, a new round begins and hands are cleared.

### Example Turn
Suppose you are in a three-player game and it is the second iteration of round one. You already have 5 dice in your hand from the first iteration: 3, 3, 3, 5, 5.

You roll: 2, 3, 5, 5, 6. You would love more threes and fives for set-building purposes, so you keep the 3 and both 5s, and trade the 2 and the 6. After confirming, those two dice go into the pool.

The other players make their trades too. The pool now contains, say: 2, 6, 1, 4, 4, 5. Because you traded 2 dice, you get to take 2 back. You have the lowest score, so you pick first. You grab the 5 (to work toward a group of five 5s), and then -- after the other players each take one -- it comes back to you and you grab the 4 (no better options left).

Your hand is now: 3, 3, 3, 3, 4, 5, 5, 5, 5, 5. Heading into the third iteration you already have a triple of 3s (3 points) and a group of five 5s (8 points) shaping up nicely.

### Scoring
At the end of each round the game finds the highest-scoring combination of non-overlapping sets from your 15 dice. From lowest to highest point value, the possible sets are:

* **Triple** (3 of the same value): 3 points
* **Mini Straight** (4 consecutive values, e.g. 2-3-4-5): 7 points
* **Group** (5 of the same value): 8 points
* **Double Triple** (3 of one value + 3 of another, 6 dice): 10 points
* **Straight** (5 consecutive values, e.g. 1-2-3-4-5 or 2-3-4-5-6): 12 points
* **Double Group** (5 of one value + 5 of another, 10 dice): 30 points
* **All Groups** (5 of three different values, all 15 dice): 50 points
* **All Triplets** (3 of five different values, all 15 dice): 50 points

The game automatically finds the optimal combination of sets -- you do not choose which sets to claim. For example, if forming a Double Triple plus a separate Triple scores higher than forming three individual Triples, the game will pick the better option for you.

## Keyboard Shortcuts
Shortcuts specific to the game of Tradeoff:

* 1-5 (PlayPalace style): Toggle the corresponding die (by position) between keeping and trading.
* 1-6 (Quentin C style): Keep the first die with that face value (remove it from trading).
* Shift+1-6 (Quentin C style): Trade the first die with that face value (add it to trading).
* B: Confirm your trades.
* H: View your current hand (during the taking phase).
* P: View the current pool of traded dice.
* V: View all players' hands and what they traded (during the taking phase).

## Game Theory / Tips
The specifics of good Tradeoff play are still very much up for debate, so this section is being left empty for now.
