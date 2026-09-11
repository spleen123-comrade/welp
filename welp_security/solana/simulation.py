from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Protocol

class SolanaSimulationProvider(Protocol):
    async def simulate(self, transaction: Any) -> dict[str, Any]: ...

@dataclass(frozen=True)
class SolanaSimulationResult:
    ok: bool
    err: Any = None
    logs: tuple[str, ...] = ()

class SolanaSimulationGateway:
    def __init__(self, provider: SolanaSimulationProvider): self.provider = provider
    async def run(self, transaction: Any) -> SolanaSimulationResult:
        raw = await self.provider.simulate(transaction)
        return SolanaSimulationResult(bool(raw.get("ok")), raw.get("err"), tuple(raw.get("logs", ()) or ()))
