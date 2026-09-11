from decimal import Decimal
import pytest
from welp_dex.models import DEXProtocol
from welp_dex.registry import DEXRegistry
from welp_dex.normalizer import normalize_pool_event, normalize_swap_event, normalize_liquidity_event

def test_registry_case_insensitive():
    r = DEXRegistry.initial()
    assert r.get("Ethereum", "UNISWAP_V2").name == "uniswap_v2"

def test_normalizers():
    p = normalize_pool_event({"chain":"ethereum","dex":"uniswap_v2","pool_address":"p","token_address":"t","liquidity_quote":"10"})
    assert p.liquidity_quote == Decimal("10")
    s = normalize_swap_event({"chain":"ethereum","dex":"uniswap_v2","pool_address":"p","token_address":"t","side":"BUY","token_amount":"2","quote_amount":"3"})
    assert s.side == "buy" and s.quote_amount == Decimal("3")
    l = normalize_liquidity_event({"chain":"solana","dex":"raydium","pool_address":"p","token_address":"t","action":"add","quote_delta":"100","quote_reserve":"100"})
    assert l.action == "add"

def test_bad_swap_rejected():
    with pytest.raises(ValueError): normalize_swap_event({"chain":"e","dex":"d","pool_address":"p","token_address":"t","side":"hold"})
