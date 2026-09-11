from dataclasses import dataclass

@dataclass(frozen=True)
class EVMNetwork:
    name: str
    chain_id: int | None
    enabled: bool = False

ETHEREUM = EVMNetwork("ethereum", 1)
BSC = EVMNetwork("bsc", 56)
# Robinhood Chain is deliberately left without a hard-coded ID until its
# production integration is verified against authoritative chain metadata.
ROBINHOOD = EVMNetwork("robinhood", None)

INITIAL_EVM_NETWORKS = (ETHEREUM, BSC, ROBINHOOD)
