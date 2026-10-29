from pathlib import Path
import pytest
from arisctl.controller import ControllerError
from tests.test_aris_controller import start_controller, metadata, card


def corpus(tmp_path: Path):
    ctl = start_controller(tmp_path, native_layer=False)
    unknown = {**metadata("U1"), "title": "Unverified record", "identity_status": "verify_pending", "abstract": None, "doi_or_stable_url": "https://example.org/unknown"}
    ctl.execute_query("test field", "fixture", lambda _: [metadata(), unknown], plan_item_id="QP-1", query_options={"year_from": 2000, "year_to": 2026, "exact_title": False, "page": 1})
    ctl.enrich_candidate_metadata("U1", identity_verifier=lambda _: {"identity_status": "verify_failed", "identity_reason": "no exact title match"})
    return ctl


def hold(ctl, paper="U1", **changes):
    args = dict(screening_in_scope=True, screening_basis="IDENTITY_UNRESOLVED", screening_reason="Identity remains unresolved; no scientific inclusion or exclusion is claimed.", reading_priority="TARGETED_GAP_FOLLOWUP", fulltext_selected=False, fulltext_selection_reason="Pending identity is not evidence.")
    args.update(changes)
    return ctl.decide_admission(paper, **args)


def test_identity_hold_allows_verified_reading_without_admitting_unknown(tmp_path):
    ctl = corpus(tmp_path)
    assert hold(ctl) == "HOLD_IDENTITY"
    ctl.decide_admission("P1", screening_in_scope=True, screening_basis="TITLE_ABSTRACT", screening_reason="Verified relevant mechanism", reading_priority="RECENT_ELITE_FRONTIER")
    with pytest.raises(ControllerError, match="excluded, duplicate, or out of scope"):
        ctl.select_reading_subset(["U1"], rationale="cannot read identity hold", initial=True)
    ctl.select_reading_subset(["P1"], rationale="Verified initial source; unresolved identity is retained separately.", initial=True)
    ctl.finish_retrieval()
    with pytest.raises(ControllerError, match="outside the active readable subset"):
        ctl.read_full_text("U1", "fixture", lambda _: "must not be read")
    read = ctl.read_full_text("P1", "fixture", lambda _: "full paper")
    ctl.submit_evidence_card("P1", card(read))
    state = ctl.status()["research_lit"]
    assert state["papers"]["U1"]["identity_status"] == "verify_failed"
    assert "evidence:U1" not in state["accepted_artifacts"]


@pytest.mark.parametrize("changes", [{"fulltext_selected": True}, {"screening_in_scope": False}, {"duplicate": True}])
def test_identity_hold_cannot_be_used_as_selection_or_false_exclusion(tmp_path, changes):
    ctl = corpus(tmp_path)
    with pytest.raises(ControllerError, match="identity hold requires"):
        hold(ctl, **changes)


def test_verified_identity_cannot_be_hidden_as_an_identity_hold(tmp_path):
    ctl = corpus(tmp_path)
    with pytest.raises(ControllerError, match="identity hold requires"):
        hold(ctl, paper="P1")


def test_scholar_zero_hit_payload_is_a_completed_empty_search():
    from arisctl.gateways import serpapi_google_scholar_search, ScholarQueryOptions
    result = serpapi_google_scholar_search("exact missing title", ScholarQueryOptions(), api_key="fixture", fetch_json=lambda *a, **k: {"error": "Google hasn't returned any results for this query."})
    assert result == []


def test_failed_query_retry_retains_failure_and_consumes_new_budget(tmp_path):
    ctl = start_controller(tmp_path, native_layer=False)
    options = {"year_from": 2000, "year_to": 2026, "exact_title": False, "page": 1}
    def fail(_):
        raise ValueError("query failed")
    with pytest.raises(ValueError):
        ctl.execute_query("test field", "fixture", fail, plan_item_id="QP-1", query_options=options)
    before = ctl.status()["research_lit"]
    assert before["query_count"] == 1
    ctl.retry_failed_query("test field", reason="One corrected adapter attempt; keep prior failure.")
    ctl.execute_query("test field", "fixture", lambda _: [], plan_item_id="QP-1", query_options=options)
    after = ctl.status()["research_lit"]
    assert after["query_count"] == 2
    assert sorted(e["status"] for e in after["query_events"].values()) == ["complete", "failed"]
