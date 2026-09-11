# Welp Normalized Event Model

Adapters convert source observations into a normalized envelope while preserving protocol-specific data.

Required fields:
- chain
- event_type
- event_id
- observed_at
- source
- block_or_slot
- transaction_id
- payload

`event_id` is used for downstream deduplication. Raw source details remain in `payload`.
