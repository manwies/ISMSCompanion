# SPDX-License-Identifier: AGPL-3.0-only
"""Consistency checks for version sources."""

import tomllib
from pathlib import Path

import src


def test_package_version_matches_pyproject() -> None:
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with pyproject.open("rb") as handle:
        data = tomllib.load(handle)
    assert src.__version__ == data["project"]["version"]
