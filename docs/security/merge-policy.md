# Merge and Commit Signing Policy

## Purpose

This policy describes how changes reach `main` and how their integrity remains verifiable.

## Rules

- Direct pushes to `main` are blocked (branch ruleset, empty bypass list).
- Changes reach `main` only through pull requests.
- Required status checks: `Format & Lint Check` and `Security Scan (Bandit)`. The branch must be up to date.
- At least one approval is required. Stale approvals are dismissed on new commits, and the approval must cover the most recent push.
- All review conversations must be resolved.
- Force pushes and deletion of `main` are blocked. History is linear.
- Merges are done exclusively as **squash merges** in the GitHub web UI. Merge commits and rebase merges are disabled.
- Signed commits are required on `main`.

## Commit Signing Decision

Feature branches do not require signed commits. Commits on feature branches are created through the GitHub API (connector) and are unsigned. The squash merge in the web UI creates a commit on `main` that is signed by GitHub (status "Verified", committer `GitHub`).

Rationale: Private signing keys must not be shared with third parties or connectors. The signature on `main` shows that the commit was created through GitHub.

## Residual Risk

- The signature on `main` does not prove authorship of individual feature-branch commits.
- The authoritative evidence for review and approval is the pull request history (reviews, approvals, status checks).
- A compromised account with admin rights could change the ruleset. Mitigations: 2FA with a passkey or hardware key, least-privilege tokens with an expiry date.

## Compliance Mapping

| Measure | ISO/IEC 27001:2022 |
| --- | --- |
| Mandatory PRs, approvals, required checks | A.8.32 Change management |
| Branch ruleset, no bypass, signature on `main` | A.8.4 Access to source code |
| Linear history, signature, PR history | A.8.15 Logging (traceability) |

Mappings to NIS2, BSI IT-Grundschutz and TISAX will be added when the control catalog is created.

## Verification

- After the first merge, verify that the squash commit on `main` is shown as "Verified".
- Review the ruleset configuration against this policy regularly (for example quarterly).
