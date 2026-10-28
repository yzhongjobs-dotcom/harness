"""Optional project-local Codex integration for portable ARIS calls."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path


MANAGED_FILES = (
    (".codex/config.toml", "config.toml"),
    (".codex/hooks.json", "hooks.json"),
    (".codex/agents/paper_reader.toml", "agents/paper_reader.toml"),
    (".codex/agents/coverage_reviewer.toml", "agents/coverage_reviewer.toml"),
    (
        ".codex/agents/independent_problem_reviewer.toml",
        "agents/independent_problem_reviewer.toml",
    ),
    (
        ".codex/agents/independent_novelty_reviewer.toml",
        "agents/independent_novelty_reviewer.toml",
    ),
    (
        ".codex/agents/independent_root_cause_reviewer.toml",
        "agents/independent_root_cause_reviewer.toml",
    ),
    (
        ".codex/agents/independent_method_reviewer.toml",
        "agents/independent_method_reviewer.toml",
    ),
    (
        ".codex/agents/result_to_claim_reviewer.toml",
        "agents/result_to_claim_reviewer.toml",
    ),
    (".codex/hooks/pre_tool_use_policy.py", "hooks/pre_tool_use_policy.py"),
    (".codex/hooks/subagent_attestation.py", "hooks/subagent_attestation.py"),
    (".codex/rules/aris.rules", "rules/aris.rules"),
)

# Optional integration only. ARIS calls never depend on installing or trusting
# these Hooks; the Controller's data and evidence validators remain authoritative.
OPTIONAL_PROJECT_HOOKS = (
    ("PreToolUse", "Checking ARIS Controller boundary"),
    ("SubagentStop", "Recording ARIS subagent provenance"),
    ("Stop", "Recording ARIS subagent provenance"),
)


def _portable_runtime_instruction() -> str:
    return (
        "- ARIS can be called from any working directory using `--root`. "
        "Project-local Codex profiles and Hooks are optional integrations, not "
        "conditions for starting a run or dispatching readers/reviewers. "
        "Do not request Hook trust as a prerequisite for research.\n"
    )


class ProjectRuntimeError(RuntimeError):
    """Compatibility error type; cwd and Hooks are not authorization gates."""


def verify_formal_native_subagent_runtime(
    root: str | Path,
    role: str,
    *,
    runtime_project_root: str | Path | None = None,
) -> dict[str, str]:
    """Describe a portable invocation without requiring project-local Hooks.

    The run root locates state and artifacts; it does not determine the caller's
    working directory. Role contracts can be loaded from the harness checkout
    when the host does not expose project-local custom roles.
    """
    project = Path(root).resolve()
    runtime = Path(runtime_project_root if runtime_project_root is not None else Path.cwd()).resolve()
    repo = Path(__file__).resolve().parents[1]
    return {
        "runtime_project_root": str(runtime),
        "project_root": str(project),
        "role": role,
        "execution_mode": "portable",
        "role_contract_path": str(repo / ".codex" / "agents" / f"{role}.toml"),
    }


def install_project_codex_layer(root: str | Path) -> Path | None:
    """Opt in to local profiles/Hooks without overwriting an unmanaged config."""
    project = Path(root).resolve()
    repo = Path(__file__).resolve().parents[1]
    source_layer = repo / ".codex"
    target_layer = project / ".codex"
    if target_layer.resolve() == source_layer.resolve():
        return None
    manifest = target_layer / "ARIS_CONTROLLER_LAYER.json"
    if (target_layer / "config.toml").exists() and not manifest.exists():
        return None
    records = []
    for source_relative, target_relative in MANAGED_FILES:
        source = repo / source_relative
        target = target_layer / target_relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        records.append(
            {"path": str(Path(".codex") / target_relative), "sha256": digest}
        )
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "source_repo": str(repo),
                "managed_files": records,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    agents = project / "AGENTS.md"
    if not agents.exists():
        agents.write_text(
        "# ARIS formal research project\n\n"
        "- Formal research-lit state changes only through `python -m arisctl`.\n"
        "- Follow the formal workflow implemented in `D:\\桌面\\科研Agent Harness设计\\ARIS`; Controller State and canonical Artifacts are the sole authority for stage transitions and research decisions.\n"
        + _portable_runtime_instruction()
            +
            "- Main performs query planning and Field Map synthesis.\n"
            "- Spawn `paper_reader` and only the reviewer role named by the live Controller request. Keep reader/reviewer work in the current active Codex turn: prefer a configured native role; otherwise use the native generic compatibility path (`fork_turns = none`) for `paper_reader` or `coverage_reviewer`, with the harness role contract and live Controller bindings. Working directory and Hook availability do not restrict this dispatch. Never use nested `codex exec`, a new CLI session, or a new top-level turn to simulate a configured role.\n"
            "- Every scientific-core reviewer performs its Controller-issued judgment directly in its configured Codex CLI role and reports that Codex session's actual model identifier. A reviewer remains independent through its configured role and fresh context; same-family verdicts are accepted by the Controller.\n"
            "- Human Gates require confirmation in the Codex interface.\n",
            encoding="utf-8",
        )
    return manifest
