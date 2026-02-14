"""
Tests for locale file completeness.

Ensures all locale directories have the same set of .ftl files as the
reference locale (English), and that no files are empty or corrupted.
"""

from pathlib import Path

import pytest


def get_locales_dir() -> Path:
    """Get the locales directory path."""
    return Path(__file__).parent.parent / "locales"


def get_all_locales(locales_dir: Path) -> list[str]:
    """Get list of all locale directory names."""
    return sorted([d.name for d in locales_dir.iterdir() if d.is_dir()])


def get_locale_files(locales_dir: Path, locale: str) -> set[str]:
    """Get set of .ftl filenames in a locale directory."""
    locale_path = locales_dir / locale
    if not locale_path.exists():
        return set()
    return {f.name for f in locale_path.glob("*.ftl")}


def test_all_locales_have_same_files():
    """
    Test that all locale directories have the same set of .ftl files
    as the reference locale (English).
    """
    locales_dir = get_locales_dir()
    reference_locale = "en"

    # Get reference files
    reference_files = get_locale_files(locales_dir, reference_locale)
    assert reference_files, f"Reference locale '{reference_locale}' has no .ftl files"

    # Check all other locales
    all_locales = get_all_locales(locales_dir)
    missing_map: dict[str, set[str]] = {}

    for locale in all_locales:
        if locale == reference_locale:
            continue

        locale_files = get_locale_files(locales_dir, locale)
        missing_files = reference_files - locale_files
        extra_files = locale_files - reference_files

        if missing_files:
            missing_map[locale] = missing_files

        # Also check for extra files (shouldn't happen but good to know)
        if extra_files:
            pytest.fail(
                f"Locale '{locale}' has extra files not in reference: "
                f"{sorted(extra_files)}"
            )

    # If any locales are missing files, fail with detailed message
    if missing_map:
        total_missing = sum(len(files) for files in missing_map.values())
        error_lines = [
            f"Found {total_missing} missing file(s) in {len(missing_map)} locale(s):"
        ]
        for locale in sorted(missing_map.keys()):
            missing_files = missing_map[locale]
            error_lines.append(f"  {locale}: {', '.join(sorted(missing_files))}")
        error_lines.append("")
        error_lines.append("Fix with: cd server && python3 tools/check_locales.py --fix")

        pytest.fail("\n".join(error_lines))


def test_no_empty_locale_files():
    """
    Test that no locale files are empty or suspiciously small.

    Files smaller than 50 bytes are likely empty or incomplete.
    """
    locales_dir = get_locales_dir()
    all_locales = get_all_locales(locales_dir)

    empty_files: list[tuple[str, str, int]] = []
    min_size = 50  # bytes

    for locale in all_locales:
        locale_path = locales_dir / locale
        for ftl_file in locale_path.glob("*.ftl"):
            file_size = ftl_file.stat().st_size
            if file_size < min_size:
                empty_files.append((locale, ftl_file.name, file_size))

    if empty_files:
        error_lines = [
            f"Found {len(empty_files)} empty or very small file(s) (< {min_size} bytes):"
        ]
        for locale, fname, size in empty_files:
            error_lines.append(f"  {locale}/{fname}: {size} bytes")

        pytest.fail("\n".join(error_lines))


def test_reference_locale_exists():
    """Test that the reference locale (English) exists and has files."""
    locales_dir = get_locales_dir()
    reference_locale = "en"

    reference_path = locales_dir / reference_locale
    assert reference_path.exists(), f"Reference locale '{reference_locale}' not found"
    assert reference_path.is_dir(), (
        f"Reference locale '{reference_locale}' is not a directory"
    )

    reference_files = get_locale_files(locales_dir, reference_locale)
    assert len(reference_files) > 0, (
        f"Reference locale '{reference_locale}' has no .ftl files"
    )

    # Ensure key system files exist
    required_files = {"main.ftl", "games.ftl", "languages.ftl"}
    assert required_files.issubset(reference_files), (
        f"Reference locale missing required files: "
        f"{required_files - reference_files}"
    )


def test_all_expected_languages_present():
    """
    Test that all expected language directories are present.

    This helps catch accidental deletions or typos in language codes.
    """
    locales_dir = get_locales_dir()
    all_locales = set(get_all_locales(locales_dir))

    # Expected languages based on current deployment
    expected_languages = {
        "ar", "cs", "de", "en", "es", "fa", "fr", "hi", "hr", "hu",
        "id", "it", "ja", "ko", "mn", "nl", "pl", "pt", "ro", "ru",
        "sk", "sl", "sv", "th", "tr", "uk", "vi", "zh", "zu",
    }

    missing_languages = expected_languages - all_locales
    extra_languages = all_locales - expected_languages

    errors = []
    if missing_languages:
        errors.append(f"Missing expected languages: {sorted(missing_languages)}")
    if extra_languages:
        errors.append(f"Found unexpected languages: {sorted(extra_languages)}")

    if errors:
        pytest.fail("\n".join(errors))
