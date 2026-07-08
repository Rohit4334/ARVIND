import streamlit as st
import ast

from ui.components.status_badges import render_status_badge


CATEGORY_ICONS = {
    "Financial": "💰",
    "Authentication": "🔐",
    "Identity": "👤",
    "Geography": "🌍",
    "Behaviour": "🖥️",
    "Device": "💻",
    "Browser": "🌐",
    "Network": "📡",
    "General": "📋",
}


def render_investigation_cards(evidence_details):

    if not evidence_details:
        st.info("No investigation evidence available.")
        return

    try:
        evidence = ast.literal_eval(evidence_details)
    except Exception:
        st.warning("Unable to read investigation evidence.")
        return

    st.markdown("## 🕵️ Investigation Findings")

    for item in evidence:

        category = item.get("category", "General")
        icon = CATEGORY_ICONS.get(category, "📋")

        with st.container(border=True):

            st.markdown(
                f"### {icon} {category}"
            )

            st.write(
                f"**Finding:** {item.get('finding','')}"
            )

            st.write(
                item.get("business_reason", "")
            )

            col1, col2 = st.columns(2)

            with col1:
                st.write("Severity")
                render_status_badge(
                    item.get("severity", "")
                )

            with col2:
                st.metric(
                    "Confidence",
                    f"{item.get('confidence',0)}%"
                )

            st.write("**Recommended Investigation**")

            st.info(
                item.get(
                    "recommended_investigation",
                    "None"
                )
            )

        st.markdown("")