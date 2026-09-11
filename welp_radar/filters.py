from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from .models import TokenCandidate

@dataclass(frozen=True)
class RadarPolicy:
    min_initial_liquidity_quote: Decimal = Decimal("0")
    allowed_chains: frozenset[str] = frozenset({"ethereum", "bsc", "robinhood", "solana"})
    require_pool: bool = True
    require_creator: bool = False

    def accepts(self, c: TokenCandidate) -> bool:
        if c.chain.lower() not in self.allowed_chains: return False
        if self.require_pool and not c.pool_address: return False
        if self.require_creator and not c.creator: return False
        return c.liquidity_quote >= self.min_initial_liquidity_quote
