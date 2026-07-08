"""
===========================================================
ARVIND
Module: Schema Mapper
Purpose: Maps uploaded dataset columns to ARVIND canonical fields.
Sprint: v0.4
===========================================================
"""

from canonical.fraud_knowledge_base import get_alias_map, get_all_fields


def normalise_column_name(column_name: str) -> str:
    """
    Standardises column names for comparison.
    Example:
    'Transaction Amount' -> 'transaction_amount'
    """
    return (
        column_name.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace(".", "_")
    )


def map_columns_to_schema(uploaded_columns: list) -> list:
    """
    Maps uploaded column names to ARVIND canonical fields.
    """

    alias_map = get_alias_map()
    knowledge_base = get_all_fields()

    mapping_results = []

    for column in uploaded_columns:
        normalised_column = normalise_column_name(column)

        if normalised_column in alias_map:
            field_id = alias_map[normalised_column]
            field_info = knowledge_base[field_id]

            mapping_results.append({
                "uploaded_column": column,
                "canonical_field_id": field_id,
                "canonical_display_name": field_info["display_name"],
                "category": field_info["category"],
                "confidence": 100,
                "mapping_status": "Matched"
            })

        else:
            mapping_results.append({
                "uploaded_column": column,
                "canonical_field_id": None,
                "canonical_display_name": "Unmapped",
                "category": "Unknown",
                "confidence": 0,
                "mapping_status": "Unmapped"
            })

    return mapping_results