# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Python support policy in `docs/python-support-policy.md`.

### Changed

- CI runs `pytest` with coverage on pull requests.
- `mypy` and Bandit (medium severity and above) now fail the CI run instead of being ignored.
- CI runs the tests on Python 3.11 to 3.14 and on 3.15 as a non-blocking experimental job. Lint, type check, dependency audit and Bandit run on Python 3.13.
- Supported Python versions are declared as package classifiers.
- Renovate no longer proposes Python minor or major upgrades.

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
