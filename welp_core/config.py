from __future__ import annotations
from dataclasses import dataclass
import os
from .errors import ConfigurationError

@dataclass(frozen=True)
class AppConfig:
    environment: str = "development"
    live_trading_enabled: bool = False
    request_timeout_seconds: float = 5.0

    @classmethod
    def from_env(cls) -> "AppConfig":
        raw = os.getenv("WELP_LIVE_TRADING", "false").strip().lower()
        if raw not in {"true", "false", "1", "0"}:
            raise ConfigurationError("WELP_LIVE_TRADING must be true/false/1/0")
        timeout = float(os.getenv("WELP_REQUEST_TIMEOUT_SECONDS", "5"))
        if not 0 < timeout <= 60:
            raise ConfigurationError("request timeout must be >0 and <=60 seconds")
        return cls(os.getenv("WELP_ENV", "development"), raw in {"true", "1"}, timeout)

INITIAL_CHAINS = ("ethereum", "bsc", "robinhood", "solana")
