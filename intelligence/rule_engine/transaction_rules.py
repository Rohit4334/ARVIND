"""
===========================================================
ARVIND
Module: Transaction Rules
Purpose: Executes fraud rules using the Fraud Rule Library.
Sprint: v0.6
===========================================================
"""

from canonical.rule_library import get_rule


def create_evidence(rule_id: str) -> dict:
    """
    Converts a triggered rule into a structured evidence object.
    """

    rule = get_rule(rule_id)

    return {
        "rule_id": rule_id,
        "rule_name": rule["rule_name"],
        "category": rule["category"],
        "severity": rule["severity"],
        "risk_points": rule["risk_points"],
        "evidence_type": rule["evidence_type"],
        "explanation": rule["ai_explanation"],
        "business_reason": rule["business_reason"],
        "recommended_investigation": "; ".join(rule["recommended_investigation"]),
    }


def run_transaction_rules(row: dict) -> list:
    """
    Runs transaction-level fraud rules on one transaction.
    """

    evidence = []

    amount = row.get("transaction_amount")
    avs = str(row.get("avs_result", "")).lower()
    cvv = str(row.get("cvv_result", "")).lower()
    status = str(row.get("transaction_status", "")).lower()
    card_country = str(row.get("card_issuing_country", "")).lower()
    txn_country = str(row.get("transaction_country", "")).lower()

    try:
        amount = float(amount)
    except (TypeError, ValueError):
        amount = None

    high_amount_rule = get_rule("HIGH_AMOUNT")
    if amount is not None and amount >= high_amount_rule["default_threshold"]:
        evidence.append(create_evidence("HIGH_AMOUNT"))

    if "no" in avs or "fail" in avs or "mismatch" in avs:
        evidence.append(create_evidence("AVS_MISMATCH"))

    if "no" in cvv or "fail" in cvv or "mismatch" in cvv:
        evidence.append(create_evidence("CVV_MISMATCH"))

    if status == "declined":
        evidence.append(create_evidence("DECLINED_TRANSACTION"))

    if card_country and txn_country and card_country != txn_country:
        evidence.append(create_evidence("COUNTRY_MISMATCH"))

    return evidence


def calculate_rule_risk_score(evidence: list) -> int:
    total = sum(item["risk_points"] for item in evidence)
    return min(total, 100)


def get_risk_level(score: int) -> str:
    if score >= 75:
        return "High"
    elif score >= 40:
        return "Medium"
    elif score >= 1:
        return "Low"
    return "Clear"


def get_recommended_action(score: int) -> str:
    if score >= 75:
        return "Manual Review / Contact Cardholder"
    elif score >= 40:
        return "Review"
    elif score >= 1:
        return "Monitor"
    return "Approve"