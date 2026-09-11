from welp_security.evm.analyzer import EVMContractAnalyzer
from welp_security.evm.selectors import classify_selector

def safe():
    return {"evidence_complete":True,"selling_enabled":True,"trading_enabled":True,"mint_enabled":False,"blacklist_enabled":False,"fee_changeable":False,"max_tx_changeable":False,"max_wallet_changeable":False,"upgradeable":False}

def test_safe_contract_passes():
    d = EVMContractAnalyzer()
    r = d.analyze(safe())
    assert r.passes and r.score == 100

def test_incomplete_evidence_fails_closed():
    r = EVMContractAnalyzer().analyze({})
    assert not r.passes and r.score == 0

def test_dangerous_control_rejects():
    e = safe(); e["selling_enabled"] = False; e["mint_enabled"] = True
    r = EVMContractAnalyzer().analyze(e)
    assert r.status == "REJECT"

def test_selector_is_only_a_hint():
    assert classify_selector("0x40c10f19") == "mint"
    assert classify_selector("0xdeadbeef") is None
