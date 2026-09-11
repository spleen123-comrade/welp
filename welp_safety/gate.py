from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

@dataclass(frozen=True)
class SafetyDecision:
    status: str
    reasons: tuple[str, ...]
    checks: Mapping[str, bool]

    @property
    def allowed(self) -> bool: return self.status == "ALLOW"

class PreBuySafetyGate:
    """Final fail-closed gate. Unknown critical evidence is never interpreted as safe."""
    REQUIRED = ("sellability", "contract_security", "liquidity", "authority_monitoring", "exit_path", "fresh_data")
    def evaluate(self, evidence: Mapping[str, Any]) -> SafetyDecision:
        checks = {k: evidence.get(k) is True for k in self.REQUIRED}
        reasons = tuple(f"{k} check failed or is unknown" for k, ok in checks.items() if not ok)
        if evidence.get("chain") not in {"ethereum", "bsc", "solana", "robinhood"}:
            reasons += ("unsupported or unverified chain",)
        return SafetyDecision("ALLOW" if not reasons else "REJECT", reasons, checks)
