# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Smoke tests for the core security module (`crypto_config`, `exceptions`) and a version consistency test.
- CI job running `pytest` with coverage on pull requests and pushes to `main`.
- `pytest-cov` as development dependency.

### Changed

- CI workflow runs with read-only `contents` permission, cancels superseded pull request runs and has job timeouts.
- `mypy` and Bandit (medium severity and above) now fail the CI run instead of being ignored.

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
