# Game Developer's Guide

This document describes the process for implementing new games in PlayPalace v11. These steps are followed rigidly by the Xtreme Games Development Group. They work well for both human developers and AI agents.

The process may look like a lot, but for an AI agent it typically takes around 20-40 minutes for medium to large games. This is significantly faster than other approaches we've tried.

## Step 1: Onboard by Reading Existing Games

If you haven't implemented a PlayPalace game before, read at least one existing game that's close to what you're building.

**Pig** - Start here if your game is simple. Pig demonstrates the basics: turn order, actions, scoring, win conditions. It's around 200 lines and easy to understand.

**Mile by Mile** - Good for card games. Shows hand management, drawing, playing cards, and the card utility classes.

**Scopa** - Read this for complex games. Demonstrates team play, capture mechanics, multiple scoring conditions, and how to break logic into separate modules. It's the most sophisticated example.

**Light Turret** or **Chaos Bear** - Good examples of RB Play Center style games with spatial elements.

Pay attention to:
- How the game dataclass is structured
- How the game initializes when it starts
- How bot timing is handled on each tick
- How actions are defined and executed
- How turn order is managed
- How the game ends

Also read the localization files. These show you what good screen reader friendly messages look like.

## Step 2: Write the Localization File

Before writing any game code, create the English localization file with all messages you'll need.

This step is not optional. Writing messages first forces you to think through the game flow: what happens on each turn, what feedback players receive, how scores are announced, what the win condition looks like. The localization file becomes your plan.

Think carefully about what information players need at each moment. Screen reader users rely entirely on these messages to understand the game state.
Use the **table** buffer for game flow so it reads as a table transcript: prefer `broadcast()` / `broadcast_l()` and `broadcast_personal_l()` for gameplay output (including “you” vs “player” split messages).
Reserve `user.speak()` / `user.speak_l()` for direct command responses (e.g., "read top card", "no saved tables").

### Writing Good Messages

Scopa's localization file is an excellent example of screen reader friendly messages. Here's what makes them good:

**Clear action feedback with context:**
```ftl
scopa-you-collect = You collect { $cards } with { $card }
scopa-player-collects = { $player } collects { $cards } with { $card }
```
The player knows exactly what happened: who did it, what they collected, and what card they used to do it.

**Explain scoring, don't just announce it:**
```ftl
scopa-most-cards = { $player } scores 1 point for most cards ({ $count } cards).
scopa-most-diamonds = { $player } scores 1 point for most diamonds ({ $count } diamonds).
```
Don't just say "Alice scores 1 point." Say *why* they scored. This helps players learn the game and verify the scoring is correct.

**Handle edge cases explicitly:**
```ftl
scopa-most-cards-tie = Most cards is a tie - no point awarded.
scopa-seven-diamonds-tie = 7 of diamonds is a tie - no point awarded.
```
When something unusual happens, explain it. Silence is confusing.

**Running totals, not just deltas:**
```ftl
scopa-round-score-line = { $player }: +{ $round_score } (total: { $total_score })
```
Players want to know both what just changed and where they stand overall.

**Distinct messages for you vs others:**
```ftl
scopa-you-put-down = You put down { $card }.
scopa-player-puts-down = { $player } puts down { $card }.
```
"You" is clearer than hearing your own name, and it helps distinguish your actions from others'.

## Step 3: Write the Game

If you're an AI agent, write the entire game in one go. You have your localization file as a plan. Use it.

Look at the existing games for the structure you need. The key constraints are:
- All state must be in dataclass fields for serialization to work
- Games communicate through the User abstraction, never directly to the network
- Use the action system for player choices
- Follow the patterns you saw in step 1

**Buffer rule of thumb:** if a message advances game state or narrates table action, route it to the **table** buffer. Use `broadcast()` / `broadcast_l()` and `broadcast_personal_l()` for “you” vs “player” messages. Reserve `user.speak()` / `user.speak_l()` for direct command responses (e.g., “read top card”, “no saved tables”).

## Step 4: Test with the CLI

Test your game using the CLI tool. This catches most bugs quickly.

Run a basic simulation with two bots to see if the game completes. Then test with more players. Then test with the serialization flag, which saves and restores game state after every tick.

If your game breaks after a save/load cycle, you have state that isn't being serialized properly. Common causes are using regular classes instead of dataclasses, or storing non-serializable objects in game state.

If you're an AI agent, fix any bugs autonomously. Read the error messages, trace through the code, and correct the issues. Most bugs at this stage are straightforward.

## Step 5: Modularize if Needed

If your game exceeds 800 lines, consider splitting it into modules. Scopa is a good example of this - it separates capture logic and scoring into their own files.

Good candidates for extraction:
- Complex scoring calculations
- AI/bot decision logic
- Card or piece manipulation utilities
- Validation logic

Keep the main game file focused on game flow. Extract the details.

## Step 6: Test Again

Run the CLI tests again after any refactoring. Make sure the game still completes and serialization still works.

## Step 7: Write Unit Tests

Create a test file for your game. Look at existing test files for the patterns. You want:

**Unit tests** for individual functions and edge cases.

**Play tests** that run complete games with bots and verify they finish.

**Persistence tests** that save and load game state and verify nothing is lost.

## Step 8: Done

Your game is complete. Run the full test suite to make sure you haven't broken anything else. If all tests pass, the game is ready.

## Summary

1. Read an existing game to onboard
2. Write localization file (it's your plan)
3. Write the game in one go
4. Test with CLI, including serialization
5. Modularize if over 800 lines
6. Test again
7. Write unit tests
8. Done

This process is designed for speed and reliability. The localization-first approach prevents false starts. The CLI testing catches most bugs immediately. The serialization tests catch persistence issues before they become problems in production.

For AI agents: this workflow is optimized for you. You can hold the entire game in context, write it completely, and iterate on bugs quickly. 20-40 minutes is typical for medium to large games.
