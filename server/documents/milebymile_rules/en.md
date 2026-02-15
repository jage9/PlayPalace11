# Rules Of Mile By Mile
PlayPalace team, 2026.

## TL;DR
Mile by Mile is a racing card game based on the classic French game Mille Bornes, which was created in 1954 by Edmond Dujardin. The name "Mille Bornes" translates to "a thousand milestones," referring to the kilometer markers along French roads.

The goal is simple: race your car to the finish line by playing distance cards, while throwing hazards at your opponents to slow them down and using remedies and safeties to keep yourself moving. The game is played over multiple races, and the first player or team to reach a winning score total takes the victory.

## Gameplay
A game of Mile by Mile consists of multiple races. Each race, every player (or team) starts stopped and must get going before they can cover any distance. Players take turns drawing a card and then either playing a card or discarding one.

On your turn, you automatically draw a card from the deck, bringing your hand up to 7 cards (the starting hand size is 6). You then choose one card to play or discard. Your cards fall into four categories.

### Distance Cards
These are the core of the game. Playing a distance card adds that many miles to your total for the current race. The available distances are 25, 50, 75, 100, and 200 miles. You can only play distance cards when your car is moving (i.e., you have no critical problems like being stopped, having a flat tire, being out of gas, or being in an accident). If you have a Speed Limit problem, you can only play distance cards worth 50 miles or less.

By default, the "perfect crossing" rule is enabled, meaning you must reach exactly the target distance -- you cannot overshoot it. For example, if the race distance is 1,000 miles and you have 925, you cannot play a 100-mile card.

### Hazard And Remedy Cards
There are five types of hazards, each with a corresponding remedy:

* **Stop**: Forces the target to stop. They need a Green Light to get moving again.
* **Speed Limit**: Restricts the target to playing distance cards of 50 miles or less. Does not stop them entirely.
* **Out of Gas**: Stops the target. They need Gasoline to fix this.
* **Flat Tire**: Stops the target. They need a Spare Tire to fix this.
* **Accident**: Stops the target. They need Repairs to fix this.

All hazards except Speed Limit also cause the target to become stopped (adding a Stop problem on top of the specific hazard). This means that after fixing the specific problem, they still need a Green Light to resume driving -- unless they have the Right of Way safety.

By default, you cannot stack critical hazards on someone who already has one. The "allow stacking attacks" option changes this behavior.

When you play a hazard, if there are multiple valid targets, you will be prompted to choose which opponent to attack.

### Safety Cards
These are powerful cards that provide permanent protection for the rest of the race. There is exactly one of each in the deck:

* **Extra Tank**: Protects against Out of Gas. If played while you have an Out of Gas problem, it also fixes it.
* **Puncture Proof**: Protects against Flat Tire. If played while you have a Flat Tire, it also fixes it.
* **Driving Ace**: Protects against Accident. If played while you have an Accident, it also fixes it.
* **Right of Way**: Protects against both Stop and Speed Limit. If played while you have either problem, it removes both. You will never need to play a Green Light again for the rest of the race.

Playing a safety card grants you an extra turn -- you immediately draw a replacement card and get to play again.

### Dirty Tricks (Coup Fourre)
This is one of the most satisfying plays in the game. When an opponent plays a hazard on you, there is a brief window (about 3 seconds) during which you can counter it by playing the matching safety card from your hand. This is called a "dirty trick" (from the French "Coup Fourre"). Press D when the window is open and you have the right safety card in hand. A successful dirty trick not only blocks the hazard but also gives you bonus points at the end of the race (300 points per dirty trick).

### Discarding
If you cannot or do not want to play any card, you can discard a card from your hand instead. Select the card you wish to discard and press Shift+Enter or Backspace. By default, you are allowed to discard any card, even playable ones. The "always allow discarding" option can be toggled off to prevent discarding playable cards.

### Deck Exhaustion
By default, when the draw pile runs out, the discard pile is reshuffled to form a new deck. This can be disabled with the "reshuffle discard pile" option. If reshuffling is disabled and the deck runs out and all hands are empty, the race ends and the team with the most miles is considered the winner of that race.

### Example Turn
It is the start of a race and you are first to play. Your hand contains: Green Light, 100 miles, 50 miles, Speed Limit, Spare Tire, Out of Gas.

You draw a card and get 75 miles. Since everyone starts stopped, you need to get moving first. You play your Green Light, removing your Stop condition. Because you only played a remedy (not a safety), your turn ends.

Next turn comes around and you draw another card -- say, 200 miles. You are now moving with no problems, so you play your 200-mile card, bringing your total to 200 miles.

A few turns later, an opponent plays a Flat Tire on you. You happen to have the Puncture Proof safety in your hand. You quickly press D within the 3-second dirty trick window, playing your Puncture Proof as a dirty trick. The Flat Tire is blocked, you gain permanent puncture protection, you draw a replacement card, and you get to take another turn immediately. Plus, you will earn 300 bonus points at the end of the race for the dirty trick.

### Scoring
At the end of each race, every team earns points based on several factors:

#### Base Score
* **Distance traveled**: 1 point per mile covered (up to the race distance).

#### Winner Bonuses (only for the team that completed the journey)
* **Trip Complete**: 400 points for reaching the target distance.
* **Perfect Crossing**: 200 points for reaching exactly the target distance (only awarded when the "perfect crossing" option is disabled, since otherwise all completions are exact by definition).
* **Safe Trip**: 300 points for completing the race without using any 200-mile cards.
* **Shut Out**: 500 points if all opponents have 0 miles.

#### Bonuses for All Teams
* **Safety Cards**: 100 points per safety card played during the race.
* **All Four Safeties**: 300 additional points if all four safety cards were played.
* **Dirty Tricks**: 300 points per successful dirty trick (Coup Fourre).

The game continues with new races until a team's total score reaches or exceeds the winning score (default 5,000 points). The team with the highest score at that point wins.

### Game Options
* **Race Distance** (default 1,000): The target distance for each race, from 300 to 3,000 miles.
* **Winning Score** (default 5,000): The total score needed to win the game, from 1,000 to 10,000.
* **Team Mode**: Play individually or in teams. Supports 2 to 9 players.
* **Perfect Crossing** (default on): Require reaching exactly the target distance.
* **Allow Stacking Attacks** (default off): Allow multiple critical hazards on one opponent.
* **Reshuffle Discard Pile** (default on): Reshuffle the discard pile when the deck runs out.
* **Karma Rule** (default off): Adds a karma mechanic. Requires at least 3 teams. Teams start with karma, and attacking costs you your karma. When both attacker and target have karma, the attack is neutralized and both lose karma. A team without karma cannot attack a team that has karma. The False Virtue special card restores your karma.
* **Deck Rigging** (default None): Modify the deck composition. Options include "No Duplicates" (avoid drawing duplicate cards), "2x Attacks" (double the hazard cards), and "2x Defenses" (double the remedy cards).
* **Always Allow Discarding** (default on): Allow discarding even when you have playable cards.

## Keyboard Shortcuts
Shortcuts specific to the game of Mile by Mile:
* S: Check the status of all players/teams (miles, problems, safeties, and scores).
* Shift+S: Show detailed status in a status box.
* D: Play a dirty trick (Coup Fourre) when the window is open.
* Shift+Enter: Discard the currently selected card.
* Backspace: Discard the currently selected card (alternative to Shift+Enter).
* Enter: Play the currently selected card (from the card menu).

## Game Theory / Tips
* The dirty trick is one of the highest-value plays in the game. If you have a safety card that matches a hazard an opponent might play on you, sometimes it is worth holding onto it rather than playing it outright -- 300 bonus points for a successful dirty trick plus the 100 safety points is much better than just the 100 safety points from playing it normally. Of course, you are gambling that the opponent actually attacks you with the matching hazard.
* Right of Way is arguably the best safety card. It protects against both Stop and Speed Limit, eliminating the need for Green Light cards entirely for the rest of the race. If you draw it, think carefully about whether to play it immediately or hold it for a dirty trick.
* Pay attention to the 200-mile card. Using one costs you the 300-point Safe Trip bonus if you win the race. If you are close to the finish and have smaller distance cards that can get you there, consider whether the Safe Trip bonus is worth passing up the 200-mile play.
* When deciding whether to attack, consider how many miles your target has versus you. Attacking the player closest to the finish line is usually the right call. The bot AI uses this exact strategy.
* Discarding is not failure. If your hand is full of remedies you do not need or hazards you cannot play, clearing out dead weight to draw something useful next turn is a perfectly valid strategy. In general you should keep one of each remedy for hazards you aren't immune to.
