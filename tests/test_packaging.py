# SPDX-License-Identifier: AGPL-3.0-only
"""Packaging completeness checks."""

from pathlib import Path

from setuptools import find_packages

import ismscompanion

PACKAGE_ROOT = Path(ismscompanion.__file__).resolve().parent


def test_every_module_directory_has_init() -> None:
    missing = sorted(
        str(directory.relative_to(PACKAGE_ROOT))
        for directory in PACKAGE_ROOT.rglob("*")
        if directory.is_dir()
        and directory.name != "__pycache__"
        and any(directory.rglob("*.py"))
        and not (directory / "__init__.py").exists()
    )
    assert missing == []


def test_setuptools_discovers_all_subpackages() -> None:
    source_root = PACKAGE_ROOT.parent
    discovered = set(
        find_packages(where=str(source_root), include=["ismscompanion*"])
    )
    on_disk = {
        ".".join(init.relative_to(source_root).parent.parts)
        for init in PACKAGE_ROOT.rglob("__init__.py")
    }
    assert discovered == on_disk
