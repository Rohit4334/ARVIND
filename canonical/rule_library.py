"""
===========================================================
ARVIND
Module: Fraud Rule Library
Purpose: Defines fraud rules as metadata-driven intelligence objects.
Sprint: v0.6
===========================================================
"""


FRAUD_RULE_LIBRARY = {
    "HIGH_AMOUNT": {
        "rule_name": "High Amount Transaction",
        "category": "Financial Risk",
        "severity": "High",
        "risk_points": 25,
        "evidence_type": "Financial Exposure",
        "description": "Transaction amount exceeds the configured high-value threshold.",
        "business_reason": "High-value transactions increase potential fraud loss and deserve closer review.",
        "default_threshold": 1000,
        "required_fields": ["transaction_amount"],
        "ai_explanation": "The transaction amount is materially higher than normal review thresholds.",
        "recommended_investigation": [
            "Check customer historical spend",
            "Check merchant category",
            "Check travel or corporate context"
        ],
        "active": True
    },

    "AVS_MISMATCH": {
        "rule_name": "AVS Mismatch",
        "category": "Verification Risk",
        "severity": "High",
        "risk_points": 25,
        "evidence_type": "Address Verification Failure",
        "description": "Address verification result indicates mismatch or failure.",
        "business_reason": "AVS mismatch can indicate that the person using the card does not know the billing address.",
        "default_threshold": None,
        "required_fields": ["avs_result"],
        "ai_explanation": "The billing address verification did not match expected cardholder information.",
        "recommended_investigation": [
            "Check billing postcode",
            "Check customer country",
            "Check whether customer is US-based"
        ],
        "active": True
    },

    "CVV_MISMATCH": {
        "rule_name": "CVV Mismatch",
        "category": "Verification Risk",
        "severity": "Critical",
        "risk_points": 30,
        "evidence_type": "Card Verification Failure",
        "description": "CVV result indicates mismatch or failure.",
        "business_reason": "CVV mismatch may indicate card testing or unauthorised card use.",
        "default_threshold": None,
        "required_fields": ["cvv_result"],
        "ai_explanation": "The card security code verification failed.",
        "recommended_investigation": [
            "Check decline history",
            "Check previous successful attempts",
            "Check card testing pattern"
        ],
        "active": True
    },

    "DECLINED_TRANSACTION": {
        "rule_name": "Declined Transaction",
        "category": "Authorisation Risk",
        "severity": "Medium",
        "risk_points": 10,
        "evidence_type": "Authorisation Failure",
        "description": "Transaction was declined.",
        "business_reason": "Declines can be normal, but repeated declines may indicate card testing or issuer rejection.",
        "default_threshold": None,
        "required_fields": ["transaction_status"],
        "ai_explanation": "The transaction was not approved by the authorisation process.",
        "recommended_investigation": [
            "Review decline reason",
            "Check repeat attempts",
            "Check whether later transaction was approved"
        ],
        "active": True
    },

    "COUNTRY_MISMATCH": {
        "rule_name": "Card Country and Transaction Country Mismatch",
        "category": "Geographic Risk",
        "severity": "Medium",
        "risk_points": 15,
        "evidence_type": "Geographic Mismatch",
        "description": "Card issuing country differs from transaction country.",
        "business_reason": "Country mismatch can indicate legitimate travel or suspicious cross-border card use.",
        "default_threshold": None,
        "required_fields": ["card_issuing_country", "transaction_country"],
        "ai_explanation": "The card issuing country is different from the country where the transaction occurred.",
        "recommended_investigation": [
            "Check travel itinerary",
            "Check previous country behaviour",
            "Check billing country"
        ],
        "active": True
    }
}


def get_rule(rule_id: str) -> dict | None:
    """
    Returns one fraud rule by rule_id.
    """
    return FRAUD_RULE_LIBRARY.get(rule_id)


def get_all_rules() -> dict:
    """
    Returns all fraud rules.
    """
    return FRAUD_RULE_LIBRARY


def get_active_rules() -> dict:
    """
    Returns only active fraud rules.
    """
    return {
        rule_id: rule
        for rule_id, rule in FRAUD_RULE_LIBRARY.items()
        if rule.get("active") is True
    }