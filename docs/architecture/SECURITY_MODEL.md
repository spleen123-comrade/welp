# Welp Security Model

Trust boundaries:
- RPC/WebSocket providers are untrusted data sources.
- Token contracts/programs and DEXs are untrusted inputs.
- User configuration is untrusted until validated.
- Signing credentials are isolated from read-only analysis.

Rules:
- Never execute arbitrary code supplied by a token.
- Never commit private keys or secrets.
- Validate chain IDs and address formats.
- Bound network timeouts and response sizes.
- Deduplicate events and record source/timestamps.
- Fail closed when critical security evidence is unavailable.
- Separate read-only intelligence from execution.
