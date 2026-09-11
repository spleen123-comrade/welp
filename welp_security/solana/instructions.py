from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

@dataclass(frozen=True)
class InstructionEvidence:
    program: str
    instruction: str | None
    signers: tuple[str, ...]
    writable_accounts: tuple[str, ...]
    dangerous: bool
    evidence: Mapping[str, Any]

DANGEROUS_HINTS = frozenset({"freeze", "mint", "set_authority", "close_account", "withdraw", "remove_liquidity", "pause", "update_config"})

def inspect_instruction(raw: Mapping[str, Any]) -> InstructionEvidence:
    name = raw.get("instruction")
    dangerous = isinstance(name, str) and name.lower() in DANGEROUS_HINTS
    return InstructionEvidence(str(raw.get("program", "unknown")), name,
                               tuple(map(str, raw.get("signers", ()) or ())),
                               tuple(map(str, raw.get("writable_accounts", ()) or ())), dangerous, raw)
