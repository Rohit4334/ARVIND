"""
===========================================================
ARVIND
Module: Upload Page
Purpose: Upload, profile, and map transaction data.
Sprint: v0.4
===========================================================
"""
from ui.components.header import render_header
from services.case_service import create_cases_from_transactions
from ui.components.executive_cards import render_executive_dashboard
from ui.components.status_badges import render_status_badge
from ui.components.investigation_cards import render_investigation_cards

from services.fraud_service import analyse_transactions

import streamlit as st
import pandas as pd

from ingestion.data_profiler import (
    profile_dataframe,
    calculate_data_quality_score,
)
from canonical.schema_mapper import map_columns_to_schema


def show_upload_page():
    render_header()

    st.caption(
    "Upload transaction data for profiling, fraud detection and investigation."
)

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is None:
        st.info("Upload a CSV file to begin ARVIND's data intelligence process.")
        return

    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully")

    profile = profile_dataframe(df)
    quality_score = calculate_data_quality_score(profile)

    mapping_results = map_columns_to_schema(list(df.columns))
    mapping_df = pd.DataFrame(mapping_results)

    show_data_preview(df)
    show_data_health(profile, quality_score)
    show_schema_mapping(mapping_df)
    show_column_profile(profile)
    show_final_assessment(quality_score, mapping_df)
    analysed_df = analyse_transactions(df, mapping_df)
    case_df = create_cases_from_transactions(analysed_df)
    show_rule_engine_results(case_df)

    


def show_data_preview(df: pd.DataFrame):
    st.markdown("## Data Preview")
    st.dataframe(df.head(20), use_container_width=True)


def show_data_health(profile: dict, quality_score: int):
    st.markdown("## Data Health Report")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", profile["total_rows"])
    col2.metric("Columns", profile["total_columns"])
    col3.metric("Duplicate Rows", profile["duplicate_rows"])
    col4.metric("Data Quality Score", f"{quality_score}/100")


def show_schema_mapping(mapping_df: pd.DataFrame):
    st.markdown("## Schema Intelligence Mapping")

    st.dataframe(mapping_df, use_container_width=True)

    matched_count = len(mapping_df[mapping_df["mapping_status"] == "Matched"])
    total_count = len(mapping_df)

    mapping_score = round((matched_count / total_count) * 100, 2)

    col1, col2, col3 = st.columns(3)

    col1.metric("Schema Understanding Score", f"{mapping_score}%")
    col2.metric("Mapped Fields", matched_count)
    col3.metric("Unmapped Fields", total_count - matched_count)

    if mapping_score >= 80:
        st.success("ARVIND understands most of this dataset schema.")
    elif mapping_score >= 50:
        st.warning("ARVIND partially understands this dataset. Some fraud engines may be limited.")
    else:
        st.error("ARVIND has limited understanding of this schema. More mapping is required.")


def show_column_profile(profile: dict):
    st.markdown("## Column Profile")

    column_profile_df = pd.DataFrame(profile["columns"])
    st.dataframe(column_profile_df, use_container_width=True)


def show_final_assessment(quality_score: int, mapping_df: pd.DataFrame):
    st.markdown("## Final Data Intelligence Assessment")

    matched_count = len(mapping_df[mapping_df["mapping_status"] == "Matched"])
    total_count = len(mapping_df)
    mapping_score = round((matched_count / total_count) * 100, 2)

    if quality_score >= 85 and mapping_score >= 80:
        st.success("ARVIND is ready to proceed with high confidence.")
    elif quality_score >= 60 and mapping_score >= 50:
        st.warning("ARVIND can proceed, but some engines may have limited confidence.")
    else:
        st.error("ARVIND requires better data or manual schema mapping before reliable fraud analysis.")

def show_rule_engine_results(analysed_df: pd.DataFrame):
    st.markdown("## Case Management & Rule Engine Results")
    analysed_df["transaction_amount"] = pd.to_numeric(
analysed_df["transaction_amount"],
 errors="coerce"
    ).fillna(0)
    """
    Shows analyst-ready fraud rule engine results.
    """


    total_transactions = len(analysed_df)
    open_cases = len(analysed_df[analysed_df["case_status"] == "Open"])
    monitor_cases = len(analysed_df[analysed_df["case_status"] == "Monitor"])
    high_risk_count = len(analysed_df[analysed_df["risk_level"] == "High"])
    medium_risk_count = len(analysed_df[analysed_df["risk_level"] == "Medium"])
    call_priority_count = len(analysed_df[analysed_df["call_priority"] == "High"])

    risky_value = analysed_df[
        analysed_df["risk_level"].isin(["High", "Medium"])
    ]["transaction_amount"].sum()

    render_executive_dashboard(
    total_cases=total_transactions,
    open_cases=open_cases,
    high_risk=high_risk_count,
    medium_risk=medium_risk_count,
    call_priority=call_priority_count,
    risky_value=risky_value,
)

    st.markdown("### Risk Level Summary")

    risk_summary = analysed_df["risk_level"].value_counts().reset_index()
    risk_summary.columns = ["Risk Level", "Count"]
    st.dataframe(risk_summary, use_container_width=True)

    st.markdown("### Call Priority Queue")

    call_queue_df = analysed_df[
        analysed_df["call_priority"].isin(["High", "Medium"])
    ]

    st.dataframe(call_queue_df, use_container_width=True)

    st.markdown("### All Transactions with ARVIND Judgement")

    judgement_columns = [
        "case_id",
        "case_status",
        "case_priority",
        "assigned_to",
        "final_decision",
        "transaction_id",
        "transaction_timestamp",
        "transaction_amount",
        "currency",
        "transaction_status",
        "risk_score",
        "risk_level",
        "recommended_action",
        "call_priority",
        "evidence_count",
        "evidence_summary",
        "decision_reason",
        "arvind_statement",
        "evidence_quality_score",
        "evidence_details",
    ]

    available_judgement_columns = [
        col for col in judgement_columns if col in analysed_df.columns
    ]

    st.dataframe(
        analysed_df[available_judgement_columns],
        use_container_width=True
    )

    st.markdown("### High and Medium Risk Cases")

    risky_df = analysed_df[
        analysed_df["risk_level"].isin(["High", "Medium"])
    ]

    st.dataframe(risky_df, use_container_width=True)
    show_investigation_workspace(analysed_df)

def show_investigation_workspace(analysed_df: pd.DataFrame):
    """
    Shows a transaction-level investigation workspace.
    """

    st.markdown("## 🕵️ Investigation Workspace")

    investigation_df = analysed_df[
        analysed_df["risk_level"].isin(["High", "Medium"])
    ].copy()

    if investigation_df.empty:
        st.success("No high or medium risk transactions require investigation.")
        return

    transaction_options = investigation_df["case_id"].astype(str).tolist()
    selected_case_id = st.selectbox(
    "Select case to investigate",
    transaction_options
)

    selected_case = investigation_df[
    investigation_df["case_id"].astype(str) == selected_case_id
].iloc[0]

    st.markdown("### Case Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Case ID", selected_case.get("case_id", "N/A"))
    col2.metric("Risk Score", selected_case.get("risk_score", "N/A"))
    col3.metric("Risk Level", selected_case.get("risk_level", "N/A"))
    col4.metric("Call Priority", selected_case.get("call_priority", "N/A"))
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.write("Case Status")
        render_status_badge(
            selected_case.get("case_status", "N/A")
    )

    with col6:
        st.write("Case Priority")
        render_status_badge(
            selected_case.get("case_priority", "N/A")
    )

    with col7:
        st.write("Assigned To")
        render_status_badge(
            selected_case.get("assigned_to", "Unassigned")
    )

    with col8:
        st.write("Final Decision")
        render_status_badge(
            selected_case.get("final_decision", "Pending")
    )


    st.markdown("### Recommended Action")
    st.warning(selected_case.get("recommended_action", "No recommendation available."))

    st.markdown("### ARVIND Statement")
    st.info(selected_case.get("arvind_statement", "No ARVIND statement available."))

    st.markdown("### Evidence Summary")
    st.write(selected_case.get("evidence_summary", "No evidence available."))

    st.markdown("### Decision Reason")
    st.write(selected_case.get("decision_reason", "No decision reason available."))

    render_investigation_cards(
    selected_case.get(
        "evidence_details",
        ""
    )
)

    st.markdown("### Analyst Notes")

    if "analyst_notes" not in st.session_state:
        st.session_state["analyst_notes"] = {}

    if selected_case_id not in st.session_state["analyst_notes"]:
        st.session_state["analyst_notes"][selected_case_id] = []

    analyst_name_key = f"analyst_name_{selected_case_id}"
    note_input_key = f"note_input_{selected_case_id}"

    analyst_name = st.text_input(
        "Analyst Name",
        placeholder="Example: Analyst 1",
        key=analyst_name_key
    )

    analyst_note = st.text_area(
        "Add analyst notes for this investigation",
        placeholder="Example: Customer contacted. No response to call.",
        height=120,
        key=note_input_key
    )

    if st.button("Save Analyst Note", key=f"save_note_{selected_case_id}"):
        if analyst_note.strip():
            from datetime import datetime

            note_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "analyst_name": analyst_name if analyst_name.strip() else "Unknown Analyst",
                "note": analyst_note.strip()
            }

            st.session_state["analyst_notes"][selected_case_id].append(note_entry)

            st.success("Analyst note saved for this session.")
        else:
            st.warning("Please enter a note before saving.")

    saved_notes = st.session_state["analyst_notes"][selected_case_id]

    if saved_notes:
        st.markdown("### Saved Analyst Notes")

        for index, note in enumerate(saved_notes, start=1):
            st.markdown(f"**Note {index}**")
            st.write(f"**Time:** {note['timestamp']}")
            st.write(f"**Analyst:** {note['analyst_name']}")
            st.info(note["note"])