# SPDX-License-Identifier: AGPL-3.0-only
"""Consistency checks for version sources."""

import importlib
import importlib.metadata
import tomllib
from pathlib import Path

import pytest

import ismscompanion


def test_package_version_matches_pyproject() -> None:
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with pyproject.open("rb") as handle:
        data = tomllib.load(handle)
    assert ismscompanion.__version__ == data["project"]["version"]


def test_version_falls_back_if_metadata_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_not_found(name: str) -> str:
        raise importlib.metadata.PackageNotFoundError(name)

    monkeypatch.setattr(importlib.metadata, "version", raise_not_found)
    try:
        reloaded = importlib.reload(ismscompanion)
        assert reloaded.__version__ == "0.0.0+unknown"
    finally:
        monkeypatch.undo()
        importlib.reload(ismscompanion)
