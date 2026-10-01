from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def test_identity_audit_passes():
    r=subprocess.run([sys.executable,str(ROOT/"scripts/cbuild800_identity_audit.py")],cwd=ROOT,text=True,capture_output=True)
    assert r.returncode==0,r.stdout+r.stderr
def test_cumulative_audit_preserves_predecessor():
    r=subprocess.run([sys.executable,str(ROOT/"scripts/cbuild800_cumulative_audit.py")],cwd=ROOT,text=True,capture_output=True)
    assert r.returncode==0,r.stdout+r.stderr
    report=json.loads((ROOT/"CBUILD800_CUMULATIVE_AUDIT.json").read_text())
    assert report["status"]=="PASS"
    assert report["unexpected_deleted_paths"]==[]
    assert report["mutated_predecessor_paths"]==[]
    assert report["historical_tree_preserved"] is True
def test_execution_boundary_locked():
    meta=json.loads((ROOT/"cbuild_metadata/build_identity_cbuild800.json").read_text())
    assert meta["signing"]=="LOCKED" and meta["broadcast"]=="LOCKED"
def test_c799_identity_untouched():
    assert (ROOT/"CBUILD799_BUILD_ID.txt").read_text().strip()=="cbuild-799"
