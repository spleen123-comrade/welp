#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,zipfile
ROOT=Path(__file__).resolve().parents[1]
PREVIOUS_ZIP=Path("/mnt/data/Welp_cbuild-799_COMPLETE_CUMULATIVE_FLAT.zip")
BUILD="cbuild-800"; PARENT="cbuild-799"
GENERATED={"CBUILD800_CUMULATIVE_AUDIT.json","CBUILD800_BUILD_IDENTITY_AUDIT.json","CBUILD800_CUMULATIVE_MANIFEST.json","Welp_cbuild-800_MANIFEST.json","Welp_cbuild-800_SOURCE_TREE_SHA256.txt","release/CBUILD-800_BC_RELEASE_RECORD.json"}
EXCLUDE_DIRS={".git","__pycache__", ".pytest_cache",".venv",".streamlit-venv","node_modules"}
def tree_inventory(root=ROOT):
    out={}
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix==".pyc" or any(x in EXCLUDE_DIRS for x in p.parts): continue
        r=p.relative_to(root).as_posix()
        if r in GENERATED: continue
        out[r]=hashlib.sha256(p.read_bytes()).hexdigest()
    return out
def zip_inventory(path):
    with zipfile.ZipFile(path) as z:
        return {n:hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if not n.endswith("/") and not n.endswith(".pyc") and "/__pycache__/" not in n and "/.pytest_cache/" not in n and not n.startswith(".pytest_cache/")}
def source_sha(items):
    h=hashlib.sha256()
    for rel,digest in sorted(items.items()):
        h.update(rel.encode()); h.update(b"\0"); h.update(digest.encode()); h.update(b"\n")
    return h.hexdigest()
def secret_scan(items):
    patterns=[re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----"),re.compile(r"\b(?:mnemonic|seed_phrase|private_key)\s*[:=]\s*['\"][^'\"]{20,}",re.I)]
    hits=[]
    for rel in items:
        p=ROOT/rel
        if p.suffix not in {".py",".md",".txt",".json",".toml",".yaml",".yml",".sh"} or p.stat().st_size>2_000_000: continue
        t=p.read_text(encoding="utf-8",errors="ignore")
        if rel=="tests/test_cbuild729_external_signer.py": continue
        if any(rx.search(t) for rx in patterns): hits.append(rel)
    return {"passed":not hits,"hits":sorted(set(hits))}
current=tree_inventory(); previous=zip_inventory(PREVIOUS_ZIP)
deleted=sorted(set(previous)-set(current)); mutated=sorted(k for k in set(previous)&set(current) if previous[k]!=current[k]); new=sorted(set(current)-set(previous))
sec=secret_scan(current); sha=source_sha(current)
report={"build":BUILD,"predecessor":PARENT,"current_file_count":len(current),"predecessor_archive_entry_count":len(previous),"unexpected_deleted_paths":deleted,"mutated_predecessor_paths":mutated,"new_paths":new,"source_tree_sha256":sha,"secret_scan":sec,"historical_tree_preserved":not deleted and not mutated,"signing_enabled":False,"broadcast_enabled":False,"status":"PASS" if not deleted and not mutated and sec["passed"] else "FAIL"}
(ROOT/"CBUILD800_CUMULATIVE_AUDIT.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2,sort_keys=True))
raise SystemExit(0 if report["status"]=="PASS" else 1)
