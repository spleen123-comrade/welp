from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

@dataclass(frozen=True)
class EVMControlFinding:
    control: str
    enabled: bool | None
    authority: str | None
    evidence: str
    dangerous: bool

@dataclass(frozen=True)
class EVMDeepReport:
    findings: tuple[EVMControlFinding, ...]
    complete: bool
    missing: tuple[str, ...]

class EVMDeepAnalyzer:
    """Evidence-driven second layer. Unknown authority/state is never treated as safe."""
    REQUIRED = ("bytecode", "owner", "admin", "upgradeable", "simulation_sell", "simulation_transfer")

    def analyze(self, evidence: Mapping[str, Any]) -> EVMDeepReport:
        missing = tuple(k for k in self.REQUIRED if k not in evidence or evidence[k] is None)
        findings: list[EVMControlFinding] = []
        controls = (
            ("mint", "mint_enabled"), ("blacklist", "blacklist_enabled"),
            ("fee_change", "fee_changeable"), ("max_tx", "max_tx_changeable"),
            ("max_wallet", "max_wallet_changeable"), ("pause", "trading_enabled"),
        )
        for name, key in controls:
            value = evidence.get(key)
            findings.append(EVMControlFinding(name, value if isinstance(value, bool) else None,
                                               evidence.get(f"{key}_authority") or evidence.get("owner"),
                                               f"evidence:{key}", value is True))
        complete = bool(evidence.get("evidence_complete")) and not missing
        return EVMDeepReport(tuple(findings), complete, missing)
