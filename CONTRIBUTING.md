# Contributing to ISMSCompanion

Thank you for your interest in ISMSCompanion. This document explains how you can help and how the project handles contributions.

_Deutsche Fassung: [CONTRIBUTING.de.md](CONTRIBUTING.de.md). If the two versions differ, the English version applies._

## Current policy: no external code contributions

ISMSCompanion is currently developed by a single maintainer. For now, the project **does not accept external code contributions**. This includes pull requests, patches and code snippets. Pull requests from third parties will be closed without a merge, no matter how good they are. Please do not take this personally.

The reason is practical: the maintainer wants to keep all rights in the code in one hand, so that the project can stay available under the `AGPL-3.0-only` license and can additionally be offered under other terms later. Accepting external code would make this much harder. If this policy changes, it will be announced here and in the README.

## How you can still help

Your input is welcome in these forms:

- **Bug reports**: open an issue and describe what you expected, what happened and how to reproduce it.
- **Ideas and feature requests**: open an issue and describe the problem you want to solve. Ideas are treated as suggestions only. The maintainer decides independently if and how to implement them.
- **Questions and feedback**: use the issue tracker or discussions.
- **Security reports**: please do not use public issues. Follow [.github/SECURITY.md](.github/SECURITY.md).

When you write an issue, please describe the problem in words. Please do not paste your own source code or patches, because the project cannot adopt them (see the next section).

## Code and rights in issues

- Do not post code that you wrote and that you expect to be used in the project.
- Short quotes from the existing code of this repository, error messages and log output are fine.
- Do not post code from other projects, especially code under a license that is not compatible with `AGPL-3.0-only`.
- Ideas and suggestions in issues are not treated as contributions of code. The maintainer implements them independently.

## Bots

Dependency update bots such as Renovate may open pull requests that change dependency versions or pins. These are reviewed and merged by the maintainer.

## AI-assisted development

Parts of the project are developed with AI assistance. All AI-generated code is reviewed, tested and adapted by the maintainer. See the note in the [README](README.md).

## Internal workflow (for the maintainer)

This section documents how changes are made, so that the process is transparent.

- **Branches**: one branch per task from the current `main`, named `feature|fix|sec|docs|chore|test/<short-name>`.
- **Commits**: atomic commits in [Conventional Commits](https://www.conventionalcommits.org/) format, in English.
- **Pull requests**: one topic per pull request, using the pull request template. Changes are merged only as a **squash merge** in the GitHub web UI, so that the commit on `main` is signed. See `docs/security/merge-policy.md`.
- **Versioning**: SemVer. The version is bumped as the last commit of a reviewed pull request. Pure documentation, test, chore and CI changes without effect on shipped behavior do not need a bump.
- **Local setup**: `pip install -e ".[dev]"`, then enable the pre-commit hooks.

### Version bump procedure

The version is defined only in `pyproject.toml`. `ismscompanion.__version__` is read from the installed package metadata.

1. Determine the bump level from the commits of the pull request. `MAJOR` applies to breaking changes, `MINOR` to backward-compatible features and `PATCH` to fixes, security changes, performance changes and refactorings. Documentation, test, chore and CI changes without effect on shipped behavior need no bump. The pull request states the level and the reason.
2. Add the bump as the last commit of the reviewed pull request. The commit changes exactly two files: `pyproject.toml` (new `version`) and `CHANGELOG.md` (rename `[Unreleased]` to `[x.y.z] - YYYY-MM-DD` and add a new empty `[Unreleased]` section above it).
3. Run `python scripts/check_version_consistency.py`. The same check runs in CI in the job "Package Build Check".
4. Repeat `pip install -e ".[dev]"` after the change. An editable install keeps the previous version in its metadata, and `tests/test_version.py` fails until it is refreshed.
5. Comparison links at the end of `CHANGELOG.md` are added once tags exist. Tags and releases are created only on explicit instruction of the maintainer.

### Definition of done

- Lint, format and typing checks pass.
- Tests exist for new logic, including security and error paths.
- No secrets and no personal data in the repository.
- New dependencies are justified, pinned and checked for license and known vulnerabilities.
- Documentation and `CHANGELOG.md` are updated.
- UI texts only via i18n (German and English).
- Code comments are written in English.

## License

The project is licensed under the `AGPL-3.0-only`. See [LICENSE](LICENSE).

## Questions

If anything in this document is unclear, please open an issue. Thank you for your understanding and your interest in the project.
