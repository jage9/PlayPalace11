# Server Architecture

This document describes the server architecture for PlayPalace v11, including module organization, async boundaries, the client-server protocol, and the relationship between network code and game simulations.

## Design Principles

The server has a clear separation between asynchronous network code and synchronous game simulation. The network layer handles connections, authentication, and message routing using async/await with websockets. Game simulations are entirely synchronous and state-based; they run on a tick system and never interact with the network directly.

This separation allows games to be tested without network infrastructure, enables persistence by design, and keeps game logic simple and predictable.

## Module Organization

The server code lives in server and is organized into the following modules:

### core

Contains the fundamental server infrastructure. This includes the main server entry point, websocket connection handling, the async event loop, and the tick scheduler. The tick scheduler calls into tables every 50 milliseconds regardless of game state.

### network

Handles all websocket communication. This module defines the message protocol, serialization format, and provides async functions for sending and receiving messages. It also handles connection lifecycle: accepting connections, tracking connected clients, and cleaning up disconnected clients.

### auth

User authentication and session management. Works with the persistence layer to verify credentials and create sessions. Exposes functions that the network layer calls when handling login/logout messages.

### persistence

SQLite database access using `var/server/playpalace.db`. Stores two things: users (id, username, password) and tables (game type, user list, serialized game dataclass). Uses Mashumaro JSON mixin for game serialization. All database operations happen through this module.

### users

Defines the User abstract class that games interact with. Real network users, test users, and bots all implement this interface. The abstract class provides methods for sending messages to a user and querying their state. Games never import from the network module; they only work with this abstraction.

### tables

Table management. A table holds a list of members and a game instance. Tables are responsible for: tracking who is present, forwarding user actions to the game, and calling the game's tick method. Tables do not manage roles; role systems are game-specific and handled by games themselves using utilities from game_utils.

### games

Contains game implementations. Each game is a dataclass that can be serialized with Mashumaro. Games expose actions that users can take, and these actions modify state imperatively. Games receive the User abstract and call methods on it to send messages; they never touch networking code. Games are responsible for managing their own role systems (player, spectator, judge, etc.) using utilities from game_utils.

### game_utils

Shared utilities for game implementations. Turn order management, role system utilities (to be implemented), common action patterns, and helper functions that multiple games need. Imported by game modules alongside the user abstract. The role system will live here so games can use flexible role definitions beyond the traditional player/spectator split.

### messages

Localization system using Mozilla Fluent via fluent-compiler. Provides functions to render messages for a specific user based on their locale. Uses Babel for list formatting. One .ftl file per game plus one for general UI.

### ui

User interface definitions. Menus, grids, keybinds and their states. Defines the data structures that get serialized and sent to the wxPython client. Keybinds have scopes (global, table) and states (never, idle, active, always).

## Async Boundaries

The async boundary exists at the network layer only. Here is how data flows:

Incoming messages: The network module receives websocket messages asynchronously. It deserializes them and dispatches to the appropriate handler. If the message is a game action, the handler acquires a lock on the relevant table, calls into the synchronous game code, then releases the lock.

Outgoing messages: Games call methods on User objects to send messages. For real network users, these methods queue messages that the network layer sends asynchronously. The game code does not await anything.

Tick loop: An async task runs the tick scheduler. Every 50 milliseconds, it iterates through all tables and calls their tick method synchronously. During a tick, bots may take actions. After the tick completes, queued messages are sent.

## Persistence Strategy

Tables are saved only when explicitly requested or on server shutdown. The game dataclass is serialized to JSON using Mashumaro and stored in the database. This avoids unnecessary disk writes during normal gameplay.

On server startup, all tables are loaded from the database and their games are deserialized. This means the server can restart without losing game state.

During play tests, the game is saved and reloaded at every tick to verify persistence is working correctly. This rigorous save/load cycle only happens in tests, not during normal server operation.

## Testing Integration

Games import only from: their own modules, the user abstract, and game_utils. This makes them easy to test in isolation. Test users implement the User abstract and capture messages for assertion. Play tests create a game, tick it repeatedly while bots take actions, and verify all messages are correct.

Integration tests exercise larger pieces: network handling, persistence, table management. Unit tests cover individual functions.

## Entry Point

The server starts from a main module in core. It initializes the database connection, loads existing tables, starts the websocket server, and begins the tick loop. All of these are async tasks managed by the event loop.

## Client-Server Protocol

All communication uses JSON over websockets. Every packet has a "type" field that identifies the packet type.

### Important: Menu Item Identification

Menu items are identified by string IDs, never by numeric indices. When sending menus to the client, items can be plain strings or objects with text and id fields. When the client sends back events, it includes the menu_id and menu_item_id (the string ID), not numeric positions. This design ensures stability when menus change dynamically and prevents off-by-one errors.

### Server to Client Packets

authorize_success: Sent after successful login. Contains username and server version.

speak: Text message to display and speak via TTS. Contains text and optional buffer name (misc, activity, chats, all).

menu: Display a menu. Contains items (array of strings or objects with text and id), menu_id (string identifier), multiletter_enabled (boolean for type-to-search), escape_behavior (keybind, select_last_option, or escape_event), grid_enabled (boolean), grid_width (number of columns), and optional position (0-based index to select).

request_input: Display an editbox. Contains prompt, input_id (string identifier), default_value, multiline (boolean), and read_only (boolean).

clear_ui: Dismiss all menus and editboxes.

play_sound: Play a sound effect. Contains name, volume (0-100), pan (-100 to 100), and pitch (0-200, where 100 is normal).

play_music: Play background music. Contains name and looping (boolean).

play_ambience: Play ambient sound. Contains intro, loop, and outro filenames.

stop_ambience: Stop ambient sound.

add_playlist: Create a playlist. Contains playlist_id, tracks (array of filenames), audio_type (music or sound), shuffle_tracks, repeats, auto_start, and auto_remove.

start_playlist: Start a playlist. Contains playlist_id.

remove_playlist: Remove a playlist. Contains playlist_id.

disconnect: Disconnect the client. Contains reconnect (boolean indicating if client should attempt reconnection).

chat: Chat message. Contains convo (table or global), sender, message, and language.

table_create: Notification that a table was created. Contains host and game.

update_options_lists: Send available games and languages. Contains games (array of objects with type and name) and languages (object mapping codes to names).

open_client_options: Request client to open its options dialog.

open_server_options: Send server-side user options. Contains options object.

### Client to Server Packets

authorize: Login request. Contains username, password, and version info (major, minor, patch).

menu: Menu selection. Contains menu_id (string) and selection (1-based index for backwards compatibility, but prefer using item IDs).

keybind: Key press while menu is displayed. Contains key (string like "f1", "space", "ctrl+a"), menu_id, menu_index (1-based or null), and menu_item_id (string ID of selected item or null).

escape: Escape key pressed (only sent when escape_behavior is escape_event). Contains menu_id.

editbox: Editbox submission. Contains input_id (string) and text.

chat: Send chat message. Contains convo (table or global), message, and language.

playlist_duration_response: Response to get_playlist_duration request. Contains request_id, playlist_id, duration_type, and duration.

### Menu Item Format

Menu items can be sent in two formats:

Plain string: The item text. No ID is associated with the item.

Object with text and id: The text field is displayed to the user. The id field is a string identifier returned in keybind events as menu_item_id. Always use meaningful string IDs like "leave_table", "start_game", "select_dice_1" rather than numeric identifiers.

Example menu packet:
```json
{
  "type": "menu",
  "menu_id": "game_actions",
  "items": [
    {"text": "Roll dice", "id": "roll"},
    {"text": "Hold", "id": "hold"},
    {"text": "Leave game", "id": "leave"}
  ],
  "multiletter_enabled": false,
  "escape_behavior": "select_last_option"
}
```

### Event Flow Example

1. Server sends menu with menu_id "turn_menu" and items with IDs "roll", "hold", "leave".
2. User navigates to "Hold" and presses Enter.
3. Client sends menu packet with menu_id "turn_menu" and selection 2.
4. Alternatively, if user presses F5 while "Hold" is highlighted, client sends keybind packet with key "f5", menu_id "turn_menu", menu_index 2, and menu_item_id "hold".
5. Server handles the event using menu_item_id "hold" to determine the action, not the numeric index.
