from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Mapping

@dataclass(frozen=True)
class DEXProtocol:
    chain: str
    name: str
    factory_or_program: str
    pool_type: str
    enabled: bool = True

@dataclass(frozen=True)
class PoolObservation:
    chain: str
    dex: str
    pool_address: str
    token_address: str
    quote_address: str | None
    block_or_slot: int | None
    transaction_id: str | None
    observed_at: str | None
    liquidity_quote: Decimal = Decimal("0")
    payload: Mapping[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class SwapObservation:
    chain: str
    dex: str
    pool_address: str
    token_address: str
    side: str
    token_amount: Decimal
    quote_amount: Decimal
    block_or_slot: int | None
    transaction_id: str | None
    payload: Mapping[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class LiquidityObservation:
    chain: str
    dex: str
    pool_address: str
    token_address: str
    action: str
    quote_delta: Decimal
    quote_reserve: Decimal
    block_or_slot: int | None
    transaction_id: str | None
    provider: str | None = None
    payload: Mapping[str, Any] = field(default_factory=dict)
