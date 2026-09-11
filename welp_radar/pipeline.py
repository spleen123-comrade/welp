from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable
from .models import TokenCandidate
from .detector import NewTokenRadar


@dataclass
class RadarPipeline:
    radar: NewTokenRadar
    accepted: list[TokenCandidate] = field(default_factory=list)
    rejected: int = 0

    def ingest(self, candidates: Iterable[TokenCandidate]) -> list[TokenCandidate]:
        out: list[TokenCandidate] = []
        for candidate in candidates:
            result = self.radar.observe(candidate)
            if result is None:
                self.rejected += 1
                continue
            self.accepted.append(result)
            out.append(result)
        return out
