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

data = load_resume_data()
exp = data.experience
skills = data.skills.copy()

back_col, _ = st.columns([1, 5])
with back_col:
    if st.button("← Back to Career", use_container_width=True):
        st.switch_page("pages/1_Career_Overview.py")

st.markdown("# Skills")

exp_labels = exp.assign(Label=exp["Role"] + " · " + exp["Experience"])
options = ["All experiences"] + exp_labels["Label"].tolist()

default_index = 0
preselected_id = st.session_state.get("selected_experience_id")
if preselected_id is not None:
    match = exp_labels.loc[exp_labels["ExperienceID"] == preselected_id, "Label"]
    if not match.empty:
        default_index = options.index(match.iloc[0])

selected_label = st.selectbox("Experience filter", options, index=default_index)
selected_id = None
if selected_label != "All experiences":
    selected_id = exp_labels.loc[exp_labels["Label"] == selected_label, "ExperienceID"].iloc[0]

if selected_id is not None:
    skills = skills[skills["ExperienceID"] == selected_id]

skills_by_name = (
    skills.groupby("Skill", as_index=False)["Years_Used"].sum().sort_values("Years_Used", ascending=True)
)

skills_by_cat = (
    skills.groupby("Category", as_index=False)["Skill"].nunique().sort_values("Skill", ascending=False)
)

left, right = st.columns([1.2, 1.8], gap="large")

with left:
    st.markdown("### Skills list & years of usage")
    if not skills_by_name.empty:
        fig = px.bar(
            skills_by_name,
            x="Years_Used",
            y="Skill",
            orientation="h",
            color_discrete_sequence=["#2563eb"],
        )
        fig.update_layout(height=420, margin=dict(l=10, r=10, t=10, b=10), xaxis_title="Years")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No skills match the selected filters.")

    st.markdown("### Category split")
    if not skills_by_cat.empty:
        pie = px.pie(
            skills_by_cat,
            values="Skill",
            names="Category",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        pie.update_layout(height=320, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(pie, use_container_width=True)

with right:
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
