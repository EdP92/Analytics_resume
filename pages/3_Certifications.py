from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from lib.data import load_resume_data
from lib.style import apply_base_styles


st.set_page_config(
    page_title="Certifications",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="collapsed",
)
apply_base_styles()

st.markdown(
    """
    <style>
    .stPlotlyChart {
        border: 0 !important;
        border-radius: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

data = load_resume_data()
exp = data.experience
certs = data.certifications.copy()
if "Year_Issued" not in certs.columns:
    certs["Year_Issued"] = pd.NA

query_id = st.query_params.get("experience_id")
if isinstance(query_id, list):
    query_id = query_id[0] if query_id else None
if query_id:
    try:
        st.session_state.selected_experience_id = int(query_id)
    except ValueError:
        st.session_state.selected_experience_id = None

top_left, top_mid, _ = st.columns([1.1, 2.8, 1], gap="large")
with top_left:
    st.page_link("pages/1_Career_Overview.py", label="← Career Overview")
with top_mid:
    st.markdown("# Certifications", text_alignment="center")

st.markdown("<div style='margin-top: -8px;'></div>", unsafe_allow_html=True)

exp_labels = exp.assign(Label=exp["Role"] + " · " + exp["Experience"])
options = ["All experiences"] + exp_labels["Label"].tolist()

filter_key = "certs_filter"
if query_id and filter_key not in st.session_state:
    preselected_id = st.session_state.get("selected_experience_id")
    if preselected_id is not None:
        match = exp_labels.loc[exp_labels["ExperienceID"] == preselected_id, "Label"]
        if not match.empty:
            st.session_state[filter_key] = match.iloc[0]
elif filter_key not in st.session_state:
    st.session_state[filter_key] = "All experiences"

def _clear_filters() -> None:
    st.session_state.selected_experience_id = None
    st.session_state[filter_key] = "All experiences"
    st.query_params.clear()


st.markdown(
    """
    <style>
    .icon-clear button {
        width: 30px;
        height: 30px;
        min-width: 30px;
        padding: 0;
        border-radius: 6px;
        border: 1px solid #111111;
        background-color: #ffffff;
        color: #7f1d1d;
        font-size: 20px;
        line-height: 1;
        font-weight: 700;
    }
    .icon-clear button:hover {
        background-color: #f3f4f6;
    }
    .filter-drop {
        margin-top: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

row_left, _ = st.columns([1.4, 2.6])
with row_left:
    filter_col, clear_col = st.columns([0.8, 0.2], gap="small")
    with filter_col:
        st.markdown('<div class="filter-drop">', unsafe_allow_html=True)
        selected_label = st.selectbox(
            "Experience filter",
            options,
            key=filter_key,
            label_visibility="collapsed",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with clear_col:
        st.markdown('<div class="icon-clear">', unsafe_allow_html=True)
        st.button("×", on_click=_clear_filters, key="certs_clear", help="Clear filters")
        st.markdown("</div>", unsafe_allow_html=True)

selected_id = None
if selected_label != "All experiences":
    selected_id = exp_labels.loc[exp_labels["Label"] == selected_label, "ExperienceID"].iloc[0]
st.session_state.selected_experience_id = selected_id

if selected_id is not None:
    certs = certs[certs["ExperienceID"] == selected_id]

left, right = st.columns([2, 1], gap="large")

with left:
    st.markdown("### Detail table")
    detail = certs.merge(
        exp[["ExperienceID", "Experience", "Role"]],
        on="ExperienceID",
        how="left",
    )
    detail = detail[["Type", "Provider", "Name", "Year_Issued", "Link"]]
    column_config = {}
    if "Year_Issued" in detail.columns:
        column_config["Year_Issued"] = st.column_config.NumberColumn("Year Issued")
    if "Link" in detail.columns:
        column_config["Link"] = st.column_config.LinkColumn("Link", display_text="🔗")
    st.dataframe(
        detail,
        use_container_width=True,
        hide_index=True,
        column_config=column_config,
    )

with right:
    st.markdown("### Certifications by type & provider")
    by_type_provider = certs.groupby(["Type", "Provider"], as_index=False)["Name"].nunique()
    if not by_type_provider.empty:
        stacked = px.bar(
            by_type_provider,
            x="Name",
            y="Type",
            color="Provider",
            orientation="h",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        stacked.update_layout(
            height=360,
            margin=dict(l=10, r=10, t=10, b=40),
            xaxis_title=None,
            yaxis_title=None,
            legend_title_text=None,
            showlegend=False,
        )
        st.plotly_chart(stacked, use_container_width=True)
    else:
        st.info("No certifications match the selected filters.")
