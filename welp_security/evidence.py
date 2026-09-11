from __future__ import annotations
from dataclasses import dataclass
from typing import Any


REQUIRED_PREBUY_EVM = (
    "selling_enabled", "trading_enabled", "owner", "admin", "upgradeable",
    "mint_enabled", "blacklist_enabled", "fee_changeable", "evidence_complete",
)


@dataclass(frozen=True)
class EvidenceReport:
    complete: bool
    missing: tuple[str, ...]


def check_prebuy_evidence(evidence: dict[str, Any], required: tuple[str, ...] = REQUIRED_PREBUY_EVM) -> EvidenceReport:
    missing = tuple(k for k in required if k not in evidence or evidence[k] is None)
    complete = bool(evidence.get("evidence_complete")) and not missing
    return EvidenceReport(complete, missing)
