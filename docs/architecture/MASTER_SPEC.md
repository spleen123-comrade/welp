# Welp Master Technical Specification

## Purpose
Welp detects newly meaningful DEX liquidity, evaluates token and wallet risk, calculates user-defined trade risk, executes only after a safety gate passes, and continuously protects positions against observable dangerous state changes.

## System layers
1. Presentation: dashboard, token radar, positions, history, analytics, security, settings.
2. API/application: authentication, user settings, portfolio, alerts, orchestration.
3. Domain/core: normalized blockchain events, token intelligence, protected state, risk, execution decisions.
4. Chain adapters: EVM and Solana interfaces with protocol-specific implementations.
5. DEX adapters: normalized pool/swap/liquidity interfaces.
6. Data: transactional database, event storage, market snapshots, audit log.
7. Infrastructure: RPC/WebSocket providers, health, failover, queues, observability.

## Safety flow
Detect -> identify -> fast reject -> deep verification -> sellability -> liquidity/LP -> wallet/holder -> protected-state baseline -> monitoring capability -> risk calculation -> PASS/REJECT -> execution -> continuous protection.

## Risk modes
- Percentage: configured percentage of balance basis excluding unrealized P/L.
- Fixed USD: configured USD risk budget converted to chain/quote units.
- Position size is derived from entry-to-protective-exit risk distance and constrained by exposure, liquidity, slippage, fees and gas.

## Rug protection
Every position has a protected-state map. Dangerous actions have an action registry describing required authorization/control paths and observable precursors. A generic approval is never enough; a precursor must be linked to the monitored token/pool/position and dangerous action.

## Observability
Public mempools do not expose every path. Private submission, hidden/off-chain signatures and atomic operations can remove a separate precursor. Welp records that limitation and uses the safest available fallback rather than claiming certainty.

## Initial chains
Ethereum, BSC, Robinhood Chain adapter, Solana. The architecture is extensible to Base, Arbitrum, Polygon, Avalanche, Optimism and additional protocols.

## Development gate
Live trading is disabled during development. Initial adapters are read/streaming foundations with deterministic fixtures; signing and execution are later, separately gated services.
