"""
===========================================================
ARVIND
Adaptive Risk & Verification Intelligence
for Next-generation Detection
===========================================================

Module:
Home Page

Purpose:
Displays the landing page and system status for ARVIND.

Owner:
UI Team

Sprint:
v0.2

Author:
Rohit Sharma
Partner & CTO: ChatGPT

===========================================================
"""

import streamlit as st


def show_home_page():
    """
    Displays the ARVIND landing page.
    """

    

    st.title("🛡️ ARVIND")

    st.subheader(
        "Adaptive Risk & Verification Intelligence for Next-generation Detection"
    )

    st.markdown("### Enterprise Fraud Decision Intelligence Platform")

    st.divider()

    st.markdown("## System Status")
    st.success("🟢 Core System Ready")

    st.markdown("## Loaded Intelligence Modules")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("✅ **Data Intelligence**")
        st.markdown("✅ **Canonical Fraud Model**")
        st.markdown("✅ **Rule Intelligence**")

    with col2:
        st.markdown("✅ **Behavioural Intelligence**")
        st.markdown("✅ **Statistical Intelligence**")
        st.markdown("✅ **Travel Intelligence**")

    with col3:
        st.markdown("✅ **Scoring Engine**")
        st.markdown("✅ **Explainable AI**")
        st.markdown("✅ **Case Management Ready**")

    st.divider()

    st.markdown("## Project Identity")

    st.markdown("""
    **Founder & Product Owner:** Rohit Sharma  
    **AI Partner:** ChatGPT  
    **Sprint:** v0.2 – Foundation & Architecture  
    """)

    st.info(
        "ARVIND assists fraud analysts. It never replaces them."
    )

    st.markdown("### Helping Fraud Analysts Make Better Decisions")