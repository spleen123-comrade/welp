from __future__ import annotations
from dataclasses import dataclass, field
from .models import TokenCandidate
from .filters import RadarPolicy

@dataclass
class NewTokenRadar:
    policy: RadarPolicy = field(default_factory=RadarPolicy)
    _seen: set[tuple[str, str]] = field(default_factory=set)

    def observe(self, candidate: TokenCandidate) -> TokenCandidate | None:
        key = (candidate.chain.lower(), candidate.token_address.lower())
        if key in self._seen: return None
        if not self.policy.accepts(candidate): return None
        self._seen.add(key)
        return candidate

    def seen(self, chain: str, token_address: str) -> bool:
        return (chain.lower(), token_address.lower()) in self._seen
