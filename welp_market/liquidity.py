from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from collections import defaultdict
from welp_dex.models import LiquidityObservation
from .models import FirstLiquidityResult

@dataclass
class FirstLiquidityDetector:
    minimum_quote_liquidity: Decimal = Decimal("0")

    def __post_init__(self):
        self._first_seen: dict[tuple[str,str], FirstLiquidityResult] = {}
        self._reserves: dict[tuple[str,str], Decimal] = defaultdict(Decimal)

    def observe(self, event: LiquidityObservation) -> FirstLiquidityResult:
        key = (event.chain.lower(), event.pool_address.lower())
        previous = self._reserves[key]
        reserve = event.quote_reserve if event.quote_reserve > 0 else max(Decimal("0"), previous + event.quote_delta)
        self._reserves[key] = reserve
        if key not in self._first_seen and event.action in {"add", "increase"} and reserve >= self.minimum_quote_liquidity:
            result = FirstLiquidityResult(event.chain, event.pool_address, event.token_address, True, reserve, event.transaction_id, event.block_or_slot, "first observed meaningful liquidity")
            self._first_seen[key] = result
            return result
        return self._first_seen.get(key) or FirstLiquidityResult(event.chain, event.pool_address, event.token_address, False, reserve, event.transaction_id, event.block_or_slot, "not first meaningful liquidity")
