#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
checks={
 "build_id":(ROOT/"CBUILD802_BUILD_ID.txt").read_text().strip()=="cbuild-802",
 "scope":all(x in (ROOT/"docs/milestones/CBUILD-802_FG_SCOPE.md").read_text() for x in ["CBUILD-801","Reproducible Verification","Release Governance"]),
 "verification":json.loads((ROOT/"docs/milestones/CBUILD-802_FG_VERIFICATION.json").read_text())["status"]=="PASS",
 "release":json.loads((ROOT/"release/CBUILD-802_FG_RELEASE_RECORD.json").read_text())["verification"]=="PASS",
 "baseline":json.loads((ROOT/"docs/milestones/CBUILD-802_FG_BASELINE_LOCK.json").read_text())["status"]=="PROTECTED_BASELINE",
 "signing_locked":json.loads((ROOT/"docs/milestones/CBUILD-802_FG_VERIFICATION.json").read_text())["signing"]=="LOCKED",
 "broadcast_locked":json.loads((ROOT/"docs/milestones/CBUILD-802_FG_VERIFICATION.json").read_text())["broadcast"]=="LOCKED",
}
report={"build":"cbuild-802","parent":"cbuild-801","milestone":"F_G_REPRODUCIBLE_VERIFICATION_AND_RELEASE_GOVERNANCE","checks":checks,"passed":all(checks.values())}
(ROOT/"CBUILD802_FG_AUDIT.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2,sort_keys=True))
raise SystemExit(0 if report["passed"] else 1)
