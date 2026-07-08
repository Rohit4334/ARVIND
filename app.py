"""
===========================================================
ARVIND
Module: Application Entry Point
Purpose: Starts the ARVIND Streamlit application.
Sprint: v0.3
===========================================================
"""

import streamlit as st

from ui.pages.home import show_home_page
from ui.pages.upload_page import show_upload_page


def main():
    st.sidebar.title("🛡️ ARVIND")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Data Intelligence"
        ]
    )

    if page == "Home":
        show_home_page()

    elif page == "Data Intelligence":
        show_upload_page()


if __name__ == "__main__":
    main()