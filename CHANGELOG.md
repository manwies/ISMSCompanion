# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- CI builds the sdist and wheel, validates the metadata with `twine check --strict` and verifies the wheel contents.
- The dependency audit in CI runs without an ignore entry. `GHSA-4xh5-x5gv-qwph` (CVE-2025-8869) is fixed in pip 25.3.
- `black` is removed from the `dev` extra and from the configuration. Formatting uses `ruff format`.

### Security

- The `dev` extra requires `pytest>=9.0.3` (CVE-2025-71176, insecure temporary directory handling in earlier versions).

## [0.2.1] - 2026-11-27

### Added

- Python support policy in `docs/python-support-policy.md`.

### Changed

- CI runs `pytest` with coverage on pull requests.
- `mypy` and Bandit (medium severity and above) now fail the CI run instead of being ignored.
- CI runs the tests on Python 3.11 to 3.14 and on 3.15 as a non-blocking experimental job. Lint, type check, dependency audit and Bandit run on Python 3.13.
- Supported Python versions are declared as package classifiers.
- Renovate no longer proposes Python minor or major upgrades.
- The Python package moved to `src/ismscompanion/`. Imports use `ismscompanion.*` instead of `src.*`.
- CI measures coverage for the `ismscompanion` package.

### Removed

- The `ismscompanion-web` console script. Its target module did not exist. It is reintroduced together with the backend.

### Fixed

- `ismscompanion.core.security` is now included in built packages (missing `__init__.py`).
- Package discovery no longer installs a top-level `core` package.
- Project URLs in `pyproject.toml` point to the correct repository.

## [0.2.0] - 2026-11-25

### Added

- Dependency license review in `docs/compliance/dependency-licenses.md`, including versions, sources, method and update policy.

### Changed

- Relicensed from `GPL-3.0-or-later` to `AGPL-3.0-only`. Previously published versions remain under their original license.
- Replaced `LICENSE` with the AGPL-3.0 text.
- Set `license = "AGPL-3.0-only"` in `pyproject.toml`.
- Added SPDX license identifiers to all existing Python source files.
- Updated the license sections in `README.md` and `README.de.md`, including the network use obligation (AGPL-3.0 section 13).

## [0.1.0] - Unreleased

### Added

- Initial project setup: package structure, security policy, CI workflows for linting and security scanning, and the core security module (cryptographic configuration and exceptions).
