# Welp cbuild-012 — FINAL CROSS-CHECK (Weeks 1–10 + Hardening)

## Scope
This is a cumulative verification milestone. No prior project files are deleted or replaced by this milestone.

## Cross-check
- cbuild-001 through cbuild-011 history remains reachable from the current main lineage.
- Comparison from cbuild-001 to cbuild-011 showed the accumulated project files as additions with zero deletions in that comparison.
- All Weeks 1–10 source areas remain present: core, EVM/Solana chains, DEX, radar, market, security, safety, tests, architecture docs and manifests.
- The previous packaging configuration was incomplete: setuptools package discovery only included `welp_core*` and `welp_chains*`. cbuild-012 fixes this so DEX, radar, market, security and safety packages are included in installation/test discovery.

## Test boundary
The cumulative deterministic test suite must pass before this milestone is considered stable. Live RPC, live DEX execution, real transaction simulation, protocol-specific decoding and production infrastructure remain integration gates.

## Safety
- Unknown security evidence remains a rejection condition.
- Generic approval events never independently trigger an exit.
- Rug protection prefers the earliest observable high-confidence precursor tied to the monitored dangerous action.
- Live trading remains disabled until live integration gates pass.
- No secrets/private keys belong in this public repository.
