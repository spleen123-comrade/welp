import asyncio
from datetime import datetime, timezone
import pytest
from welp_chains.solana.adapter import SolanaAdapter
from welp_chains.solana.providers import FailoverProvider

class FakeProvider:
    def __init__(self, healthy=True, slot=200): self.healthy, self.slot = healthy, slot
    async def health(self): return self.healthy
    async def latest_slot(self):
        if not self.healthy: raise RuntimeError("down")
        return self.slot
    async def get_transaction(self, tx):
        if not self.healthy: raise RuntimeError("down")
        return {"signature": tx}
    async def stream_events(self):
        yield {"event_type":"instruction","event_id":"sol:200:0","source":"fake","slot":200,"transaction_id":"sig123","observed_at":datetime.now(timezone.utc),"payload":{"program":"program1","signers":["signer1"],"writable_accounts":["acct1"]}}

def test_instruction_context_is_preserved():
    async def run():
        event = await anext(SolanaAdapter(FakeProvider()).stream_events())
        assert event.chain.name == "solana"
        assert event.block_or_slot == 200
        assert event.payload["program"] == "program1"
        assert event.payload["writable_accounts"] == ["acct1"]
    asyncio.run(run())

def test_failover():
    async def run():
        provider = FailoverProvider([FakeProvider(False), FakeProvider(True, 321)])
        assert await provider.health() is True
        assert await provider.latest_slot() == 321
        assert await provider.get_transaction("sig") == {"signature":"sig"}
    asyncio.run(run())

def test_missing_event_field_rejected():
    adapter = SolanaAdapter(FakeProvider())
    with pytest.raises(Exception): adapter.normalize_event({"event_type":"instruction","source":"fake"})
