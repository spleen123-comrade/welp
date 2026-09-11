# Data resiliency foundation

Welp treats blockchain data providers as replaceable, untrusted dependencies.

The current foundation provides deterministic sequential failover for read and stream interfaces on EVM and Solana. Later production work will add provider health scoring, latency metrics, circuit breakers, stale-data detection, quorum/consistency checks where useful, and independently managed WebSocket reconnects.

A provider failure must never be interpreted as evidence that a token is safe or that a dangerous event did not happen.
