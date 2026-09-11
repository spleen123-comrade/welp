from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import AsyncIterator

from welp_core.errors import ProviderError
from welp_core.models import ChainRef, NormalizedEvent
from .providers import EVMProviderProtocol

@dataclass
class EVMAdapter:
    chain_name: str
    chain_id: int
    provider: EVMProviderProtocol

    async def health(self) -> bool:
        try:
            return bool(await self.provider.health())
        except Exception as exc:
            raise ProviderError(f"{self.chain_name} provider health failed") from exc

    async def latest_height(self) -> int:
        try:
            return int(await self.provider.latest_block())
        except Exception as exc:
            raise ProviderError(f"{self.chain_name} latest block failed") from exc

    async def get_transaction(self, transaction_id: str) -> dict:
        try:
            return await self.provider.get_transaction(transaction_id)
        except Exception as exc:
            raise ProviderError(f"{self.chain_name} transaction lookup failed") from exc

    async def stream_events(self) -> AsyncIterator[NormalizedEvent]:
        async for raw in self.provider.stream_events():
            yield self.normalize_event(raw)

    def normalize_event(self, raw: dict) -> NormalizedEvent:
        required = ("event_type", "event_id", "source")
        missing = [key for key in required if not raw.get(key)]
        if missing:
            raise ProviderError(f"invalid EVM event; missing {missing}")
        return NormalizedEvent(
            chain=ChainRef(self.chain_name, self.chain_id),
            event_type=str(raw["event_type"]),
            event_id=str(raw["event_id"]),
            observed_at=raw.get("observed_at") or datetime.now(timezone.utc),
            source=str(raw["source"]),
            block_or_slot=raw.get("block_number"),
            transaction_id=raw.get("transaction_id"),
            payload=raw.get("payload", {}),
        )
