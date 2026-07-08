"""
===========================================================
ARVIND
Module: Data Profiler
Purpose: Understand uploaded data before fraud analysis.
Sprint: v0.3
===========================================================
"""

import pandas as pd


def profile_dataframe(df: pd.DataFrame) -> dict:
    total_rows = len(df)
    total_columns = len(df.columns)

    missing_values = df.isnull().sum()
    missing_percent = (missing_values / total_rows * 100).round(2)

    duplicate_rows = df.duplicated().sum()

    profile = {
        "total_rows": total_rows,
        "total_columns": total_columns,
        "duplicate_rows": int(duplicate_rows),
        "columns": []
    }

    for column in df.columns:
        profile["columns"].append({
            "column_name": column,
            "data_type": str(df[column].dtype),
            "missing_values": int(missing_values[column]),
            "missing_percent": float(missing_percent[column]),
            "unique_values": int(df[column].nunique())
        })

    return profile


def calculate_data_quality_score(profile: dict) -> int:
    score = 100

    if profile["duplicate_rows"] > 0:
        score -= 10

    for column in profile["columns"]:
        if column["missing_percent"] > 50:
            score -= 10
        elif column["missing_percent"] > 20:
            score -= 5

    return max(score, 0)