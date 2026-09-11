from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class MarketMetrics:
    price: float
    liquidity: float
    volume: float
    buy_count: int
    sell_count: int

    @property
    def buy_sell_ratio(self) -> float:
        if self.sell_count == 0:
            return float("inf") if self.buy_count else 0.0
        return self.buy_count / self.sell_count


def price_from_reserves(base_reserve: float, quote_reserve: float) -> float:
    if base_reserve <= 0 or quote_reserve <= 0:
        raise ValueError("reserves must be positive")
    return quote_reserve / base_reserve


def constant_product_liquidity(base_reserve: float, quote_reserve: float, quote_price: float = 1.0) -> float:
    if base_reserve < 0 or quote_reserve < 0 or quote_price < 0:
        raise ValueError("reserves and price must be non-negative")
    return quote_reserve + base_reserve * quote_price
