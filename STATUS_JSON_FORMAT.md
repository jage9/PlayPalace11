# Status JSON Format Documentation

## Overview

The PlayPalace server writes a `status.json` file periodically (every ~1 second) that external systems (like the website) can read to get real-time server status and player information.

## Enabling Status File Output

Run the server with the `--status-file` option:

```bash
python -m server.main --host 0.0.0.0 --port 8000 --status-file /path/to/status.json
```

## File Format

```json
{
  "version": "11.2.2",
  "online": true,
  "timestamp": 1705969000,
  "players": {
    "count": 3,
    "list": ["player1", "player2", "player3"]
  },
  "tables": {
    "count": 2,
    "active": 1
  }
}
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `version` | string | Server version (e.g., "11.2.2") |
| `online` | boolean | Whether server is running (always true in this file) |
| `timestamp` | integer | Unix timestamp when status was last updated |
| `players.count` | integer | Number of currently online players |
| `players.list` | array | List of online player usernames, sorted alphabetically |
| `tables.count` | integer | Total number of active tables on server |
| `tables.active` | integer | Number of tables with games currently in progress |

## Update Frequency

The status file is written approximately every 1 second (every 20 ticks at 50ms per tick).

## Website Integration Example

### JavaScript Fetch

```javascript
async function updatePlayerCount() {
  try {
    const response = await fetch('/api/status.json');
    const status = await response.json();
    
    document.getElementById('player-count').textContent = status.players.count;
    document.getElementById('players-list').textContent = status.players.list.join(', ');
    document.getElementById('server-status').textContent = 
      status.online ? 'Online' : 'Offline';
    document.getElementById('active-games').textContent = status.tables.active;
  } catch (error) {
    console.error('Failed to fetch status:', error);
  }
}

// Update every 5 seconds
setInterval(updatePlayerCount, 5000);
```

### HTML Display

```html
<div id="server-status-widget">
  <h3>PlayPalace Server Status</h3>
  <p>Status: <span id="server-status">Unknown</span></p>
  <p>Players Online: <span id="player-count">0</span></p>
  <p>Active Games: <span id="active-games">0</span></p>
  <div>
    <h4>Online Players:</h4>
    <p id="players-list">None</p>
  </div>
</div>
```

## File Permissions

Ensure the server process has write permission to the directory containing `status.json`. The file will be created if it doesn't exist, or overwritten if it does.

## Error Handling

If the status file cannot be written, the server will print an error message but continue running normally:

```
Failed to write status file: [error details]
```

## API Alternative

Authenticated clients can also request the online player list via the `get_online_players` packet type (see network protocol documentation).
