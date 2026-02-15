# Chat Buffer Notes (Follow-up)

We reverted to server-sent `chat` packets so the client’s existing mute/language
logic continues to work. Server-side chat routing now only decides *who* receives
chat (table vs lobby vs global). The client still applies:

- `mute_table_chat` / `mute_global_chat`
- language subscription filters
- chat sound selection + buffer routing

This keeps behavior consistent with existing preferences, but it also leaves
chat filtering in client code that is currently large and partly commented out.

## Follow-up ideas
- Revisit the client chat handler and either:
  - cleanly re-enable language filtering, or
  - move mute/language decisions server-side and simplify the client.

## Decision needed
- Prefer to keep chat filtering on client (current) or move to server?
- If moved to server, define how muted chats should be handled (suppressed vs
  `muted=True` speak packets).
