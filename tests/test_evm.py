import asyncio
from datetime import datetime, timezone
import pytest
from welp_chains.evm.adapter import EVMAdapter
from welp_chains.evm.providers import FailoverProvider

class FakeProvider:
    def __init__(self, healthy=True, height=100):
        self._healthy, self._height = healthy, height
    async def health(self): return self._healthy
    async def latest_block(self):
        if not self._healthy: raise RuntimeError("down")
        return self._height
    async def get_transaction(self, tx):
        if not self._healthy: raise RuntimeError("down")
        return {"hash": tx}
    async def stream_events(self):
        yield {"event_type":"block","event_id":"eth:100","source":"fake","block_number":100,"transaction_id":"0xabc","observed_at":datetime.now(timezone.utc),"payload":{"ok":True}}

def test_event_normalization():
    async def run():
        event = await anext(EVMAdapter("ethereum", 1, FakeProvider()).stream_events())
        assert event.chain.name == "ethereum"
        assert event.block_or_slot == 100
        assert event.transaction_id == "0xabc"
    asyncio.run(run())

def test_failover():
    async def run():
        provider = FailoverProvider([FakeProvider(False), FakeProvider(True, 123)])
        assert await provider.health() is True
        assert await provider.latest_block() == 123
        assert await provider.get_transaction("0x1") == {"hash":"0x1"}
    asyncio.run(run())

def test_missing_event_field_rejected():
    adapter = EVMAdapter("ethereum", 1, FakeProvider())
    with pytest.raises(Exception):
        adapter.normalize_event({"event_type":"block","source":"fake"})
