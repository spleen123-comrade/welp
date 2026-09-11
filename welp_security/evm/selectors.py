"""Common EVM control-function selectors used as hints, not proof.

The security engine must combine selector evidence with target, caller, decoded
arguments and resulting state. A selector alone never triggers a trade exit.
"""
CONTROL_HINTS = {
    "0x715018a6": "renounceOwnership",
    "0xf2fde38b": "transferOwnership",
    "0x8456cb59": "pause",
    "0x3f4ba83a": "unpause",
    "0x40c10f19": "mint",
    "0x42966c68": "burn",
    "0x06fdde03": "name",
    "0x8da5cb5b": "owner",
    "0x5c975abb": "paused",
}

def classify_selector(selector: str) -> str | None:
    return CONTROL_HINTS.get(selector.lower())
