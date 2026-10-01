# WELP Build Storage Policy

## Mandatory cumulative rule

Every WELP milestone/build must be stored persistently in the repository. Chat-only instructions, local-only artifacts, or unrecorded milestone decisions are not considered stored.

For every cumulative CBUILD, preserve and record:
- milestone/build identifier
- predecessor build
- scope and acceptance criteria
- implementation artifacts
- verification/test evidence
- source-tree SHA-256
- cumulative manifest and deletion/change audit
- release notes
- protected-baseline/lock record when verification passes
- cumulative ZIP provenance where applicable

Historical builds must not be deleted, overwritten, silently simplified, or replaced.

Signing and broadcast boundaries remain explicitly recorded and locked unless a later milestone independently verifies a permitted transition.

## Current baseline

- Protected architecture baseline: CBUILD-799
- Milestone: A_ARCHITECTURE
- Predecessor: CBUILD-798
- Source-tree SHA-256: e03f05d2217638b2072e2d02745f31512b6fc49a84b8a8d7e3e391da0450650b
- Architecture audit: PASS
- Cumulative audit: PASS
- Signing: LOCKED
- Broadcast: LOCKED

## Next cumulative milestone

- Build: CBUILD-800
- Combined milestone: B+C
- B: BUILD_IDENTITY
- C: CUMULATIVE_INTEGRITY
- Parent baseline: CBUILD-799

This policy is repository-level and applies to subsequent cumulative builds.
