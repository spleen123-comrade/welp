from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping
from .models import SolanaSecurityEvidence, SolanaSecurityReport

@dataclass
class SolanaSecurityAnalyzer:
    minimum_score: int = 80

    def analyze(self, evidence: Mapping[str, Any]) -> SolanaSecurityReport:
        e = SolanaSecurityEvidence(**{k: evidence.get(k) for k in SolanaSecurityEvidence.__dataclass_fields__ if k != "raw"}, raw=evidence)
        reasons: list[str] = []
        score = 100
        if not e.evidence_complete: return SolanaSecurityReport("REJECT", 0, ("critical Solana security evidence is incomplete",), e)
        if e.selling_enabled is not True: reasons.append("selling not positively verified"); score -= 35
        if e.simulation_sell is not True: reasons.append("sell simulation not positively verified"); score -= 35
        if e.simulation_buy is not True: reasons.append("buy simulation not positively verified"); score -= 10
        if e.freeze_authority: reasons.append("freeze authority remains active"); score -= 10
        if e.mint_authority: reasons.append("mint authority remains active"); score -= 10
        if e.update_authority: reasons.append("metadata/program update authority remains active"); score -= 5
        score = max(0, score)
        status = "PASS" if score >= self.minimum_score and not reasons else "REJECT"
        return SolanaSecurityReport(status, score, tuple(reasons), e)
