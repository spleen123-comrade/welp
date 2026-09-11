from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from .models import MarketSnapshot

@dataclass
class MarketSnapshotBuilder:
    """Build deterministic market snapshots from aggregated observations."""
    def build(self, *, chain: str, token_address: str, pool_address: str, price_quote: Decimal, liquidity_quote: Decimal, volume_quote: Decimal, buys: int, sells: int, observed_at: str, block_or_slot: int | None = None) -> MarketSnapshot:
        if price_quote < 0 or liquidity_quote < 0 or volume_quote < 0: raise ValueError("market values cannot be negative")
        if buys < 0 or sells < 0: raise ValueError("trade counts cannot be negative")
        return MarketSnapshot(chain, token_address, pool_address, price_quote, liquidity_quote, volume_quote, buys, sells, observed_at, block_or_slot)
