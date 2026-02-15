# PlayPalace Web Client

This is an early version of a web client for the PlayPalace. is designed to connect to a server you indicate and can be hosted on the web.

## Public Setup

1. Copy the `/clients/web` directory to a public website location.
2. Copy the sounds folder from `/clients/desktop` to the same place, and put it in `./sounds`.
3. Copy the config sample to config.js and update any of the items if desired, such as server, port, or sounds folder.
4. GO to your new URL. You should see a login screen.

## Local Setup

1. Start the web server:
   - `python3 -m http.server 8080`
3. Open:
   - `http://127.0.0.1:8080/clients/web/`
## How it Works

When viewing the web client from a computer, you can tab between game, history, and chat similar to the desktop client. Most desktop hotkeys work here as well.
From mobile, the menu items become buttons, and you can expand and collapse the history.
Other desktop features like the buffers also work here.
