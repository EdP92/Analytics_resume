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

query_id = st.query_params.get("experience_id")
if isinstance(query_id, list):
    query_id = query_id[0] if query_id else None
if query_id:
    try:
        st.session_state.selected_experience_id = int(query_id)
    except ValueError:
        st.session_state.selected_experience_id = None

back_col, _ = st.columns([1, 5])
with back_col:
    st.page_link("pages/1_Career_Overview.py", label="← Career Overview")

st.markdown("# Certifications")

exp_labels = exp.assign(Label=exp["Role"] + " · " + exp["Experience"])
options = ["All experiences"] + exp_labels["Label"].tolist()

filter_key = "certs_filter"
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


filter_col, clear_col = st.columns([4, 1])
with filter_col:
    selected_label = st.selectbox("Experience filter", options, key=filter_key)
with clear_col:
    st.button("Clear filters", use_container_width=True, on_click=_clear_filters)

selected_id = None
if selected_label != "All experiences":
    selected_id = exp_labels.loc[exp_labels["Label"] == selected_label, "ExperienceID"].iloc[0]
st.session_state.selected_experience_id = selected_id

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
