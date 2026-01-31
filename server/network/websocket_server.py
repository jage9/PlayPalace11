"""WebSocket server for client connections."""

import json
import ssl
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Coroutine
import websockets
from websockets.asyncio.server import serve, ServerConnection


@dataclass
class ClientConnection:
    """Represents a connected client."""

    websocket: ServerConnection
    address: str
    username: str | None = None
    authenticated: bool = False

    async def send(self, packet: dict) -> None:
        """Send a packet to this client."""
        try:
            await self.websocket.send(json.dumps(packet))
        except websockets.exceptions.ConnectionClosed:
            pass

    async def close(self) -> None:
        """Close this connection."""
        try:
            await self.websocket.close()
        except Exception:
            pass


class WebSocketServer:
    """
    Async WebSocket server for handling client connections.

    The server is async, but game logic is synchronous. Messages are
    queued and processed synchronously, then responses are sent async.
    """

    def __init__(
        self,
        host: str = "::",
        port: int = 8000,
        on_connect: Callable[[ClientConnection], Coroutine] | None = None,
        on_disconnect: Callable[[ClientConnection], Coroutine] | None = None,
        on_message: Callable[[ClientConnection, dict], Coroutine] | None = None,
        ssl_cert: str | Path | None = None,
        ssl_key: str | Path | None = None,
        max_message_size: int | None = None,
    ):
        self.host = host
        self.port = port
        self._on_connect = on_connect
        self._on_disconnect = on_disconnect
        self._on_message = on_message
        self._clients: dict[str, ClientConnection] = {}
        self._server = None
        self._running = False
        self._ssl_context = None
        self._max_message_size = max_message_size

        # Configure SSL if certificates provided
        if ssl_cert and ssl_key:
            self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            self._ssl_context.load_cert_chain(str(ssl_cert), str(ssl_key))

    @property
    def clients(self) -> dict[str, ClientConnection]:
        """Get all connected clients keyed by address."""
        return self._clients

    async def start(self) -> None:
        """Start the WebSocket server."""
        self._running = True
        # Manually enter the context manager to control lifecycle
        self._server = await serve(
            self._handle_client,
            self.host,
            self.port,
            ssl=self._ssl_context,
            max_size=self._max_message_size,
        ).__aenter__()
        
        protocol = "wss" if self._ssl_context else "ws"
        print(f"WebSocket server started on {protocol}://{self.host}:{self.port}")

    async def stop(self) -> None:
        """Stop the WebSocket server."""
        self._running = False
        if self._server:
            self._server.close()
            await self._server.wait_closed()

        # Close all client connections
        for client in list(self._clients.values()):
            await client.close()
        self._clients.clear()

    async def _handle_client(self, websocket: ServerConnection) -> None:
        """Handle a client connection."""
        address = f"{websocket.remote_address[0]}:{websocket.remote_address[1]}"
        client = ClientConnection(websocket=websocket, address=address)
        self._clients[address] = client

        try:
            if self._on_connect:
                await self._on_connect(client)

            async for message in websocket:
                try:
                    packet = json.loads(message)
                    if self._on_message:
                        await self._on_message(client, packet)
                except json.JSONDecodeError:
                    pass  # Ignore malformed messages

        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            if address in self._clients:
                del self._clients[address]
            if self._on_disconnect:
                await self._on_disconnect(client)

    async def broadcast(
        self, packet: dict, exclude: ClientConnection | None = None
    ) -> None:
        """Broadcast a packet to all authenticated clients."""
        for client in self._clients.values():
            if client.authenticated and client != exclude:
                await client.send(packet)

    async def send_to_user(self, username: str, packet: dict) -> bool:
        """Send a packet to a specific user."""
        for client in self._clients.values():
            if client.username == username:
                await client.send(packet)
                return True
        return False

    def get_client_by_username(self, username: str) -> ClientConnection | None:
        """Get a client by username."""
        for client in self._clients.values():
            if client.username == username:
                return client
        return None
