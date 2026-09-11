from __future__ import annotations
from decimal import Decimal, InvalidOperation
from .models import PoolObservation, SwapObservation, LiquidityObservation

def _d(value: object) -> Decimal:
    try: return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc: raise ValueError(f"invalid decimal: {value!r}") from exc

def normalize_pool_event(raw: dict) -> PoolObservation:
    required = ("chain", "dex", "pool_address", "token_address")
    missing = [k for k in required if not raw.get(k)]
    if missing: raise ValueError(f"missing pool fields: {missing}")
    return PoolObservation(raw["chain"], raw["dex"], raw["pool_address"], raw["token_address"], raw.get("quote_address"), raw.get("block_or_slot"), raw.get("transaction_id"), raw.get("observed_at"), _d(raw.get("liquidity_quote", 0)), raw.get("payload", {}))

def normalize_swap_event(raw: dict) -> SwapObservation:
    required = ("chain", "dex", "pool_address", "token_address", "side")
    missing = [k for k in required if not raw.get(k)]
    if missing: raise ValueError(f"missing swap fields: {missing}")
    side = str(raw["side"]).lower()
    if side not in {"buy", "sell"}: raise ValueError("swap side must be buy or sell")
    return SwapObservation(raw["chain"], raw["dex"], raw["pool_address"], raw["token_address"], side, _d(raw.get("token_amount", 0)), _d(raw.get("quote_amount", 0)), raw.get("block_or_slot"), raw.get("transaction_id"), raw.get("payload", {}))

def normalize_liquidity_event(raw: dict) -> LiquidityObservation:
    required = ("chain", "dex", "pool_address", "token_address", "action")
    missing = [k for k in required if not raw.get(k)]
    if missing: raise ValueError(f"missing liquidity fields: {missing}")
    action = str(raw["action"]).lower()
    if action not in {"add", "remove", "increase", "decrease", "migrate"}: raise ValueError("unsupported liquidity action")
    return LiquidityObservation(raw["chain"], raw["dex"], raw["pool_address"], raw["token_address"], action, _d(raw.get("quote_delta", 0)), _d(raw.get("quote_reserve", 0)), raw.get("block_or_slot"), raw.get("transaction_id"), raw.get("provider"), raw.get("payload", {}))
