# Python Support Policy

## Supported versions

The project supports every CPython version that still receives security fixes
upstream and for which all runtime dependencies provide compatible releases.
The status of each version is published in the
[Python Developer Guide](https://devguide.python.org/versions/).

| Version | Role | Upstream end of life |
|---------|------|----------------------|
| 3.11 | Minimum supported version | 2027-10-31 |
| 3.12 | Supported | 2028-10-31 |
| 3.13 | Primary version (lint, type check, audit, Bandit) | 2029-10-31 |
| 3.14 | Supported | 2030-10-31 |
| 3.15 | Experimental (non-blocking in CI) | 2031-10-31 |

## Rules

- The minimum supported version is declared in `requires-python`
  (`pyproject.toml`). `ruff` and `mypy` target this version.
- The primary version is defined in `.python-version`. Format, lint, type
  check, dependency audit and Bandit run on it.
- Tests run on every supported version. Newly released versions are added as
  experimental and promoted after dependency compatibility is confirmed.
- A version is dropped from the supported range in the release that follows
  its upstream end of life at the latest. After end of life no security fixes
  are published, which conflicts with vulnerability management requirements
  (ISO/IEC 27001 Annex A 8.8).
- Minor and major Python upgrades are not proposed by Renovate. The range is
  reviewed once per year after the October release of CPython. Patch updates
  of the CI interpreter are applied automatically.

## Runtime environments

Container images and bundled desktop artifacts ship their own interpreter, so
the primary version applies. Source and `pip` installations use the
interpreter of the host, which must lie within the supported range.

## Planned changes

- 2027-10: remove Python 3.11 from the supported range and raise
  `requires-python`, `ruff` `target-version` and `mypy` `python_version`.
