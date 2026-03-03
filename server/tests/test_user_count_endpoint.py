"""Tests for the /api/user_count HTTP endpoint and its rate limiting."""

import http
import json
import time
from types import SimpleNamespace
from pathlib import Path

import pytest

from server.core.server import (
    Server,
    DEFAULT_USER_COUNT_REQUESTS_PER_MINUTE,
    USER_COUNT_RATE_WINDOW_SECONDS,
)
from server.messages.localization import Localization


def _make_server(tmp_path) -> Server:
    Localization.init(Path(__file__).resolve().parents[1] / "locales")
    srv = Server.__new__(Server)
    srv._users = {}
    srv._user_count_ip_limit = DEFAULT_USER_COUNT_REQUESTS_PER_MINUTE
    srv._user_count_ip_window = USER_COUNT_RATE_WINDOW_SECONDS
    srv._user_count_attempts_ip = {}
    return srv


class DummyConnection:
    """Minimal stand-in for websockets.asyncio.server.ServerConnection."""

    def __init__(self, remote_ip: str = "1.2.3.4"):
        self._remote_ip = remote_ip

    @property
    def remote_address(self):
        return (self._remote_ip, 9999)

    def respond(self, status, body: str):
        return SimpleNamespace(status_code=int(status), body=body.encode())


def _make_request(path: str = "/api/user_count"):
    return SimpleNamespace(path=path)


@pytest.mark.asyncio
async def test_user_count_returns_zero_when_no_users(tmp_path):
    srv = _make_server(tmp_path)
    conn = DummyConnection()
    req = _make_request()
    response = await srv._handle_user_count_request(conn, req)
    assert response.status_code == http.HTTPStatus.OK
    data = json.loads(response.body)
    assert data == {"user_count": 0}


@pytest.mark.asyncio
async def test_user_count_returns_correct_count(tmp_path):
    srv = _make_server(tmp_path)
    srv._users = {"alice": object(), "bob": object(), "carol": object()}
    conn = DummyConnection()
    req = _make_request()
    response = await srv._handle_user_count_request(conn, req)
    assert response.status_code == http.HTTPStatus.OK
    data = json.loads(response.body)
    assert data == {"user_count": 3}


@pytest.mark.asyncio
async def test_unknown_path_returns_404(tmp_path):
    srv = _make_server(tmp_path)
    conn = DummyConnection()
    req = _make_request("/unknown")
    response = await srv._handle_user_count_request(conn, req)
    assert response.status_code == http.HTTPStatus.NOT_FOUND


@pytest.mark.asyncio
async def test_rate_limit_blocks_after_limit(tmp_path):
    srv = _make_server(tmp_path)
    srv._user_count_ip_limit = 3
    conn = DummyConnection("5.5.5.5")
    req = _make_request()

    # First three requests should succeed.
    for _ in range(3):
        response = await srv._handle_user_count_request(conn, req)
        assert response.status_code == http.HTTPStatus.OK

    # Fourth request should be rate-limited.
    response = await srv._handle_user_count_request(conn, req)
    assert response.status_code == http.HTTPStatus.TOO_MANY_REQUESTS


@pytest.mark.asyncio
async def test_rate_limit_is_per_ip(tmp_path):
    srv = _make_server(tmp_path)
    srv._user_count_ip_limit = 1

    conn_a = DummyConnection("10.0.0.1")
    conn_b = DummyConnection("10.0.0.2")
    req = _make_request()

    # Each IP gets its own bucket.
    response_a = await srv._handle_user_count_request(conn_a, req)
    assert response_a.status_code == http.HTTPStatus.OK

    response_b = await srv._handle_user_count_request(conn_b, req)
    assert response_b.status_code == http.HTTPStatus.OK

    # Both are now exhausted.
    response_a2 = await srv._handle_user_count_request(conn_a, req)
    assert response_a2.status_code == http.HTTPStatus.TOO_MANY_REQUESTS


def test_check_user_count_rate_limit_allows_within_limit(tmp_path):
    srv = _make_server(tmp_path)
    srv._user_count_ip_limit = 5

    for _ in range(5):
        assert srv._check_user_count_rate_limit("1.1.1.1") is True

    assert srv._check_user_count_rate_limit("1.1.1.1") is False


def test_check_user_count_rate_limit_disabled_when_zero(tmp_path):
    srv = _make_server(tmp_path)
    srv._user_count_ip_limit = 0

    # When limit is 0 (disabled), all requests are allowed.
    for _ in range(100):
        assert srv._check_user_count_rate_limit("2.2.2.2") is True
