# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the changelog and version consistency check."""

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load_script() -> ModuleType:
    path = ROOT / "scripts" / "check_version_consistency.py"
    spec = importlib.util.spec_from_file_location("check_version_consistency", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


script = _load_script()

VALID = """# Changelog

## [Unreleased]

## [0.2.1] - 2026-11-27

## [0.2.0] - 2026-11-25
"""


def test_valid_changelog_has_no_errors() -> None:
    assert script.check(VALID, "0.2.1") == []


def test_version_mismatch_is_reported() -> None:
    errors = script.check(VALID, "0.2.2")
    assert any("0.2.2" in error for error in errors)


def test_unpublished_version_below_release_is_reported() -> None:
    errors = script.check(VALID + "\n## [0.1.0] - Unreleased\n", "0.2.1")
    assert any("0.1.0" in error and "YYYY-MM-DD" in error for error in errors)


def test_ascending_order_is_reported() -> None:
    text = "## [Unreleased]\n\n## [0.2.0] - 2026-11-25\n\n## [0.2.1] - 2026-11-27\n"
    errors = script.check(text, "0.2.0")
    assert any("descending" in error for error in errors)


def test_missing_unreleased_heading_is_reported() -> None:
    errors = script.check("## [0.2.1] - 2026-11-27\n", "0.2.1")
    assert any("Unreleased" in error for error in errors)


def test_invalid_date_is_reported() -> None:
    text = "## [Unreleased]\n\n## [0.2.1] - 2026-13-40\n"
    errors = script.check(text, "0.2.1")
    assert any("YYYY-MM-DD" in error for error in errors)


def test_invalid_version_is_reported() -> None:
    text = "## [Unreleased]\n\n## [v1] - 2026-11-27\n"
    errors = script.check(text, "v1")
    assert any("semantic version" in error for error in errors)


def test_missing_release_is_reported() -> None:
    errors = script.check("## [Unreleased]\n", "0.2.1")
    assert any("released" in error for error in errors)


def test_repository_sources_are_consistent() -> None:
    assert script.main([str(ROOT)]) == 0


def test_main_fails_on_mismatch(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (tmp_path / "CHANGELOG.md").write_text(VALID, encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nversion = "9.9.9"\n', encoding="utf-8"
    )
    assert script.main([str(tmp_path)]) == 1
    assert "9.9.9" in capsys.readouterr().err


def test_main_fails_if_files_are_missing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert script.main([str(tmp_path)]) == 1
    assert "Cannot read" in capsys.readouterr().err
