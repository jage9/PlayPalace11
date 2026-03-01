"""Integration tests for Monopoly catalog build pipeline."""

from pathlib import Path

from server.scripts.monopoly.build_catalog import run_pipeline


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "monopoly"


def test_run_pipeline_offline_fixtures_writes_canonical_outputs(tmp_path: Path):
    """Offline fixture run emits canonical artifact files."""
    output_dir = tmp_path / "catalog"

    run_pipeline(fixture_dir=FIXTURE_DIR, output_dir=output_dir, offline=True)

    assert (output_dir / "monopoly_editions.json").exists()
    assert (output_dir / "monopoly_manual_variants.json").exists()
    assert (output_dir / "catalog_stats.json").exists()


def test_pipeline_outputs_are_stably_sorted_and_repeatable(tmp_path: Path):
    """Running offline twice with same fixtures should produce identical output."""
    output_a = tmp_path / "run_a"
    output_b = tmp_path / "run_b"

    run_pipeline(fixture_dir=FIXTURE_DIR, output_dir=output_a, offline=True)
    run_pipeline(fixture_dir=FIXTURE_DIR, output_dir=output_b, offline=True)

    editions_a = (output_a / "monopoly_editions.json").read_text(encoding="utf-8")
    editions_b = (output_b / "monopoly_editions.json").read_text(encoding="utf-8")
    manuals_a = (output_a / "monopoly_manual_variants.json").read_text(encoding="utf-8")
    manuals_b = (output_b / "monopoly_manual_variants.json").read_text(encoding="utf-8")
    stats_a = (output_a / "catalog_stats.json").read_text(encoding="utf-8")
    stats_b = (output_b / "catalog_stats.json").read_text(encoding="utf-8")

    assert editions_a == editions_b
    assert manuals_a == manuals_b
    assert stats_a == stats_b


def test_runbook_lists_pipeline_commands():
    """Runbook must include executable pipeline command examples."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    text = (repo_root / "docs" / "design" / "plans" / "monopoly_catalog_pipeline.md").read_text(encoding="utf-8")
    assert "uv run python scripts/monopoly/build_catalog.py" in text
