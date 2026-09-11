from decimal import Decimal
from welp_radar.models import TokenCandidate
from welp_radar.filters import RadarPolicy
from welp_radar.detector import NewTokenRadar

def candidate():
    return TokenCandidate("ethereum", "0xabc", "now", "factory", "0xpool", "uniswap_v2", liquidity_quote=Decimal("100"))

def test_radar_accepts_and_deduplicates():
    r = NewTokenRadar(RadarPolicy(min_initial_liquidity_quote=Decimal("50")))
    assert r.observe(candidate()) is not None
    assert r.observe(candidate()) is None

def test_policy_rejects_insufficient_liquidity():
    r = NewTokenRadar(RadarPolicy(min_initial_liquidity_quote=Decimal("101")))
    assert r.observe(candidate()) is None
