from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Protocol

class EVMSimulationProvider(Protocol):
    async def simulate(self, request: dict[str, Any]) -> dict[str, Any]: ...

@dataclass(frozen=True)
class SimulationResult:
    ok: bool
    reverted: bool
    gas_used: int | None
    return_data: str | None
    reason: str | None = None

class SimulationGateway:
    def __init__(self, provider: EVMSimulationProvider): self.provider = provider
    async def run(self, request: dict[str, Any]) -> SimulationResult:
        raw = await self.provider.simulate(request)
        return SimulationResult(bool(raw.get("ok")), bool(raw.get("reverted")),
                                raw.get("gas_used"), raw.get("return_data"), raw.get("reason"))
