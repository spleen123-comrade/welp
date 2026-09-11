from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class RawDEXEvent:
    chain: str
    protocol: str
    event_type: str
    tx_id: str
    block_or_slot: int
    log_index: int = 0
    payload: dict[str, Any] | None = None


class DEXAdapter(Protocol):
    chain: str
    protocol: str

    def normalize(self, event: RawDEXEvent) -> dict[str, Any]: ...


class GenericDEXAdapter:
    """Protocol-neutral adapter used until a protocol-specific decoder is configured."""

    def __init__(self, chain: str, protocol: str) -> None:
        self.chain = chain.lower()
        self.protocol = protocol.lower()

    def normalize(self, event: RawDEXEvent) -> dict[str, Any]:
        if event.chain.lower() != self.chain or event.protocol.lower() != self.protocol:
            raise ValueError("event does not belong to adapter")
        return {
            "chain": self.chain,
            "protocol": self.protocol,
            "event_type": event.event_type,
            "tx_id": event.tx_id,
            "block_or_slot": event.block_or_slot,
            "log_index": event.log_index,
            "payload": dict(event.payload or {}),
        }
