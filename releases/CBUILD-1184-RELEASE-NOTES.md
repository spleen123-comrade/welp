# Welp CBUILD-1184 — local Streamlit entrypoint repair

The CBUILD-1183 archive showed that `welp_ui/app.py` put an import before its module docstring. Streamlit therefore rendered the legacy CBUILD-561 description as page content instead of treating it as a module docstring.

The fix moves the descriptive docstring immediately after `from __future__ import annotations`, then keeps the CBUILD-723 compatibility import below it. The local `main()` defined later in `welp_ui/app.py` remains the entrypoint invoked when Streamlit runs that file.

The cumulative source archive is delivered separately as `Welp_cbuild-1184.tar.zst`. This repository's current `main` branch is still the original foundation scaffold and does not contain the full CBUILD-1183 source tree; this branch records the exact patch but does not claim that the whole application has been synced or deployed from this repository.

Safety unchanged: Gate 2 deferred; signing and broadcast disabled; strict source-event timestamp provenance and the <1.0s freshness rule unchanged.
