# cbuild-003 — Week 2

## Scope
Generic EVM adapter, normalized EVM events, Ethereum/BSC network definitions, Robinhood Chain adapter placeholder, and deterministic provider failover.

## Safety
Read/streaming only. No wallet signing, arbitrary contract execution, or live trading.

## Verification
The adapter is tested with deterministic fake providers for health, block height, transaction lookup, event normalization, malformed events, and provider failover.
