from __future__ import annotations

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

data = load_resume_data()
exp = data.experience
certs = data.certifications.copy()

back_col, _ = st.columns([1, 5])
with back_col:
    st.page_link("pages/1_Career_Overview.py", label="← Career")

st.markdown("# Certifications")

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
    certs = certs[certs["ExperienceID"] == selected_id]

left, right = st.columns([1.2, 1.8], gap="large")

with left:
    st.markdown("### Certification types")
    by_type = certs.groupby("Type", as_index=False)["Name"].nunique()
    if not by_type.empty:
        fig = px.pie(
            by_type,
            values="Name",
            names="Type",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        fig.update_layout(height=320, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No certifications match the selected filters.")

    st.markdown("### Providers")
    by_provider = certs.groupby("Provider", as_index=False)["Name"].nunique().sort_values("Name")
    if not by_provider.empty:
        bar = px.bar(
            by_provider,
            x="Name",
            y="Provider",
            orientation="h",
            color_discrete_sequence=["#d97706"],
        )
        bar.update_layout(height=320, margin=dict(l=10, r=10, t=10, b=10), xaxis_title="Count")
        st.plotly_chart(bar, use_container_width=True)

with right:
    st.markdown("### Detail table")
    detail = certs.merge(
        exp[["ExperienceID", "Experience", "Role"]],
        on="ExperienceID",
        how="left",
    )
    detail = detail[["Experience", "Role", "Name", "Provider", "Type", "Link"]]
    st.dataframe(detail, use_container_width=True, hide_index=True)
