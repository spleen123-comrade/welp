from __future__ import annotations
from dataclasses import dataclass
from .models import EVMControlState, SecurityDecision

@dataclass
class EVMContractAnalyzer:
    minimum_score: int = 80

    def analyze(self, evidence: dict) -> SecurityDecision:
        """Analyze supplied read/simulation evidence and fail closed if incomplete."""
        reasons: list[str] = []
        score = 100
        state = EVMControlState(
            owner=evidence.get("owner"), admin=evidence.get("admin"), proxy_admin=evidence.get("proxy_admin"),
            upgradeable=bool(evidence.get("upgradeable", False)),
            trading_enabled=evidence.get("trading_enabled"), selling_enabled=evidence.get("selling_enabled"),
            mint_enabled=evidence.get("mint_enabled"), blacklist_enabled=evidence.get("blacklist_enabled"),
            whitelist_enabled=evidence.get("whitelist_enabled"), fee_changeable=evidence.get("fee_changeable"),
            max_tx_changeable=evidence.get("max_tx_changeable"), max_wallet_changeable=evidence.get("max_wallet_changeable"),
            evidence_complete=bool(evidence.get("evidence_complete", False)), raw=evidence,
        )
        if not state.evidence_complete:
            return SecurityDecision("REJECT", 0, ("critical security evidence is incomplete",), state)
        if state.selling_enabled is not True:
            reasons.append("selling is not positively verified as enabled"); score -= 40
        if state.trading_enabled is not True:
            reasons.append("trading is not positively verified as enabled"); score -= 20
        for label, value, penalty in (("mint", state.mint_enabled, 15), ("blacklist", state.blacklist_enabled, 10), ("fee", state.fee_changeable, 10), ("max-tx", state.max_tx_changeable, 5), ("max-wallet", state.max_wallet_changeable, 5)):
            if value is True:
                reasons.append(f"{label} control remains changeable"); score -= penalty
        if state.upgradeable:
            reasons.append("contract is upgradeable"); score -= 10
        if score < 0: score = 0
        status = "PASS" if score >= self.minimum_score and not reasons else "REJECT"
        return SecurityDecision(status, score, tuple(reasons), state)
