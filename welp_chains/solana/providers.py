from __future__ import annotations
from typing import Protocol, AsyncIterator

class SolanaProviderProtocol(Protocol):
    async def health(self) -> bool: ...
    async def latest_slot(self) -> int: ...
    async def get_transaction(self, transaction_id: str) -> dict: ...
    async def stream_events(self) -> AsyncIterator[dict]: ...

class FailoverProvider:
    """Sequential provider failover for the Solana read/streaming foundation."""
    def __init__(self, providers: list[SolanaProviderProtocol]):
        if not providers:
            raise ValueError("at least one provider is required")
        self.providers = list(providers)

    async def health(self) -> bool:
        for provider in self.providers:
            try:
                if await provider.health(): return True
            except Exception: continue
        return False

    async def latest_slot(self) -> int:
        last_error = None
        for provider in self.providers:
            try: return int(await provider.latest_slot())
            except Exception as exc: last_error = exc
        raise RuntimeError("all Solana providers failed") from last_error

    async def get_transaction(self, transaction_id: str) -> dict:
        last_error = None
        for provider in self.providers:
            try: return await provider.get_transaction(transaction_id)
            except Exception as exc: last_error = exc
        raise RuntimeError("all Solana providers failed") from last_error

    async def stream_events(self) -> AsyncIterator[dict]:
        for provider in self.providers:
            try:
                async for event in provider.stream_events(): yield event
                return
            except Exception: continue
        raise RuntimeError("all Solana event streams failed")
