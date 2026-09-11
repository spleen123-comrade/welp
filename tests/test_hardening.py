from welp_dex.adapters import GenericDEXAdapter, RawDEXEvent
from welp_market.analytics import price_from_reserves
from welp_security.evidence import check_prebuy_evidence
from welp_security.evm.bytecode import extract_selectors, normalize_bytecode


def test_dex_adapter_rejects_wrong_protocol():
    adapter = GenericDEXAdapter("ethereum", "uniswap_v2")
    event = RawDEXEvent("bsc", "pancakeswap_v2", "swap", "0x1", 1)
    try:
        adapter.normalize(event)
    except ValueError:
        return
    assert False


def test_market_price():
    assert price_from_reserves(2, 10) == 5


def test_bytecode_selector_evidence():
    assert normalize_bytecode("0x63abcdef01") == "63abcdef01"
    assert "0xabcdef01" in extract_selectors("0x63abcdef01")


def test_prebuy_evidence_fails_closed_when_missing():
    report = check_prebuy_evidence({"evidence_complete": True})
    assert not report.complete
    assert "selling_enabled" in report.missing
