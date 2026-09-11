from __future__ import annotations
from dataclasses import dataclass, field
from .models import DEXProtocol

@dataclass
class DEXRegistry:
    protocols: dict[tuple[str, str], DEXProtocol] = field(default_factory=dict)

    def register(self, protocol: DEXProtocol) -> None:
        key = (protocol.chain.lower(), protocol.name.lower())
        self.protocols[key] = protocol

    def get(self, chain: str, name: str) -> DEXProtocol | None:
        return self.protocols.get((chain.lower(), name.lower()))

    def enabled(self, chain: str) -> tuple[DEXProtocol, ...]:
        return tuple(p for (c, _), p in self.protocols.items() if c == chain.lower() and p.enabled)

    @classmethod
    def initial(cls) -> "DEXRegistry":
        r = cls()
        # Addresses/program IDs are intentionally configuration inputs, not guessed constants.
        for chain, names in {
            "ethereum": ("uniswap_v2", "uniswap_v3", "sushi"),
            "bsc": ("pancakeswap_v2", "pancakeswap_v3"),
            "solana": ("raydium", "orca", "meteora", "pumpswap"),
            "robinhood": (),
        }.items():
            for name in names:
                r.register(DEXProtocol(chain, name, "CONFIGURE_ME", "amm"))
        return r
