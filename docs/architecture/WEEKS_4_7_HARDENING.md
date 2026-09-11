# Weeks 4–7 hardening status

This document records the cleanup pass applied after the initial Weeks 4–7 foundation.

## Preserved
- All earlier cbuilds and source files remain in the repository.
- No prior project file is deleted by this pass.
- Live trading remains disabled.

## Added/strengthened
- Protocol-neutral DEX adapter contract so protocol-specific decoders can be plugged in without changing the normalized event model.
- Radar ingestion pipeline around the existing candidate filters/deduplication.
- Deterministic market price/liquidity analytics.
- EVM bytecode selector extraction as evidence only.
- Exact EIP-1967 slot checks instead of a broad storage-key heuristic.
- Explicit EVM control findings and pre-buy evidence completeness checks.
- Regression coverage for the new hardening layer.

## Still deliberately blocked from being called production-complete
- Live RPC/WebSocket DEX discovery and protocol-specific event decoders.
- Verified protocol addresses/program IDs from live chain configuration.
- Full ABI/bytecode semantic analysis and proxy implementation discovery.
- Real buy/sell simulation against live state.
- Controller/owner/upgrade authority resolution across every protocol.
- Mempool/private-orderflow visibility and earliest precursor detection.
- Solana program-specific security semantics.

Those items require live infrastructure and protocol-specific integration. Welp must fail closed rather than pretend deterministic fixtures provide live-chain guarantees.
