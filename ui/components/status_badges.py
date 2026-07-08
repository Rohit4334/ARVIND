"""
===========================================================
ARVIND
Module: Status Badges
Purpose: Render reusable enterprise-style status badges.
Presentation Sprint PS-3
===========================================================
"""

import streamlit as st


def render_status_badge(status: str):
    """
    Renders a pill-style status badge.
    """

    status = str(status)

    styles = {
        "High": {
            "bg": "#FDECEC",
            "text": "#B42318",
            "border": "#F5B5B0",
            "label": "🔴 HIGH",
        },
        "Medium": {
            "bg": "#FFF4E5",
            "text": "#B54708",
            "border": "#FED7AA",
            "label": "🟠 MEDIUM",
        },
        "Low": {
            "bg": "#ECFDF3",
            "text": "#027A48",
            "border": "#A6F4C5",
            "label": "🟢 LOW",
        },
        "Open": {
            "bg": "#EFF8FF",
            "text": "#175CD3",
            "border": "#B2DDFF",
            "label": "🔵 OPEN",
        },
        "Pending": {
            "bg": "#F4F3FF",
            "text": "#5925DC",
            "border": "#D9D6FE",
            "label": "🟣 PENDING",
        },
        "Review": {
            "bg": "#FEFBE8",
            "text": "#A15C07",
            "border": "#FEEE95",
            "label": "🟡 REVIEW",
        },
        "Approved": {
            "bg": "#ECFDF3",
            "text": "#027A48",
            "border": "#A6F4C5",
            "label": "🟢 APPROVED",
        },
        "Monitor": {
            "bg": "#F2F4F7",
            "text": "#344054",
            "border": "#D0D5DD",
            "label": "⚪ MONITOR",
        },
        "Auto Approved": {
            "bg": "#ECFDF3",
            "text": "#027A48",
            "border": "#A6F4C5",
            "label": "🟢 AUTO APPROVED",
        },
        "None": {
            "bg": "#F2F4F7",
            "text": "#344054",
            "border": "#D0D5DD",
            "label": "NONE",
        },
        "Unassigned": {
            "bg": "#F2F4F7",
            "text": "#344054",
            "border": "#D0D5DD",
            "label": "UNASSIGNED",
        },
    }

    style = styles.get(
        status,
        {
            "bg": "#F2F4F7",
            "text": "#344054",
            "border": "#D0D5DD",
            "label": status.upper(),
        },
    )

    st.markdown(
        f"""
        <div style="
            display:inline-block;
            background:{style["bg"]};
            color:{style["text"]};
            border:1px solid {style["border"]};
            padding:6px 12px;
            border-radius:999px;
            font-weight:700;
            font-size:13px;
            letter-spacing:0.3px;
            text-align:center;
            min-width:110px;
        ">
            {style["label"]}
        </div>
        """,
        unsafe_allow_html=True,
    )