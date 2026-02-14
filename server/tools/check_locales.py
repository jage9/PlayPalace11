#!/usr/bin/env python3
"""
Locale Completeness Checker

Verifies that all locale directories have the same set of .ftl files as the
reference locale (English). Can detect missing files and optionally auto-fix
by copying English templates.

Usage:
    python check_locales.py                 # Check only
    python check_locales.py --fix           # Copy missing files from English
    python check_locales.py --verbose       # Detailed output
    python check_locales.py --fix --verbose # Both

Exit codes:
    0 - All locales are complete
    1 - Missing files detected (or other errors)
"""

import argparse
import shutil
import sys
from pathlib import Path


def get_locales_dir() -> Path:
    """Get the locales directory path."""
    script_dir = Path(__file__).parent
    locales_dir = script_dir.parent / "locales"
    return locales_dir


def get_all_locales(locales_dir: Path) -> list[str]:
    """Get list of all locale directory names."""
    return sorted([d.name for d in locales_dir.iterdir() if d.is_dir()])


def get_locale_files(locales_dir: Path, locale: str) -> set[str]:
    """Get set of .ftl filenames in a locale directory."""
    locale_path = locales_dir / locale
    if not locale_path.exists():
        return set()
    return {f.name for f in locale_path.glob("*.ftl")}


def check_completeness(
    locales_dir: Path, reference_locale: str = "en", verbose: bool = False
) -> dict[str, set[str]]:
    """
    Check all locales against the reference locale.

    Returns a dict mapping locale names to sets of missing filenames.
    Empty sets indicate complete locales.
    """
    reference_files = get_locale_files(locales_dir, reference_locale)
    if not reference_files:
        print(f"ERROR: Reference locale '{reference_locale}' has no .ftl files!")
        sys.exit(1)

    if verbose:
        print(f"Reference locale '{reference_locale}' has {len(reference_files)} files:")
        for fname in sorted(reference_files):
            print(f"  - {fname}")
        print()

    all_locales = get_all_locales(locales_dir)
    missing_map: dict[str, set[str]] = {}

    for locale in all_locales:
        if locale == reference_locale:
            continue

        locale_files = get_locale_files(locales_dir, locale)
        missing_files = reference_files - locale_files

        if missing_files:
            missing_map[locale] = missing_files
            if verbose:
                print(f"❌ {locale}: missing {len(missing_files)} file(s)")
                for fname in sorted(missing_files):
                    print(f"   - {fname}")
        elif verbose:
            print(f"✅ {locale}: complete ({len(locale_files)} files)")

    return missing_map


def fix_missing_files(
    locales_dir: Path, missing_map: dict[str, set[str]], reference_locale: str = "en"
) -> int:
    """
    Copy missing files from reference locale to incomplete locales.

    Returns the number of files copied.
    """
    copied_count = 0
    reference_path = locales_dir / reference_locale

    for locale, missing_files in missing_map.items():
        locale_path = locales_dir / locale
        locale_path.mkdir(parents=True, exist_ok=True)

        for fname in missing_files:
            src = reference_path / fname
            dst = locale_path / fname

            if not src.exists():
                print(f"WARNING: Source file {src} does not exist, skipping")
                continue

            shutil.copy2(src, dst)
            print(f"Copied {fname} to {locale}/")
            copied_count += 1

    return copied_count


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Check and optionally fix locale file completeness"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Copy missing files from English to incomplete locales",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed output"
    )
    parser.add_argument(
        "--reference",
        default="en",
        help="Reference locale to compare against (default: en)",
    )

    args = parser.parse_args()

    locales_dir = get_locales_dir()

    if not locales_dir.exists():
        print(f"ERROR: Locales directory not found: {locales_dir}")
        return 1

    if args.verbose:
        print(f"Checking locales in: {locales_dir}")
        print()

    missing_map = check_completeness(locales_dir, args.reference, args.verbose)

    if not missing_map:
        if not args.verbose:
            print("✅ All locales are complete!")
        return 0

    # Report missing files
    total_missing = sum(len(files) for files in missing_map.values())
    print()
    print(f"❌ Found {total_missing} missing file(s) in {len(missing_map)} locale(s):")
    for locale in sorted(missing_map.keys()):
        missing_files = missing_map[locale]
        print(f"  {locale}: {', '.join(sorted(missing_files))}")

    if args.fix:
        print()
        print("Fixing missing files...")
        copied = fix_missing_files(locales_dir, missing_map, args.reference)
        print(f"✅ Copied {copied} file(s)")
        return 0
    else:
        print()
        print("Run with --fix to copy missing files from English.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
