"""Validate repository docs and workflow syntax; optional multi-root workspace audit."""
import argparse
import json
import re
import subprocess
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REPOS = ["architecture", "contracts", "infrastructure", "api-gateway", "estate-service", "spatial-service", "operations-service", "telemetry-service", "analytics-service", "ai-service", "web", "immersive"]
REPOS = ["agrosphere-" + name for name in REPOS]

def check_workflow(file):
    data = yaml.load(file.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    assert isinstance(data, dict) and all(k in data for k in ("name", "on", "jobs")), file
    assert data["permissions"]["contents"] == "read", file
    for job in data["jobs"].values():
        assert "runs-on" in job and job["steps"], file
        for step in job["steps"]:
            assert ("uses" in step) != ("run" in step), file

for file in (ROOT / "docs/architecture").glob("*.puml"):
    source = file.read_text()
    assert source.startswith("@startuml") and source.rstrip().endswith("@enduml"), file
assert len(list((ROOT / "docs/architecture").glob("*.puml"))) == 7
assert len(list((ROOT / "docs/adr").glob("*.md"))) == 13
assert len(list((ROOT / "diagrams/milestone-3a").glob("*.puml"))) == 7
for file in (ROOT / "diagrams/milestone-3a").glob("*.puml"):
    assert file.read_text().startswith("@startuml") and file.read_text().rstrip().endswith("@enduml")
assert len(list((ROOT / "diagrams/milestone-3b").glob("*.puml"))) == 6
for file in (ROOT / "diagrams/milestone-3b").glob("*.puml"):
    source = file.read_text()
    assert source.startswith("@startuml") and source.rstrip().endswith("@enduml"), file
assert "Status: ACCEPTED" in (ROOT / "docs/adr/0013-latex-collection-and-drc.md").read_text(encoding="utf-8")
check_workflow(ROOT / ".github/workflows/ci.yml")
print("PASS: architecture source layout, thirteen ADRs, workflow YAML/structure")

parser = argparse.ArgumentParser()
parser.add_argument("--workspace", type=Path)
args = parser.parse_args()
if args.workspace:
    workspace = args.workspace.resolve()
    assert not (workspace / ".git").exists(), "Parent must not have .git"
    parent_check = subprocess.run(["git", "-C", str(workspace), "rev-parse", "--show-toplevel"], capture_output=True)
    assert parent_check.returncode != 0, "Parent is inside a Git repository"
    for name in REPOS:
        project = workspace / name
        assert (project / ".git").is_dir(), name
        actual = subprocess.check_output(["git", "-C", str(project), "rev-parse", "--show-toplevel"], text=True).strip()
        assert Path(actual).resolve() == project.resolve(), name
        assert not (project / ".gitmodules").exists(), name
        assert not (project / ".git/modules").exists(), name
        # Existing remotes are valid for independent repositories; never mutate connections here.
        for required in ("README.md", "AGENTS.md", ".gitignore", ".gitattributes", "LICENSE.md", "VERSION", "CHANGELOG.md", ".github/workflows/ci.yml"):
            assert (project / required).is_file(), (name, required)
        check_workflow(project / ".github/workflows/ci.yml")
        tracked = subprocess.check_output(["git", "-C", str(project), "ls-files", "--cached", "--others", "--exclude-standard"], text=True).splitlines()
        deleted = set(subprocess.check_output(["git", "-C", str(project), "ls-files", "--deleted"], text=True).splitlines())
        assert not subprocess.check_output(["git", "-C", str(project), "ls-files", "--stage"], text=True).startswith("160000"), name
        for relative in tracked:
            file = project / relative
            # A working-tree rename can leave the old index entry until review/staging.
            # Validate current files without mutating the user's index.
            if not file.exists():
                assert relative in deleted, (name, relative)
                continue
            assert file.name != ".env" and not (file.suffix in {".pem", ".key", ".p12", ".jks"}), file
            assert ".git" not in Path(relative).parts, file
            text = file.read_text(encoding="utf-8", errors="replace")
            assert not re.search(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|AKIA[0-9A-Z]{16}|ghp_[a-zA-Z0-9]{36}", text), file
            if file.suffix in {".yml", ".yaml"}:
                yaml.load(text, Loader=yaml.BaseLoader)
        for relative in (".env", "target/probe", "node_modules/probe", ".venv/probe"):
            assert subprocess.run(["git", "-C", str(project), "check-ignore", "--quiet", relative]).returncode == 0, (name, relative)
    data = json.loads((workspace / "AgroSphere.code-workspace").read_text())
    assert {x["path"] for x in data["folders"]} == set(REPOS)
    print("PASS: 12 distinct Git roots, no parent Git, no submodules; existing remotes preserved, standards, all workflow/YAML syntax, secret-pattern/ignore checks, workspace folders")
    print("Secret scan is heuristic; this validator performs no commits, pushes or remote mutations.")
