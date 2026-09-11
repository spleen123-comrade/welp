# Welp Component Map

- `welp_core`: chain-agnostic domain contracts, configuration and normalized events.
- `welp_chains.evm`: generic EVM adapter and provider failover foundation.
- `welp_chains.solana`: generic Solana adapter and provider failover foundation.
- Future domains: DEX discovery, token security, sellability, wallets, holders, protected state, precursor detection, risk, execution, portfolio, alerts, replay and paper trading.

Dependency direction: UI/API -> application/domain -> interfaces -> adapters. Adapters never import UI code. Domain models stay chain-agnostic where practical.
