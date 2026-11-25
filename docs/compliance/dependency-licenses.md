# Dependency License Review

## Purpose

This document records the license review of the direct dependencies against the project license `AGPL-3.0-only` (see issue #11). It is not legal advice.

- Review date: 2026-11-25
- Source of license data: PyPI project metadata (license expression) and upstream documentation
- Scope: direct dependencies declared in `pyproject.toml`

## Runtime Dependencies

| Package | License (SPDX) | Status | Compatible with AGPL-3.0-only |
| --- | --- | --- | --- |
| fastapi | MIT | verified | Yes |
| uvicorn | BSD-3-Clause | verified | Yes |
| sqlalchemy | MIT | verified | Yes |
| pydantic | MIT (expected) | open: not verified in this review | To be confirmed |
| cryptography | Apache-2.0 OR BSD-3-Clause | verified | Yes |
| argon2-cffi | MIT | verified | Yes |
| python-multipart | Apache-2.0 | verified | Yes |

Permissive licenses (MIT, BSD-3-Clause, Apache-2.0) allow inclusion in a work licensed under AGPL-3.0. Apache-2.0 is compatible with GPL-3.0 and AGPL-3.0 (one-way: Apache-2.0 code may be combined into an AGPL-3.0 work).

## Build Dependencies (optional)

| Package | License | Assessment |
| --- | --- | --- |
| pyinstaller | GPL-2.0-or-later with Bootloader Exception (Apache-2.0 for a few files) | Build tool only, not a runtime dependency. The exception permits shipping bundles built from the project source under any license, as long as the licenses of the bundled dependencies are respected. |

## Development and Security Tools

pytest, black, ruff, mypy, bandit and safety are used for development and CI only and are not distributed with the application. They are not part of this review.

## Open Items

- Verify the license of `pydantic` and update the table above.
- Transitive dependencies (for example Starlette via FastAPI) are not covered by this review. Follow-up: automated license report in CI (for example `pip-licenses`) with an allow-list.
- Frontend (npm) and Tauri (Cargo) dependencies are out of scope until they are added to the repository.

## Compliance Mapping

| Measure | ISO/IEC 27001:2022 |
| --- | --- |
| License review of dependencies | A.5.32 Intellectual property rights |
