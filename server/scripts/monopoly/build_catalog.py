"""Build canonical Monopoly catalog artifacts from official instruction sources."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


# Allow direct script execution: python server/scripts/monopoly/build_catalog.py
if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from server.games.monopoly.catalog.instruction_parser import (  # noqa: E402
    extract_next_data_json,
    extract_raw_records,
)
from server.games.monopoly.catalog.manual_validator import validate_manual  # noqa: E402
from server.games.monopoly.catalog.normalize import build_canonical_catalog  # noqa: E402
from server.games.monopoly.catalog.sitemap_parser import (  # noqa: E402
    parse_monopoly_instruction_urls,
    parse_sitemap_index,
)


DEFAULT_ROOT_SITEMAP = "https://instructions.hasbro.com/sitemap.xml"


def _fetch_text(url: str, timeout: float = 30.0) -> str:
    request = Request(
        url,
        headers={"User-Agent": "PlayPalace-Monopoly-Catalog/1.0"},
    )
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8")


def _load_offline_records(fixture_dir: Path):
    records = []
    for payload_path in sorted(fixture_dir.glob("*_payload.json")):
        payload = json.loads(payload_path.read_text(encoding="utf-8"))
        page_props = payload.get("props", {}).get("pageProps", {})
        locale = page_props.get("locale", "en-us")
        slug = payload.get("query", {}).get("instruction", "")
        instruction_url = f"https://instructions.hasbro.com/{locale}/instruction/{slug}"
        records.extend(extract_raw_records(payload, instruction_url))
    return records


def _load_live_records(root_sitemap_url: str):
    records = []
    fetch_errors: list[dict] = []
    index_xml = _fetch_text(root_sitemap_url)
    locale_sitemaps = parse_sitemap_index(index_xml)
    print(f"Discovered {len(locale_sitemaps)} locale sitemaps")

    for locale_sitemap_url in locale_sitemaps:
        try:
            locale_xml = _fetch_text(locale_sitemap_url)
        except (HTTPError, URLError, OSError) as error:
            fetch_errors.append(
                {
                    "stage": "locale_sitemap",
                    "url": locale_sitemap_url,
                    "error": str(error),
                }
            )
            print(f"Skipping locale sitemap due to error: {locale_sitemap_url} ({error})")
            continue

        instruction_urls = parse_monopoly_instruction_urls(locale_xml)
        print(
            f"Processing locale sitemap {locale_sitemap_url} "
            f"with {len(instruction_urls)} monopoly URLs"
        )
        for instruction_url in instruction_urls:
            try:
                html = _fetch_text(instruction_url)
                payload = extract_next_data_json(html)
                records.extend(extract_raw_records(payload, instruction_url))
            except (HTTPError, URLError, OSError, ValueError, json.JSONDecodeError) as error:
                fetch_errors.append(
                    {
                        "stage": "instruction_page",
                        "url": instruction_url,
                        "error": str(error),
                    }
                )
                continue
    return records, fetch_errors


def _stable_dump(path: Path, data) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False),
        encoding="utf-8",
    )
    tmp_path.replace(path)


def run_pipeline(
    *,
    fixture_dir: Path | None = None,
    output_dir: Path,
    offline: bool = False,
    root_sitemap_url: str = DEFAULT_ROOT_SITEMAP,
    validate_manual_urls: bool = False,
) -> None:
    """Run catalog extraction and write canonical artifacts."""
    output_dir.mkdir(parents=True, exist_ok=True)

    if offline:
        if fixture_dir is None:
            raise ValueError("offline mode requires fixture_dir")
        records = _load_offline_records(fixture_dir)
    else:
        records, fetch_errors = _load_live_records(root_sitemap_url)
    if offline:
        fetch_errors = []

    catalog = build_canonical_catalog(records)

    manual_variants = [dict(row) for row in catalog.manual_variants]
    if validate_manual_urls:
        for row in manual_variants:
            validation = validate_manual(row["pdf_url"])
            row.update(validation)

    editions = [asdict(edition) for edition in catalog.editions]
    editions.sort(key=lambda row: (row["sku"], row["edition_id"]))
    manual_variants.sort(
        key=lambda row: (
            row["edition_id"],
            row.get("locale", ""),
            row.get("filename", ""),
            row.get("pdf_url", ""),
        )
    )

    stats = {
        "records_raw": len(records),
        "editions_count": len(editions),
        "manual_variants_count": len(manual_variants),
        "locales_count": len({record.locale for record in records}),
        "fetch_errors_count": len(fetch_errors),
        "offline": offline,
    }

    _stable_dump(output_dir / "monopoly_editions.json", editions)
    _stable_dump(output_dir / "monopoly_manual_variants.json", manual_variants)
    _stable_dump(output_dir / "catalog_stats.json", stats)
    _stable_dump(output_dir / "catalog_fetch_errors.json", fetch_errors)


def main() -> None:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description="Build Monopoly catalog artifacts.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("server/games/monopoly/catalog"),
        help="Directory for canonical output files.",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Use local fixture payloads instead of live crawling.",
    )
    parser.add_argument(
        "--fixture-dir",
        type=Path,
        default=Path("server/tests/fixtures/monopoly"),
        help="Fixture directory used when --offline is set.",
    )
    parser.add_argument(
        "--root-sitemap-url",
        default=DEFAULT_ROOT_SITEMAP,
        help="Root sitemap URL for live crawling.",
    )
    parser.add_argument(
        "--validate-manual-urls",
        action="store_true",
        help="Download and checksum manuals.",
    )
    args = parser.parse_args()

    run_pipeline(
        fixture_dir=args.fixture_dir,
        output_dir=args.output_dir,
        offline=args.offline,
        root_sitemap_url=args.root_sitemap_url,
        validate_manual_urls=args.validate_manual_urls,
    )


if __name__ == "__main__":
    main()
