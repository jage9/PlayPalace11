"""Tests for config sharing data helpers and dialog flows."""

import json
import time
from pathlib import Path

import pytest

from config_schemas import OptionsProfile, ExportedIdentities
from config_manager import ConfigManager
from ui.config_sharing import (
    build_export_server,
    match_servers,
    find_changed_accounts,
    has_meaningful_changes,
    server_info_differs,
    build_server_info_display,
    append_imported_notes,
    has_options_profile_data,
    try_load_export_file,
    format_export_timestamp,
)


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))


def make_manager(tmp_path):
    return ConfigManager(base_path=tmp_path / "pp")


def make_server_dict(**overrides):
    """Build a minimal server dict with defaults."""
    base = {
        "server_id": "srv-1",
        "name": "Test Server",
        "host": "localhost",
        "port": 8000,
        "notes": "",
        "accounts": {},
        "last_account_id": None,
        "options_profile": OptionsProfile().model_dump(),
        "trusted_certificate": None,
    }
    base.update(overrides)
    return base


def make_account_dict(**overrides):
    """Build a minimal account dict with defaults."""
    base = {
        "account_id": "acct-1",
        "username": "alice",
        "password": "pass123",
        "email": "alice@example.com",
        "notes": "",
    }
    base.update(overrides)
    return base


# ========== build_export_server ==========


class TestBuildExportServer:
    def test_clears_sensitive_fields(self):
        server = make_server_dict(
            trusted_certificate={"fingerprint": "aa:bb"},
            last_account_id="acct-1",
        )
        result = build_export_server(server, include_accounts=True, include_options=True)
        assert result["trusted_certificate"] is None
        assert result["last_account_id"] is None

    def test_preserves_accounts_when_included(self):
        accounts = {"a1": make_account_dict()}
        server = make_server_dict(accounts=accounts)
        result = build_export_server(server, include_accounts=True, include_options=False)
        assert len(result["accounts"]) == 1
        assert "a1" in result["accounts"]

    def test_clears_accounts_when_excluded(self):
        accounts = {"a1": make_account_dict()}
        server = make_server_dict(accounts=accounts)
        result = build_export_server(server, include_accounts=False, include_options=False)
        assert result["accounts"] == {}

    def test_preserves_options_when_included(self):
        custom_opts = OptionsProfile().model_dump()
        custom_opts["audio"]["music_volume"] = 99
        server = make_server_dict(options_profile=custom_opts)
        result = build_export_server(server, include_accounts=False, include_options=True)
        assert result["options_profile"]["audio"]["music_volume"] == 99

    def test_resets_options_when_excluded(self):
        custom_opts = OptionsProfile().model_dump()
        custom_opts["audio"]["music_volume"] = 99
        server = make_server_dict(options_profile=custom_opts)
        result = build_export_server(server, include_accounts=False, include_options=False)
        assert result["options_profile"] == OptionsProfile().model_dump()

    def test_preserves_server_id(self):
        server = make_server_dict(server_id="my-id-123")
        result = build_export_server(server, include_accounts=False, include_options=False)
        assert result["server_id"] == "my-id-123"

    def test_deep_copies_data(self):
        accounts = {"a1": make_account_dict()}
        server = make_server_dict(accounts=accounts)
        result = build_export_server(server, include_accounts=True, include_options=True)
        result["accounts"]["a1"]["username"] = "modified"
        assert server["accounts"]["a1"]["username"] == "alice"


# ========== match_servers ==========


class TestMatchServers:
    def test_matches_by_host_case_insensitive(self):
        imported = [
            {"host": "EXAMPLE.COM", "name": "S1"},
            {"host": "new.host", "name": "S2"},
        ]
        existing = {
            "srv-1": {"host": "example.com", "name": "Example"},
        }
        result = match_servers(imported, existing)
        assert result[0] == "srv-1"
        assert result[1] is None

    def test_all_new_servers(self):
        imported = [{"host": "a.com"}, {"host": "b.com"}]
        existing = {"s1": {"host": "c.com"}}
        result = match_servers(imported, existing)
        assert result[0] is None
        assert result[1] is None

    def test_empty_imported(self):
        result = match_servers([], {"s1": {"host": "a.com"}})
        assert result == {}

    def test_empty_existing(self):
        result = match_servers([{"host": "a.com"}], {})
        assert result[0] is None


# ========== find_changed_accounts ==========


class TestFindChangedAccounts:
    def test_finds_new_accounts(self):
        imported = {"i1": make_account_dict(username="bob", account_id="i1")}
        existing = {"e1": make_account_dict(username="alice", account_id="e1")}
        new_accts, changed = find_changed_accounts(imported, existing)
        assert len(new_accts) == 1
        assert new_accts[0]["username"] == "bob"
        assert len(changed) == 0

    def test_finds_changed_password(self):
        imported = {"i1": make_account_dict(username="alice", password="newpass", account_id="i1")}
        existing = {"e1": make_account_dict(username="alice", password="oldpass", account_id="e1")}
        new_accts, changed = find_changed_accounts(imported, existing)
        assert len(new_accts) == 0
        assert len(changed) == 1
        assert "password" in changed[0]["changed_fields"]

    def test_finds_changed_email(self):
        imported = {"i1": make_account_dict(username="alice", email="new@x.com", account_id="i1")}
        existing = {"e1": make_account_dict(username="alice", email="old@x.com", account_id="e1")}
        _, changed = find_changed_accounts(imported, existing)
        assert len(changed) == 1
        assert "email" in changed[0]["changed_fields"]

    def test_ignores_notes_differences(self):
        imported = {"i1": make_account_dict(username="alice", notes="new notes", account_id="i1")}
        existing = {"e1": make_account_dict(username="alice", notes="old notes", account_id="e1")}
        new_accts, changed = find_changed_accounts(imported, existing)
        assert len(new_accts) == 0
        assert len(changed) == 0

    def test_case_insensitive_username_match(self):
        imported = {"i1": make_account_dict(username="ALICE", password="new", account_id="i1")}
        existing = {"e1": make_account_dict(username="alice", password="old", account_id="e1")}
        _, changed = find_changed_accounts(imported, existing)
        assert len(changed) == 1

    def test_identical_accounts_not_reported(self):
        acct = make_account_dict()
        imported = {"i1": acct.copy()}
        imported["i1"]["account_id"] = "i1"
        existing = {"e1": acct.copy()}
        existing["e1"]["account_id"] = "e1"
        new_accts, changed = find_changed_accounts(imported, existing)
        assert len(new_accts) == 0
        assert len(changed) == 0

    def test_includes_existing_id_in_changed(self):
        imported = {"i1": make_account_dict(username="alice", password="new", account_id="i1")}
        existing = {"e1": make_account_dict(username="alice", password="old", account_id="e1")}
        _, changed = find_changed_accounts(imported, existing)
        assert changed[0]["existing_id"] == "e1"


# ========== has_meaningful_changes ==========


class TestHasMeaningfulChanges:
    def test_name_differs(self):
        imp = make_server_dict(name="New Name")
        ext = make_server_dict(name="Old Name")
        assert has_meaningful_changes(imp, ext) is True

    def test_port_differs(self):
        imp = make_server_dict(port=9000)
        ext = make_server_dict(port=8000)
        assert has_meaningful_changes(imp, ext) is True

    def test_has_options(self):
        custom = OptionsProfile().model_dump()
        custom["audio"]["music_volume"] = 50
        imp = make_server_dict(options_profile=custom)
        ext = make_server_dict()
        assert has_meaningful_changes(imp, ext) is True

    def test_new_accounts(self):
        imp = make_server_dict(accounts={"a1": make_account_dict(username="bob")})
        ext = make_server_dict()
        assert has_meaningful_changes(imp, ext) is True

    def test_no_changes(self):
        server = make_server_dict()
        assert has_meaningful_changes(server, server) is False

    def test_only_notes_differ(self):
        imp = make_server_dict(notes="new notes")
        ext = make_server_dict(notes="old notes")
        # Notes alone shouldn't count (server_info_differs only checks name/port)
        assert has_meaningful_changes(imp, ext) is False


# ========== server_info_differs ==========


class TestServerInfoDiffers:
    def test_same_info(self):
        s = make_server_dict()
        assert server_info_differs(s, s) is False

    def test_name_differs(self):
        assert server_info_differs({"name": "A", "port": 8000}, {"name": "B", "port": 8000}) is True

    def test_port_differs(self):
        assert server_info_differs({"name": "A", "port": 9000}, {"name": "A", "port": 8000}) is True

    def test_notes_ignored(self):
        a = make_server_dict(notes="foo")
        b = make_server_dict(notes="bar")
        assert server_info_differs(a, b) is False


# ========== build_server_info_display ==========


class TestBuildServerInfoDisplay:
    def test_both_differ(self):
        imp = {"name": "New", "port": 9000}
        ext = {"name": "Old", "port": 8000}
        text = build_server_info_display(imp, ext)
        assert "Name: Old -> New" in text
        assert "Port: 8000 -> 9000" in text

    def test_only_name_differs(self):
        imp = {"name": "New", "port": 8000}
        ext = {"name": "Old", "port": 8000}
        text = build_server_info_display(imp, ext)
        assert "Name:" in text
        assert "Port:" not in text

    def test_nothing_differs(self):
        s = {"name": "Same", "port": 8000}
        assert build_server_info_display(s, s) == ""


# ========== append_imported_notes ==========


class TestAppendImportedNotes:
    def test_appends_with_header(self):
        result = append_imported_notes("existing", "imported", "My Export", 1700000000)
        assert "existing" in result
        assert "Imported Notes From Export (My Export," in result
        assert "imported" in result

    def test_skips_empty_imported(self):
        result = append_imported_notes("existing", "", "desc", 0)
        assert result == "existing"

    def test_no_existing_notes(self):
        result = append_imported_notes("", "imported", "desc", 1700000000)
        assert result.startswith("Imported Notes From Export")
        assert "imported" in result
        assert not result.startswith("\n")

    def test_separator_between_existing_and_imported(self):
        result = append_imported_notes("old", "new", "desc", 1700000000)
        assert "\n\n" in result

    def test_stacking_multiple_imports(self):
        first = append_imported_notes("original", "first import", "Export 1", 1700000000)
        second = append_imported_notes(first, "second import", "Export 2", 1700001000)
        assert "Export 1" in second
        assert "Export 2" in second
        assert "first import" in second
        assert "second import" in second


# ========== has_options_profile_data ==========


class TestHasOptionsProfileData:
    def test_default_options_returns_false(self):
        server = make_server_dict()
        assert has_options_profile_data(server) is False

    def test_custom_options_returns_true(self):
        custom = OptionsProfile().model_dump()
        custom["audio"]["music_volume"] = 50
        server = make_server_dict(options_profile=custom)
        assert has_options_profile_data(server) is True

    def test_missing_options_returns_false(self):
        server = {"name": "Test"}
        assert has_options_profile_data(server) is False


# ========== try_load_export_file ==========


class TestTryLoadExportFile:
    def test_valid_file(self, tmp_path):
        data = {
            "description": "test export",
            "timestamp": int(time.time()),
            "servers": [make_server_dict()],
        }
        path = tmp_path / "export.json"
        path.write_text(json.dumps(data))
        result = try_load_export_file(str(path))
        assert result is not None
        assert result["description"] == "test export"

    def test_invalid_json(self, tmp_path):
        path = tmp_path / "bad.json"
        path.write_text("{not-json")
        assert try_load_export_file(str(path)) is None

    def test_missing_description(self, tmp_path):
        data = {"timestamp": 123, "servers": [make_server_dict()]}
        path = tmp_path / "no_desc.json"
        path.write_text(json.dumps(data))
        assert try_load_export_file(str(path)) is None

    def test_empty_description(self, tmp_path):
        data = {"description": "", "timestamp": 123, "servers": [make_server_dict()]}
        path = tmp_path / "empty_desc.json"
        path.write_text(json.dumps(data))
        assert try_load_export_file(str(path)) is None

    def test_empty_servers(self, tmp_path):
        data = {"description": "test", "timestamp": 123, "servers": []}
        path = tmp_path / "no_servers.json"
        path.write_text(json.dumps(data))
        assert try_load_export_file(str(path)) is None

    def test_nonexistent_file(self):
        assert try_load_export_file("/nonexistent/path.json") is None


# ========== format_export_timestamp ==========


class TestFormatExportTimestamp:
    def test_formats_valid_timestamp(self):
        # 2023-11-14 roughly
        result = format_export_timestamp(1700000000)
        assert "2023" in result
        assert "November" in result

    def test_handles_invalid_timestamp(self):
        result = format_export_timestamp(-99999999999999)
        assert result == "Unknown date"


# ========== Integration Tests ==========


class TestExportIntegration:
    def test_full_export_round_trip(self, tmp_path):
        """Export servers, then verify the file is valid and loadable."""
        cm = make_manager(tmp_path)
        sid1 = cm.add_server("Server 1", "host1.com", 8000, "notes1")
        cm.add_account(sid1, "alice", "pass1", "a@x.com")
        cm.add_account(sid1, "bob", "pass2")
        sid2 = cm.add_server("Server 2", "host2.com", 9000)

        servers = cm.get_all_servers()

        # Build export for both servers
        export_servers = []
        for server_id, server in servers.items():
            export_servers.append(
                build_export_server(server, include_accounts=True, include_options=True)
            )

        export_data = {
            "description": "Test export",
            "timestamp": int(time.time()),
            "servers": export_servers,
        }

        # Validate
        model = ExportedIdentities.model_validate(export_data)
        assert len(model.servers) == 2

        # Write and reload
        path = tmp_path / "export.json"
        path.write_text(json.dumps(export_data, indent=2))
        loaded = try_load_export_file(str(path))
        assert loaded is not None
        assert loaded["description"] == "Test export"
        assert len(loaded["servers"]) == 2

        # Verify sensitive fields cleared
        for s in loaded["servers"]:
            assert s["trusted_certificate"] is None
            assert s["last_account_id"] is None


class TestImportIntegration:
    def test_import_new_servers(self, tmp_path):
        """Import servers that don't exist yet."""
        cm = make_manager(tmp_path)
        assert len(cm.get_all_servers()) == 0

        # Simulate import data
        imp_server = make_server_dict(
            server_id="imp-1",
            name="Imported Server",
            host="imported.com",
            port=9000,
            accounts={
                "a1": make_account_dict(username="user1", account_id="a1"),
                "a2": make_account_dict(username="user2", account_id="a2"),
            },
        )

        # Match servers (should all be new)
        matches = match_servers([imp_server], cm.get_all_servers())
        assert matches[0] is None

        # Add the new server
        new_id = cm.add_server(
            name=imp_server["name"],
            host=imp_server["host"],
            port=imp_server["port"],
            notes=imp_server.get("notes", ""),
        )
        for acct_id, acct in imp_server["accounts"].items():
            cm.add_account(
                new_id,
                username=acct["username"],
                password=acct["password"],
                email=acct.get("email", ""),
                notes=acct.get("notes", ""),
            )

        servers = cm.get_all_servers()
        assert len(servers) == 1
        new_server = cm.get_server_by_id(new_id)
        assert new_server["name"] == "Imported Server"
        assert len(new_server["accounts"]) == 2

    def test_import_detects_existing_server(self, tmp_path):
        """Import matches existing server by host."""
        cm = make_manager(tmp_path)
        existing_id = cm.add_server("My Server", "example.com", 8000)
        cm.add_account(existing_id, "alice", "oldpass")

        imp_server = make_server_dict(
            host="example.com",
            name="Renamed Server",
            port=9000,
            accounts={
                "i1": make_account_dict(username="alice", password="newpass", account_id="i1"),
                "i2": make_account_dict(username="bob", password="bobpass", account_id="i2"),
            },
        )

        matches = match_servers([imp_server], cm.get_all_servers())
        assert matches[0] == existing_id

        existing_server = cm.get_server_by_id(existing_id)
        assert has_meaningful_changes(imp_server, existing_server) is True
        assert server_info_differs(imp_server, existing_server) is True

        new_accts, changed_accts = find_changed_accounts(
            imp_server["accounts"],
            cm.get_server_accounts(existing_id),
        )
        assert len(new_accts) == 1  # bob
        assert len(changed_accts) == 1  # alice's password changed

    def test_import_filters_unchanged_existing(self, tmp_path):
        """Existing server with no meaningful changes is filtered out."""
        cm = make_manager(tmp_path)
        cm.add_server("Server", "example.com", 8000)

        # Same server, nothing different
        imp_server = make_server_dict(host="example.com", name="Server", port=8000)

        existing_server = list(cm.get_all_servers().values())[0]
        assert has_meaningful_changes(imp_server, existing_server) is False

    def test_rollback_on_error(self, tmp_path):
        """Verify that identities can be restored after a failed import."""
        cm = make_manager(tmp_path)
        sid = cm.add_server("Original", "original.com", 8000)

        # Snapshot
        import copy
        snapshot = copy.deepcopy(cm.identities)

        # Make changes
        cm.add_server("Bad Import", "bad.com", 9000)
        assert len(cm.get_all_servers()) == 2

        # Rollback
        cm.identities = snapshot
        cm.save_identities()
        assert len(cm.get_all_servers()) == 1
        assert cm.get_server_by_id(sid)["name"] == "Original"
