from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Mapping

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

@dataclass(frozen=True)
class ChainRef:
    name: str
    chain_id: int | None = None

@dataclass(frozen=True)
class NormalizedEvent:
    chain: ChainRef
    event_type: str
    event_id: str
    observed_at: datetime
    source: str
    block_or_slot: int | None = None
    transaction_id: str | None = None
    payload: Mapping[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class TokenRef:
    chain: ChainRef
    address: str
    symbol: str | None = None
    decimals: int | None = None

@dataclass(frozen=True)
class PoolRef:
    chain: ChainRef
    address: str
    dex: str
    token: TokenRef
    quote_address: str | None = None

@dataclass(frozen=True)
class RiskBudget:
    mode: str
    value: Decimal
    balance_basis_usd: Decimal | None = None

    def validate(self) -> None:
        if self.mode not in {"percent_balance", "fixed_usd"}:
            raise ValueError("invalid risk mode")
        if self.value <= 0:
            raise ValueError("risk value must be positive")
