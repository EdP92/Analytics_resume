from __future__ import annotations

import plotly.express as px
import streamlit as st

from lib.data import load_resume_data
from lib.style import apply_base_styles


st.set_page_config(
    page_title="Skills",
    page_icon="🧩",
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
skills = data.skills.copy()

query_id = st.query_params.get("experience_id")
if isinstance(query_id, list):
    query_id = query_id[0] if query_id else None
if query_id:
    try:
        st.session_state.selected_experience_id = int(query_id)
    except ValueError:
        st.session_state.selected_experience_id = None

st.page_link("pages/1_Career_Overview.py", label="← Career Overview")

st.markdown("# Skills")

exp_labels = exp.assign(Label=exp["Role"] + " · " + exp["Experience"])
options = ["All experiences"] + exp_labels["Label"].tolist()

filter_key = "skills_filter"
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
        line-height: 1;
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
        st.button("×", on_click=_clear_filters, key="skills_clear", help="Clear filters")
        st.markdown("</div>", unsafe_allow_html=True)

selected_id = None
if selected_label != "All experiences":
    selected_id = exp_labels.loc[exp_labels["Label"] == selected_label, "ExperienceID"].iloc[0]
st.session_state.selected_experience_id = selected_id

if selected_id is not None:
    skills = skills[skills["ExperienceID"] == selected_id]

skills_by_name = (
    skills.groupby("Skill", as_index=False)["Years_Used"].sum().sort_values("Years_Used", ascending=False)
)

skills_by_cat = (
    skills.groupby("Category", as_index=False)["Skill"].nunique().sort_values("Skill", ascending=False)
)

left, right = st.columns([2, 1], gap="large")

with left:
    st.markdown("### Detail table")
    detail = skills.merge(
        exp[["ExperienceID", "Experience", "Team", "Role"]],
        on="ExperienceID",
        how="left",
        suffixes=("", "_exp"),
    )
    detail = detail.rename(
        columns={
            "Experience": "Experience",
            "Role": "Role",
            "Team": "Team",
            "Skill": "Skill",
            "Level": "Level",
            "Years_Used": "Years Used",
        }
    )
    detail = detail[["Experience", "Role", "Team", "Category", "Skill", "Level", "Years Used"]]
    st.dataframe(detail, use_container_width=True, hide_index=True)

with right:
    st.markdown("### Category split")
    if not skills_by_cat.empty:
        pie = px.pie(
            skills_by_cat,
            values="Skill",
            names="Category",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        pie.update_layout(height=180, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(pie, use_container_width=True)

    st.markdown("### Skills list & years of usage")
    if not skills_by_name.empty:
        fig = px.bar(
            skills_by_name,
            x="Years_Used",
            y="Skill",
            orientation="h",
            color="Skill",
            color_discrete_sequence=px.colors.qualitative.Set3,
        )
        fig.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10), xaxis_title="Years")
        fig.update_traces(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No skills match the selected filters.")
