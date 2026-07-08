"""
===========================================================
ARVIND
Module: Case Service
Purpose: Creates fraud investigation cases from analysed transactions.
Sprint: v0.10
===========================================================
"""

from datetime import datetime
import pandas as pd


def create_cases_from_transactions(analysed_df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts analysed transactions into investigation cases.
    """

    cases = []

    for index, row in analysed_df.iterrows():
        case_id = f"CASE-{index + 1:06}"

        case_status = determine_case_status(row)
        case_priority = determine_case_priority(row)

        case = row.to_dict()
        case["case_id"] = case_id
        case["case_status"] = case_status
        case["case_priority"] = case_priority
        case["assigned_to"] = "Unassigned"
        case["opened_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        case["closed_timestamp"] = ""
        case["final_decision"] = "Pending"
        case["review_required"] = case_status != "Auto Approved"

        cases.append(case)

    return pd.DataFrame(cases)


def determine_case_status(row) -> str:
    """
    Determines initial case status.
    """

    risk_level = row.get("risk_level", "Clear")

    if risk_level in ["High", "Medium"]:
        return "Open"

    if risk_level == "Low":
        return "Monitor"

    return "Auto Approved"


def determine_case_priority(row) -> str:
    """
    Determines case priority.
    """

    risk_level = row.get("risk_level", "Clear")
    call_priority = row.get("call_priority", "Low")

    if risk_level == "High" or call_priority == "High":
        return "High"

    if risk_level == "Medium" or call_priority == "Medium":
        return "Medium"

    if risk_level == "Low":
        return "Low"

    return "None"