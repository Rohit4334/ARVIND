import streamlit as st


def render_header():

    st.markdown("""
    <div style="
        background-color:#102A43;
        padding:25px;
        border-radius:15px;
        margin-bottom:25px;
        text-align:center;
    ">

    <h1 style="
        color:white;
        margin-bottom:5px;
        font-size:42px;
    ">
        🛡️ ARVIND
    </h1>

    <h3 style="
        color:#D9E2EC;
        margin-top:0px;
    ">
        Fraud Intelligence Platform
    </h3>

    <p style="
        color:#BCCCDC;
        font-size:18px;
    ">
        Understand • Investigate • Decide
    </p>

    </div>
    """, unsafe_allow_html=True)