from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test_identity_and_parent():
    assert (ROOT/"CBUILD802_BUILD_ID.txt").read_text().strip()=="cbuild-802"
    scope=(ROOT/"docs/milestones/CBUILD-802_FG_SCOPE.md").read_text()
    assert "CBUILD-801" in scope and "F — Reproducible Verification" in scope and "G — Release Governance" in scope

def test_verification_passes():
    r=json.loads((ROOT/"docs/milestones/CBUILD-802_FG_VERIFICATION.json").read_text())
    assert r["status"]=="PASS"
    assert r["f"]=="CLOSED" and r["g"]=="CLOSED"
    assert r["c801_predecessor_deletions"]==0
    assert r["c801_predecessor_mutations"]==0

def test_execution_boundary():
    r=json.loads((ROOT/"docs/milestones/CBUILD-802_FG_VERIFICATION.json").read_text())
    assert r["signing"]=="LOCKED" and r["broadcast"]=="LOCKED"
    assert r["live_gates_3_to_7"]=="UNCHANGED_NOT_PROMOTED"

def test_release_and_lock_records():
    release=json.loads((ROOT/"release/CBUILD-802_FG_RELEASE_RECORD.json").read_text())
    lock=json.loads((ROOT/"docs/milestones/CBUILD-802_FG_BASELINE_LOCK.json").read_text())
    assert release["verification"]=="PASS"
    assert lock["status"]=="PROTECTED_BASELINE"
