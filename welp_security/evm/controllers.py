from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

@dataclass(frozen=True)
class ControllerReport:
    authorities: Mapping[str, str | None]
    upgradeable: bool | None
    complete: bool
    missing: tuple[str, ...]

class EVMControllerDiscovery:
    REQUIRED = ("owner", "admin", "proxy_admin", "upgradeable")
    def analyze(self, evidence: Mapping[str, Any]) -> ControllerReport:
        missing = tuple(k for k in self.REQUIRED if k not in evidence)
        authorities = {k: evidence.get(k) for k in ("owner", "admin", "proxy_admin")}
        return ControllerReport(authorities, evidence.get("upgradeable"), not missing and bool(evidence.get("evidence_complete")), missing)
