from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ControlFinding:
    name: str
    dangerous: bool
    authority: str | None
    evidence: str


CONTROL_KEYS = (
    "selling_enabled", "trading_enabled", "mint_enabled", "blacklist_enabled",
    "whitelist_enabled", "fee_changeable", "max_tx_changeable", "max_wallet_changeable",
    "upgradeable",
)


def evaluate_controls(evidence: dict[str, Any]) -> tuple[ControlFinding, ...]:
    """Turn explicit state/control evidence into findings without guessing missing data."""
    findings: list[ControlFinding] = []
    for key in CONTROL_KEYS:
        value = evidence.get(key)
        authority = evidence.get(f"{key}_authority") or evidence.get("admin") or evidence.get("owner")
        if value is True:
            findings.append(ControlFinding(key, True, authority, "explicitly reported as changeable/enabled"))
        elif value is False:
            findings.append(ControlFinding(key, False, authority, "explicitly reported as not changeable/disabled"))
        else:
            findings.append(ControlFinding(key, True, authority, "unknown state; must be treated as unsafe"))
    return tuple(findings)
