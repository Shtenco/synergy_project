from datetime import datetime, timedelta, timezone
from uuid import UUID
import importlib.util
from pathlib import Path
import pytest

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"contracts"/"capital_governance_v1.py"
spec=importlib.util.spec_from_file_location("capital_governance_v1",PATH)
mod=importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(mod)


def test_project_proposal_cannot_self_authorize():
    with pytest.raises(ValueError):
        mod.validate_project_proposal({
            "project_id":"KZ-1","capital_required":"100","currency":"USD",
            "authorization_status":"AUTHORIZED"
        })


def test_funding_authorization_requires_approver_and_evidence():
    with pytest.raises(ValueError):
        mod.funding_authorization_payload(
            project_event_id=UUID("11111111-1111-4111-8111-111111111111"),
            authorization_id=UUID("22222222-2222-4222-8222-222222222222"),
            decision="AUTHORIZE",max_amount="100",currency="USD",
            authorized_rails=["bank"],expires_at=datetime.now(timezone.utc)+timedelta(hours=1),
            conditions=[],approver_refs=[],underwriting_evidence_ids=[],policy_version="gov-v1"
        )


def test_funding_authorization_is_explicit_and_bounded():
    p=mod.funding_authorization_payload(
        project_event_id=UUID("11111111-1111-4111-8111-111111111111"),
        authorization_id=UUID("22222222-2222-4222-8222-222222222222"),
        decision="AUTHORIZE",max_amount="100",currency="USD",
        authorized_rails=["bank"],expires_at=datetime.now(timezone.utc)+timedelta(hours=1),
        conditions=["M1 evidence complete"],approver_refs=["committee:1"],
        underwriting_evidence_ids=["urn:synergy:evidence:synergy_project:underwriting:sha256:"+"1"*64],
        policy_version="gov-v1"
    )
    assert p["decision"]=="AUTHORIZE"
    assert p["max_amount"]=="100"
