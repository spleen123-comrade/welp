# Welp Project Rules

## Version preservation

1. Never delete project files as part of normal development.
2. Every progress milestone is a complete cumulative build (cbuild).
3. A new cbuild contains all prior project work plus the latest changes.
4. Preserve previous stable states so rollback remains possible.
5. Do not overwrite a protected baseline without explicitly creating a newer milestone.

## Engineering safety

1. Test imports, integration points, and core functionality before declaring a milestone complete.
2. Security-critical logic must fail closed when required evidence is unavailable.
3. No live trading by default during development; paper/simulation mode comes first.
4. Rug protection must prefer the earliest observable high-confidence precursor to a dangerous action, rather than simply racing the final transaction.
5. Never trigger an exit from a generic approval event alone; the event must be linked to the monitored token, pool/LP position, controller, and dangerous action path.

## Build naming

Milestones use cumulative cbuild numbering beginning with `cbuild-001`.
