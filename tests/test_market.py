from decimal import Decimal
from welp_dex.models import LiquidityObservation
from welp_market.liquidity import FirstLiquidityDetector
from welp_market.snapshots import MarketSnapshotBuilder

def test_first_meaningful_liquidity():
    d = FirstLiquidityDetector(Decimal("100"))
    e = LiquidityObservation("ethereum","dex","pool","token","add",Decimal("100"),Decimal("100"),1,"tx")
    r = d.observe(e)
    assert r.first_meaningful and r.quote_liquidity == Decimal("100")
    assert d.observe(e).transaction_id == "tx"

def test_snapshot_ratio():
    s = MarketSnapshotBuilder().build(chain="e", token_address="t", pool_address="p", price_quote=Decimal("2"), liquidity_quote=Decimal("100"), volume_quote=Decimal("20"), buys=4, sells=2, observed_at="now")
    assert s.buy_sell_ratio == Decimal("2")
