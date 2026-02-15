# Simulation
For this project, we hold the view that the game simulation should be stored entirely as state. If your game can't be saved and loaded without any custom save/load code, you have failed in this regard.

We use Mashumaro's json mixin for saving games. You don't need to mark all your dataclasses as serializable in this way, only the game class itself. It does, however, mean that all your classes should be dataclasses

Games *never* send network packets directly to the user. Games get things that implement the 'User' class (which is an abstract), and can thus make certain guarantees. However, the things to which they are sending messages might not be users at all: they could be normal users, test users with special debug code, bots (though I don't know why you'd want to do this) - the game internally doesn't need to know or care.

This helps for testing, because the game usually only needs to import from:
* its own modules
* user abstract
* game-utils module

It's also ideal that there is a layer between 'action in a game' and 'event received from a user'. Bots are allowed to call into actions just fine on tick; they are designed this way for that exact reason.

A tick happens every fifty milliseconds, and is called no matter the phase of the table: waiting, main, auction, between_rounds, etc etc.

We recommend that all game state be changed imperatively, not declaratively. Actions should not return a result that ends a turn: they should just end it, using the appropriate action that automatically handles turn order, sending out messages to players and so on.
