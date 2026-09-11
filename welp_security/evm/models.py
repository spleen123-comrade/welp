from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping

@dataclass(frozen=True)
class EVMControlState:
    owner: str | None = None
    admin: str | None = None
    proxy_admin: str | None = None
    upgradeable: bool = False
    trading_enabled: bool | None = None
    selling_enabled: bool | None = None
    mint_enabled: bool | None = None
    blacklist_enabled: bool | None = None
    whitelist_enabled: bool | None = None
    fee_changeable: bool | None = None
    max_tx_changeable: bool | None = None
    max_wallet_changeable: bool | None = None
    evidence_complete: bool = False
    raw: Mapping[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class SecurityDecision:
    status: str
    score: int
    reasons: tuple[str, ...]
    protected_state: EVMControlState

    @property
    def passes(self) -> bool:
        return self.status == "PASS"
