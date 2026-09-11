from __future__ import annotations
import re

_HEX = re.compile(r"^[0-9a-fA-F]*$")


def normalize_bytecode(value: str) -> str:
    value = value[2:] if value.startswith("0x") else value
    if len(value) % 2 or not _HEX.fullmatch(value):
        raise ValueError("invalid EVM bytecode hex")
    return value.lower()


def extract_selectors(bytecode: str) -> frozenset[str]:
    """Extract PUSH4 constants as evidence; never treats them as proof of reachability."""
    raw = normalize_bytecode(bytecode)
    selectors = set()
    for match in re.finditer(r"63([0-9a-f]{8})", raw):
        selectors.add("0x" + match.group(1))
    return frozenset(selectors)


def looks_like_eip1967_proxy_storage(storage: dict[str, str]) -> bool:
    keys = {k.lower().removeprefix("0x") for k in storage}
    return any(len(k) == 64 for k in keys)
