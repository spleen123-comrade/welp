# Weeks 7–10 Completion Matrix

This document is the explicit handoff matrix for the security stages. It prevents unfinished requirements from being silently treated as complete.

| Week | Capability | Implemented foundation | Live integration gate |
|---|---|---|---|
| 7 | EVM security | control state, selector evidence, bytecode evidence, deep findings, controller evidence | live ABI/bytecode decoding, proxy/controller resolution, chain RPC reads |
| 8 | Sellability/honeypot | buy/sell/transfer gate, slippage evidence, simulation gateway | live fork/state simulation and real router execution simulation |
| 9 | Solana security | authority model, instruction context, simulation gateway, fail-closed scoring | real program parsers, account-state simulation and DEX-specific execution |
| 10 | Pre-buy gate | cross-chain fail-closed decision layer | wire every production detector/provider into the gate before enabling trading |

## Non-negotiable safety rules

1. Unknown is not safe.
2. A function selector alone never proves behavior.
3. An `approve` alone never triggers an exit; the authorization must be linked to the monitored asset/pool/position and dangerous action.
4. EVM and Solana use different security models.
5. The final buy gate requires positive evidence for every critical check.
6. Live trading remains disabled until live-chain integration tests pass.
7. Private transactions, hidden signatures and atomic actions can defeat advance observation; Welp therefore rejects opportunities where required protection cannot be established.
