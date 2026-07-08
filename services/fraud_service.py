"""
===========================================================
ARVIND
Module: Fraud Service
Purpose: Coordinates rule execution and produces analyst-ready fraud decisions.
Sprint: v0.7
===========================================================
"""

from intelligence.evidence.evidence_engine import (
    build_evidence_list,
    summarise_evidence,
    calculate_evidence_quality_score,
)

import pandas as pd

from intelligence.rule_engine.transaction_rules import (
    run_transaction_rules,
    calculate_rule_risk_score,
    get_risk_level,
    get_recommended_action,
)


def analyse_transactions(df: pd.DataFrame, mapping_df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts uploaded columns to canonical fields, runs fraud rules,
    and produces analyst-ready judgement outputs.
    """

    column_mapping = build_column_mapping(mapping_df)
    canonical_df = df.rename(columns=column_mapping)

    results = []

    for _, row in canonical_df.iterrows():
        row_dict = row.to_dict()

        evidence = run_transaction_rules(row_dict)
        structured_evidence = build_evidence_list(evidence)
        evidence_quality_score = calculate_evidence_quality_score(structured_evidence)
        risk_score = calculate_rule_risk_score(evidence)
        risk_level = get_risk_level(risk_score)
        action = get_recommended_action(risk_score)

        arvind_statement = generate_arvind_statement(
            risk_level=risk_level,
            action=action,
            evidence=evidence,
        )

        decision_reason = generate_decision_reason(evidence)
        call_priority = calculate_call_priority(risk_score, evidence)

        result = row_dict.copy()
        result["risk_score"] = risk_score
        result["risk_level"] = risk_level
        result["recommended_action"] = action
        result["call_priority"] = call_priority
        result["evidence_count"] = len(evidence)
        result["evidence_summary"] = summarise_evidence(structured_evidence)
        result["evidence_quality_score"] = evidence_quality_score
        result["evidence_details"] = str(structured_evidence)
        result["decision_reason"] = decision_reason
        result["arvind_statement"] = arvind_statement

        results.append(result)

    return pd.DataFrame(results)


def build_column_mapping(mapping_df: pd.DataFrame) -> dict:
    """
    Builds mapping from uploaded column names to canonical ARVIND field IDs.
    """

    column_mapping = {}

    for _, row in mapping_df.iterrows():
        if row["mapping_status"] == "Matched":
            column_mapping[row["uploaded_column"]] = row["canonical_field_id"]

    return column_mapping


def generate_evidence_summary(evidence: list) -> str:
    """
    Creates short evidence summary.
    """

    if not evidence:
        return "No rule-based risk evidence detected."

    return "; ".join(item["rule_name"] for item in evidence)


def generate_decision_reason(evidence: list) -> str:
    """
    Creates analyst-friendly decision reason.
    """

    if not evidence:
        return "No rule-based fraud indicators were detected."

    reasons = []

    for item in evidence:
        reasons.append(
            f"{item['rule_name']}: {item['business_reason']}"
        )

    return " | ".join(reasons)


def generate_arvind_statement(risk_level: str, action: str, evidence: list) -> str:
    """
    Produces a human-readable ARVIND judgement statement.
    """

    if not evidence:
        return (
            "ARVIND found no rule-based fraud indicators. "
            "Recommended action is to approve the transaction."
        )

    evidence_names = ", ".join(item["rule_name"] for item in evidence)

    return (
        f"ARVIND assessed this transaction as {risk_level} risk. "
        f"Recommended action: {action}. "
        f"Primary evidence: {evidence_names}."
    )


def calculate_call_priority(risk_score: int, evidence: list) -> str:
    """
    Determines whether contacting the cardholder is worthwhile.
    """

    evidence_ids = [item["rule_id"] for item in evidence]

    if risk_score >= 75:
        return "High"

    if "CVV_MISMATCH" in evidence_ids and "AVS_MISMATCH" in evidence_ids:
        return "High"

    if risk_score >= 40:
        return "Medium"

    return "Low"