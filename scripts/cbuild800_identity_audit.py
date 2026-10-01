#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
BUILD="cbuild-800"; PARENT="cbuild-799"; MILESTONE="B_C_BUILD_IDENTITY_AND_CUMULATIVE_INTEGRITY"
checks={}
checks["build_id"]=(ROOT/"CBUILD800_BUILD_ID.txt").read_text().strip()==BUILD
meta=json.loads((ROOT/"cbuild_metadata/build_identity_cbuild800.json").read_text())
checks["metadata"]=meta["build"]==BUILD and meta["parent"]==PARENT and meta["milestone"]==MILESTONE
scope=(ROOT/"docs/milestones/CBUILD-800_BC_SCOPE.md").read_text()
release=(ROOT/"CBUILD800_RELEASE_NOTES.md").read_text()
checks["scope_identity"]=BUILD in scope and PARENT in scope and MILESTONE in scope
checks["release_identity"]=BUILD in release and PARENT in release and MILESTONE in release
checks["historical_identity_preserved"]=(ROOT/"CBUILD799_BUILD_ID.txt").read_text().strip()==PARENT
checks["signing_locked"]=meta["signing"]=="LOCKED" and "Signing remains LOCKED" in release
checks["broadcast_locked"]=meta["broadcast"]=="LOCKED" and "Broadcast remains LOCKED" in release
report={"build":BUILD,"parent":PARENT,"milestone":MILESTONE,"checks":checks,"passed":all(checks.values()),"signing_enabled":False,"broadcast_enabled":False}
(ROOT/"CBUILD800_BUILD_IDENTITY_AUDIT.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2,sort_keys=True))
raise SystemExit(0 if report["passed"] else 1)
