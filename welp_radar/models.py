from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Mapping

@dataclass(frozen=True)
class TokenCandidate:
    chain: str
    token_address: str
    first_seen_at: str
    source: str
    pool_address: str | None = None
    dex: str | None = None
    creator: str | None = None
    liquidity_quote: Decimal = Decimal("0")
    initial_price: Decimal | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)
