# SPDX-License-Identifier: AGPL-3.0-only
"""Check that CHANGELOG.md and pyproject.toml agree on the released version.

Usage: python scripts/check_version_consistency.py [REPOSITORY_ROOT]
"""

import re
import sys
import tomllib
from datetime import date
from pathlib import Path

UNRELEASED = "Unreleased"
HEADING = re.compile(r"## \[(?P<name>[^\]]+)\](?: - (?P<date>.+?))?\s*")
SEMVER = re.compile(
    r"(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?"
)
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def parse_headings(text: str) -> list[tuple[str, str | None]]:
    """Return (name, date) for every second-level version heading."""
    headings: list[tuple[str, str | None]] = []
    for line in text.splitlines():
        match = HEADING.fullmatch(line)
        if match:
            headings.append((match["name"], match["date"]))
    return headings


def _is_iso_date(value: str) -> bool:
    if not DATE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _check_released(released: list[tuple[str, str | None]]) -> list[str]:
    errors: list[str] = []
    cores: list[tuple[int, int, int]] = []
    for name, day in released:
        match = SEMVER.fullmatch(name)
        if match:
            cores.append((int(match["major"]), int(match["minor"]), int(match["patch"])))
        else:
            errors.append(f"Heading '{name}' is not a valid semantic version.")
        if day is None or not _is_iso_date(day):
            errors.append(
                f"Heading '{name}' needs a release date in YYYY-MM-DD format, "
                f"found '{day}'."
            )
    if len(cores) == len(released) and any(
        newer <= older for newer, older in zip(cores, cores[1:], strict=False)
    ):
        errors.append("Released versions must be listed in descending order.")
    return errors


def check(changelog: str, project_version: str) -> list[str]:
    """Return a list of problems; an empty list means the sources agree."""
    headings = parse_headings(changelog)
    errors: list[str] = []
    if not headings or headings[0] != (UNRELEASED, None):
        errors.append("The first heading must be '## [Unreleased]' without a date.")
    if any(name == UNRELEASED for name, _ in headings[1:]):
        errors.append("The heading '[Unreleased]' must appear only once.")
    released = [heading for heading in headings if heading[0] != UNRELEASED]
    if not released:
        errors.append("No released version found in the changelog.")
        return errors
    errors.extend(_check_released(released))
    if released[0][0] != project_version:
        errors.append(
            f"Newest released version in the changelog is '{released[0][0]}', "
            f"but pyproject.toml defines '{project_version}'."
        )
    return errors


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    root = Path(args[0]) if args else Path.cwd()
    try:
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        with (root / "pyproject.toml").open("rb") as handle:
            project_version = str(tomllib.load(handle)["project"]["version"])
    except (OSError, tomllib.TOMLDecodeError, KeyError) as exc:
        print(f"Cannot read version sources: {exc!r}", file=sys.stderr)
        return 1
    errors = check(changelog, project_version)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"Version consistency check passed: {project_version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
