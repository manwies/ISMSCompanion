# Dependency License Review

## Purpose

This document records the license review of the direct dependencies against the project license `AGPL-3.0-only` (see issue #11). It serves as evidence for ISO/IEC 27001:2022 A.5.32 until an automated report replaces it (see issue #17). It is not legal advice.

- Review date: 2026-11-25
- Scope: direct dependencies declared in `pyproject.toml`
- Versions: the table lists the latest release on PyPI on the review date. The versions pinned by lock files or Renovate were not checked.

## Runtime Dependencies

| Package | Version reviewed | License (SPDX) | Source | Compatible with AGPL-3.0-only |
| --- | --- | --- | --- | --- |
| fastapi | 0.165.0 | MIT | [upstream LICENSE](https://github.com/fastapi/fastapi/blob/master/LICENSE), [deps.dev](https://deps.dev/pypi/fastapi) | Yes |
| uvicorn | 0.54.0 | BSD-3-Clause | [PyPI](https://pypi.org/project/uvicorn/) (license expression) | Yes |
| sqlalchemy | 2.1.9 | MIT | [PyPI](https://pypi.org/project/SQLAlchemy/), [upstream LICENSE](https://github.com/sqlalchemy/sqlalchemy/blob/main/LICENSE) | Yes |
| pydantic | 2.14.4 | MIT | [PyPI](https://pypi.org/project/pydantic/), [upstream LICENSE](https://github.com/pydantic/pydantic/blob/main/LICENSE) | Yes |
| cryptography | 50.0.2 | Apache-2.0 OR BSD-3-Clause | [PyPI](https://pypi.org/project/cryptography/) (license expression) | Yes |
| argon2-cffi | 25.1.0 | MIT | [PyPI](https://pypi.org/project/argon2-cffi/) (license expression) | Yes |
| python-multipart | 0.0.34 | Apache-2.0 | [PyPI](https://pypi.org/project/python-multipart/) (license expression) | Yes |

MIT and BSD-3-Clause are permissive licenses that can be included in a work licensed under AGPL-3.0. Apache-2.0 is commonly considered compatible with GPL-3.0 and AGPL-3.0 (one-way: Apache-2.0 code may be combined into an AGPL-3.0 work). This statement was not independently verified in this review; see the FSF license list and confirm with legal counsel if needed. For `cryptography` the `OR` expression allows choosing BSD-3-Clause.

## Build Dependencies (optional)

| Package | License | Source | Assessment |
| --- | --- | --- | --- |
| pyinstaller | GPL 2.0 with an exception for bundled applications; Apache-2.0 for a few files | [PyInstaller documentation (6.22.3)](https://pyinstaller.org/en/stable/license.html) | Build tool only, not a runtime dependency. According to the upstream documentation, bundles generated from the project source can be shipped under any license, as long as the licenses of the bundled dependencies are respected. |

## Development and Security Tools

pytest, pytest-cov, ruff, mypy, bandit, safety, pip-audit, build and twine are used for development and CI only and are not distributed with the application. They are not part of this review.

## Method and Update Policy

- Method: manual review. The SPDX license expression published on PyPI was compared with the upstream `LICENSE` file where available. Results are recorded with version and source in the tables above.
- Update policy: repeat the review when a direct dependency is added or replaced, when a major release changes the license, and at least quarterly until the automated report from issue #17 is in place.
- A dependency with a license outside the permissive set above must be assessed and documented before it is merged.

## Limitations

- License metadata on PyPI is declared by the package authors and may be incomplete or wrong.
- Transitive dependencies (for example Starlette via FastAPI) are not covered by this review.
- Frontend (npm) and Tauri (Cargo) dependencies are out of scope until they are added to the repository.

## Open Items

- Automated license report with allow-list in CI, including transitive dependencies: issue #17.

## Compliance Mapping

| Measure | ISO/IEC 27001:2022 |
| --- | --- |
| License review of dependencies | A.5.32 Intellectual property rights |
