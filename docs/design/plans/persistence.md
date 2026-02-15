# Persistence And Server
Few things in PlayPalace actually need custom persistence handling, since games are automatically persistent by their nature.

What the server saves (using sqlite, in `var/server/playpalace.db`):
* users; with IDs, usernames, and passwords
* Tables; with type of game, user list, and a game dataclass
And that's all.
