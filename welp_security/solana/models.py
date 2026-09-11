from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping

@dataclass(frozen=True)
class SolanaSecurityEvidence:
    mint_authority: str | None = None
    freeze_authority: str | None = None
    update_authority: str | None = None
    lp_authority: str | None = None
    trading_enabled: bool | None = None
    selling_enabled: bool | None = None
    simulation_buy: bool | None = None
    simulation_sell: bool | None = None
    token_program: str | None = None
    evidence_complete: bool = False
    raw: Mapping[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class SolanaSecurityReport:
    status: str
    score: int
    reasons: tuple[str, ...]
    evidence: SolanaSecurityEvidence

    @property
    def passes(self) -> bool: return self.status == "PASS"
