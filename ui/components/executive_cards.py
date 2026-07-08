"""
===========================================================
ARVIND
Module: Executive KPI Cards
Purpose: Render reusable executive KPI cards.
Presentation Sprint PS-2
===========================================================
"""

import streamlit as st


def render_executive_dashboard(
    total_cases: int,
    open_cases: int,
    high_risk: int,
    medium_risk: int,
    call_priority: int,
    risky_value: float,
):
    """
    Renders the Executive Dashboard KPI cards.
    """

    st.markdown("## 📊 Executive Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="📁 Cases Created",
        value=f"{total_cases:,}"
    )

    col2.metric(
        label="📂 Open Cases",
        value=f"{open_cases:,}"
    )

    col3.metric(
        label="🔴 High Risk",
        value=f"{high_risk:,}"
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        label="🟠 Medium Risk",
        value=f"{medium_risk:,}"
    )

    col5.metric(
        label="📞 Call Priority",
        value=f"{call_priority:,}"
    )

    col6.metric(
        label="💷 Risk Exposure",
        value=f"£{risky_value:,.2f}"
    )

    st.divider()