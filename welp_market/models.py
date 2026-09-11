from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class FirstLiquidityResult:
    chain: str
    pool_address: str
    token_address: str
    first_meaningful: bool
    quote_liquidity: Decimal
    transaction_id: str | None
    block_or_slot: int | None
    reason: str

@dataclass(frozen=True)
class MarketSnapshot:
    chain: str
    token_address: str
    pool_address: str
    price_quote: Decimal
    liquidity_quote: Decimal
    volume_quote: Decimal
    buys: int
    sells: int
    observed_at: str
    block_or_slot: int | None = None

    @property
    def buy_sell_ratio(self) -> Decimal:
        if self.sells == 0: return Decimal("Infinity") if self.buys else Decimal("0")
        return Decimal(self.buys) / Decimal(self.sells)
