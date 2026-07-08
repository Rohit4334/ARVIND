"""
===========================================================
ARVIND
Module: Evidence Engine
Purpose: Converts rule outputs into structured fraud evidence.
Sprint: v0.8
===========================================================
"""


def build_evidence_object(rule_evidence: dict, sequence: int) -> dict:
    """
    Converts rule engine output into a standard ARVIND evidence object.
    """

    return {
        "evidence_id": f"EVID-{sequence:03}",
        "source_engine": "Rule Engine",
        "rule_id": rule_evidence.get("rule_id"),
        "category": rule_evidence.get("category"),
        "evidence_type": rule_evidence.get("evidence_type"),
        "finding": rule_evidence.get("rule_name"),
        "severity": rule_evidence.get("severity"),
        "confidence": assign_confidence(rule_evidence.get("severity")),
        "weight": rule_evidence.get("risk_points", 0),
        "business_reason": rule_evidence.get("business_reason"),
        "explanation": rule_evidence.get("explanation"),
        "recommended_investigation": rule_evidence.get("recommended_investigation"),
    }


def build_evidence_list(rule_evidence_list: list) -> list:
    """
    Converts all rule evidence into structured ARVIND evidence objects.
    """

    evidence_objects = []

    for index, rule_evidence in enumerate(rule_evidence_list, start=1):
        evidence_objects.append(
            build_evidence_object(rule_evidence, index)
        )

    return evidence_objects


def assign_confidence(severity: str) -> int:
    """
    Assigns simple confidence based on severity.
    """

    if severity == "Critical":
        return 95
    if severity == "High":
        return 85
    if severity == "Medium":
        return 70
    if severity == "Low":
        return 50

    return 40


def summarise_evidence(evidence_objects: list) -> str:
    """
    Creates short analyst-friendly evidence summary.
    """

    if not evidence_objects:
        return "No structured fraud evidence detected."

    return "; ".join(
        f"{item['finding']} ({item['severity']})"
        for item in evidence_objects
    )


def calculate_evidence_quality_score(evidence_objects: list) -> int:
    """
    Calculates quality of available evidence.
    """

    if not evidence_objects:
        return 0

    total_confidence = sum(item["confidence"] for item in evidence_objects)
    return round(total_confidence / len(evidence_objects))