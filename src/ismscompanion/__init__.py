# SPDX-License-Identifier: AGPL-3.0-only
"""ISMSCompanion - Information Security Management System Companion.

A comprehensive ISMS tool supporting multiple security standards.
"""

from importlib.metadata import PackageNotFoundError, version

# The version is defined once in pyproject.toml and read from the installed
# distribution metadata. The fallback keeps imports working from a plain
# source tree; tests compare the value with pyproject.toml.
try:
    __version__ = version("ismscompanion")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__author__ = "ISMSCompanion Team"
