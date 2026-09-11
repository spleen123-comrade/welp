from __future__ import annotations
import re

_HEX = re.compile(r"^[0-9a-fA-F]*$")

# EIP-1967 implementation/admin/beacon slots.
EIP1967_SLOTS = frozenset({
    "360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc",
    "b53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103",
    "a3f0ad74e5423aebfd80d3ef4346578335a9a72aeaee4b6d9a9f7f4c3f4f5b0e",
})


def normalize_bytecode(value: str) -> str:
    value = value[2:] if value.startswith("0x") else value
    if len(value) % 2 or not _HEX.fullmatch(value):
        raise ValueError("invalid EVM bytecode hex")
    return value.lower()


def extract_selectors(bytecode: str) -> frozenset[str]:
    """Extract PUSH4 constants as evidence; never treats them as proof of reachability."""
    raw = normalize_bytecode(bytecode)
    return frozenset("0x" + m.group(1) for m in re.finditer(r"63([0-9a-f]{8})", raw))


def eip1967_slots_present(storage: dict[str, str]) -> frozenset[str]:
    keys = {k.lower().removeprefix("0x") for k in storage}
    return frozenset(slot for slot in EIP1967_SLOTS if slot in keys)


def looks_like_eip1967_proxy_storage(storage: dict[str, str]) -> bool:
    """Return true only when a known EIP-1967 slot is actually present."""
    return bool(eip1967_slots_present(storage))
