# Welp

Multi-chain DEX launch intelligence, automated trading, and rug protection.

## Project status

Foundation repository initialized.

## Core goals

- Detect first meaningful liquidity for new tokens across supported chains and DEXs.
- Verify sellability and contract/control risk before any purchase.
- Monitor liquidity providers, creators, controllers, and dangerous state changes.
- Detect the earliest observable precursor to a dangerous action when technically possible.
- Fail closed when critical safety information cannot be verified.
- Support paper trading, replay, testing, and eventually controlled live execution.

## Initial chain scope

- Solana
- Ethereum
- BNB Smart Chain
- Robinhood Chain (EVM-compatible adapter, subject to live protocol/RPC verification)

The architecture is intended to support additional EVM and Solana ecosystems through chain adapters.

## Safety principle

Welp is designed for maximum detectable rug protection, not an impossible guarantee of absolute safety. Private transactions, hidden/off-chain signatures, and atomic transactions can prevent advance observation of some actions. The system therefore rejects opportunities when required protection cannot be established.

## Development rule

Every milestone must preserve the complete prior project state. Previous files and builds must not be deleted. Each milestone is cumulative and must be test-checked before being treated as a stable build.
