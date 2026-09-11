from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

@dataclass(frozen=True)
class SellabilityReport:
    buy_simulated: bool
    sell_simulated: bool
    transfer_simulated: bool
    received_amount_positive: bool
    slippage_bps: int | None
    status: str
    reasons: tuple[str, ...]

class EVMSellabilityAnalyzer:
    """Honeypot gate. A missing/unknown sell result fails closed."""
    def analyze(self, evidence: Mapping[str, Any]) -> SellabilityReport:
        reasons: list[str] = []
        buy = evidence.get("simulation_buy") is True
        sell = evidence.get("simulation_sell") is True
        transfer = evidence.get("simulation_transfer") is True
        received = evidence.get("received_amount_positive") is True
        if not buy: reasons.append("buy simulation not positively verified")
        if not sell: reasons.append("sell simulation not positively verified")
        if not transfer: reasons.append("transfer simulation not positively verified")
        if not received: reasons.append("positive received amount not verified")
        slip = evidence.get("slippage_bps")
        max_slip = evidence.get("max_slippage_bps", 500)
        if slip is None: reasons.append("slippage evidence missing")
        elif int(slip) > int(max_slip): reasons.append("simulated slippage exceeds policy")
        return SellabilityReport(buy, sell, transfer, received, slip,
                                 "PASS" if not reasons else "REJECT", tuple(reasons))
