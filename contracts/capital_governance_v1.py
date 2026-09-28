from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import Any
from uuid import UUID


PROJECT_CONTRACT_ID = "synergy.economy.project-proposal/v1"
AUTH_CONTRACT_ID = "synergy.economy.funding-authorization/v1"
AUTHORITY = "capital_governance"


def validate_project_proposal(payload: dict[str, Any]) -> None:
    if not payload.get("project_id"):
        raise ValueError("project_id required")
    capital=Decimal(str(payload.get("capital_required","0")))
    if capital <= 0:
        raise ValueError("capital_required must be positive")
    if not payload.get("currency"):
        raise ValueError("currency required")
    status=str(payload.get("authorization_status",""))
    if status not in {"PROPOSED","UNDER_REVIEW","AUTHORIZED","REJECTED"}:
        raise ValueError("unknown proposal authorization status")
    if status=="AUTHORIZED":
        raise ValueError("ProjectProposal cannot self-authorize funding")


def funding_authorization_payload(
    *,
    project_event_id: UUID | str,
    authorization_id: UUID | str,
    decision: str,
    max_amount: Decimal | str,
    currency: str,
    authorized_rails: list[str],
    expires_at: datetime,
    conditions: list[str],
    approver_refs: list[str],
    underwriting_evidence_ids: list[str],
    policy_version: str,
) -> dict[str, Any]:
    d=decision.upper()
    if d not in {"AUTHORIZE","REJECT","DEFER"}:
        raise ValueError("invalid funding decision")
    amount=Decimal(str(max_amount))
    if amount < 0:
        raise ValueError("max_amount cannot be negative")
    if expires_at <= datetime.now(timezone.utc):
        raise ValueError("authorization must expire in the future")
    if d=="AUTHORIZE":
        if amount <= 0:
            raise ValueError("authorized amount must be positive")
        if not authorized_rails:
            raise ValueError("authorization requires at least one payment rail")
        if not approver_refs:
            raise ValueError("authorization requires explicit approver provenance")
        if not underwriting_evidence_ids:
            raise ValueError("authorization requires underwriting evidence")
    return {
        "project_event_id":str(project_event_id),
        "authorization_id":str(authorization_id),
        "decision":d,
        "max_amount":str(amount),
        "currency":currency.upper(),
        "authorized_rails":list(authorized_rails),
        "expires_at":expires_at.isoformat(),
        "conditions":list(conditions),
        "approver_refs":list(approver_refs),
        "policy_version":policy_version,
        "underwriting_evidence_ids":list(underwriting_evidence_ids),
    }
