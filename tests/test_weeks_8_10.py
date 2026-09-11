from welp_security.evm.sellability import EVMSellabilityAnalyzer
from welp_security.evm.deep import EVMDeepAnalyzer
from welp_security.solana.analyzer import SolanaSecurityAnalyzer
from welp_safety.gate import PreBuySafetyGate

def test_evm_sellability_fails_closed():
    r = EVMSellabilityAnalyzer().analyze({"simulation_buy": True, "simulation_sell": False, "simulation_transfer": True, "received_amount_positive": True, "slippage_bps": 20})
    assert r.status == "REJECT"

def test_evm_deep_requires_complete_evidence():
    r = EVMDeepAnalyzer().analyze({})
    assert not r.complete and "bytecode" in r.missing

def test_solana_security_requires_sell():
    r = SolanaSecurityAnalyzer().analyze({"evidence_complete": True, "selling_enabled": True, "simulation_sell": False, "simulation_buy": True})
    assert not r.passes

def test_gate_is_fail_closed():
    r = PreBuySafetyGate().evaluate({"chain":"ethereum", "sellability":True})
    assert not r.allowed

def test_gate_allows_only_all_critical_checks():
    e = {"chain":"ethereum", "sellability":True, "contract_security":True, "liquidity":True, "authority_monitoring":True, "exit_path":True, "fresh_data":True}
    assert PreBuySafetyGate().evaluate(e).allowed
