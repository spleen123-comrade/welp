import pytest
from decimal import Decimal
from welp_core.config import AppConfig, INITIAL_CHAINS
from welp_core.models import RiskBudget

def test_initial_chains():
    assert INITIAL_CHAINS == ("ethereum", "bsc", "robinhood", "solana")

def test_live_trading_defaults_off(monkeypatch):
    monkeypatch.delenv("WELP_LIVE_TRADING", raising=False)
    assert AppConfig.from_env().live_trading_enabled is False

def test_invalid_live_flag(monkeypatch):
    monkeypatch.setenv("WELP_LIVE_TRADING", "maybe")
    with pytest.raises(Exception):
        AppConfig.from_env()

def test_risk_budget_validation():
    RiskBudget("percent_balance", Decimal("0.5"), Decimal("10000")).validate()
    RiskBudget("fixed_usd", Decimal("50")).validate()
    with pytest.raises(ValueError):
        RiskBudget("percent_balance", Decimal("0")).validate()
