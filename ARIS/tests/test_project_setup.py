from __future__ import annotations

import json
from pathlib import Path

import pytest

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 support
    import tomli as tomllib

from arisctl.project_setup import (
    OPTIONAL_PROJECT_HOOKS,
    install_project_codex_layer,
    verify_formal_native_subagent_runtime,
)


REVIEWER_ROLES = {
    "independent_problem_reviewer",
    "independent_novelty_reviewer",
    "independent_root_cause_reviewer",
    "independent_method_reviewer",
}


def test_project_layer_installs_every_declared_agent_without_gemini_bridge(
    tmp_path: Path,
) -> None:
    manifest_path = install_project_codex_layer(tmp_path)
    assert manifest_path is not None

    config = tomllib.loads(
        (tmp_path / ".codex" / "config.toml").read_text(encoding="utf-8")
    )
    declared = {
        role
        for role, definition in config["agents"].items()
        if isinstance(definition, dict)
    }
    assert REVIEWER_ROLES <= declared
    for role, definition in config["agents"].items():
        if not isinstance(definition, dict):
            continue
        assert (tmp_path / ".codex" / definition["config_file"]).is_file(), role

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    managed = {record["path"].replace("\\", "/") for record in manifest["managed_files"]}
    assert "gemini-review" not in str(config)
    assert not any("gemini-review" in path for path in managed)
    assert all(f".codex/agents/{role}.toml" in managed for role in REVIEWER_ROLES)

    agents_md = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    assert "reviewer role named by the live Controller request" in agents_md
    assert "any working directory" in agents_md
    assert "Hooks are optional integrations" in agents_md
    assert "native generic compatibility path" in agents_md
    assert "nested `codex exec`" in agents_md
    assert "Every scientific-core reviewer" in agents_md
    assert "configured Codex CLI role" in agents_md
    assert "same-family verdicts are accepted" in agents_md
    assert "Do not request Hook trust as a prerequisite" in agents_md
    assert "`/hooks` trust action" not in agents_md
    rules = (tmp_path / ".codex" / "rules" / "aris.rules").read_text(encoding="utf-8")
    assert "ARIS calls are portable" in rules

    hook_config = json.loads((tmp_path / ".codex" / "hooks.json").read_text(encoding="utf-8"))
    installed_hooks = {
        (event, str(entry.get("statusMessage") or ""))
        for event, groups in hook_config["hooks"].items()
        for group in groups
        for entry in group.get("hooks", [])
        if isinstance(entry, dict) and entry.get("type") == "command"
    }
    assert installed_hooks == set(OPTIONAL_PROJECT_HOOKS)

def test_formal_native_runtime_is_portable_without_project_layer(tmp_path: Path) -> None:
    project = tmp_path / "run"
    caller = tmp_path / "other-project"
    project.mkdir()
    caller.mkdir()
    passed = verify_formal_native_subagent_runtime(
        project, "paper_reader", runtime_project_root=caller,
    )
    assert passed["runtime_project_root"] == str(caller.resolve())
    assert passed["project_root"] == str(project.resolve())
    assert passed["role"] == "paper_reader"
    assert passed["execution_mode"] == "portable"
    assert Path(passed["role_contract_path"]).is_file()
    assert not (project / ".codex").exists()


def test_optional_layer_does_not_overwrite_unmanaged_codex_config(tmp_path: Path) -> None:
    config = tmp_path / ".codex" / "config.toml"
    config.parent.mkdir()
    original = b'model = "user-selected-model"\n'
    config.write_bytes(original)
    assert install_project_codex_layer(tmp_path) is None
    assert config.read_bytes() == original
    assert not (config.parent / "hooks.json").exists()


def test_every_scientific_core_reviewer_uses_direct_codex_cli() -> None:
    repo = Path(__file__).resolve().parents[1]
    for role in REVIEWER_ROLES:
        text = (repo / ".codex" / "agents" / f"{role}.toml").read_text(
            encoding="utf-8"
        )
        assert "directly in this Codex CLI session" in text
        assert "mcp__gemini-review__review_start" not in text
        assert "mcp__gemini-review__review_status" not in text
        assert "exact model identifier" in text


def test_method_reviewer_can_read_bound_artifacts_without_mutation_authority() -> None:
    repo = Path(__file__).resolve().parents[1]
    config = tomllib.loads(
        (repo / ".codex" / "agents" / "independent_method_reviewer.toml").read_text(
            encoding="utf-8"
        )
    )

    assert config["sandbox_mode"] == "read-only"
    assert config["approval_policy"] == "never"
    assert config["features"]["shell_tool"] is True
    assert config["tools"]["web_search"] is False

    instructions = config["developer_instructions"]
    assert "list bound paths" in instructions
    assert "read their original contents" in instructions
    assert "search within those files" in instructions
    assert "compute or verify their hashes" in instructions
    assert "Do not use inline handoff text as a substitute" in instructions
    assert "Do not create, edit, delete, rename, copy" in instructions
    assert "do not run `arisctl` or any Controller/Gate command" in instructions
    assert "`reviewed_artifact` must be a JSON object with exactly `path` and `sha256`" in instructions
    assert "never return a path string there" in instructions


@pytest.mark.parametrize(
    "role",
    ("independent_problem_reviewer", "independent_novelty_reviewer"),
)
def test_candidate_reviewers_require_validator_binding_fields(role: str) -> None:
    repo = Path(__file__).resolve().parents[1]
    text = (repo / ".codex" / "agents" / f"{role}.toml").read_text(encoding="utf-8")
    assert "Every record must copy" in text
    for field in (
        "schema_version",
        "review_request_id",
        "reviewer",
        "verdict_id",
        "reviewed_artifact_hashes",
    ):
        assert field in text
    assert "one phase-level `verdict_id`" in text
    assert "candidate-specific verdict IDs are invalid" in text
