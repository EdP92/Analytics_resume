from __future__ import annotations

import hashlib

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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

top_left, top_mid, _ = st.columns([1.1, 2.8, 1], gap="large")
with top_left:
    st.page_link("pages/1_Career_Overview.py", label="← Career Overview")
with top_mid:
    st.markdown("# Skills", text_alignment="center")

st.markdown("<div style='margin-top: -8px;'></div>", unsafe_allow_html=True)

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
    st.dataframe(detail, use_container_width=True, hide_index=True, height=520)

with right:
    st.markdown("### Skills radar")
    if not skills.empty:
        levels = ["Basic", "Intermediate", "Advanced"]
        level_map = {lvl.lower(): idx for idx, lvl in enumerate(levels, start=1)}
        skills["level_norm"] = skills["Level"].astype(str).str.strip().str.lower()
        skills = skills[skills["level_norm"].isin(level_map)]
        skills["level_idx"] = skills["level_norm"].map(level_map)

        skills = (
            skills.groupby(["Skill", "Category", "Level", "level_norm", "level_idx"], as_index=False)[
                "Years_Used"
            ]
            .sum()
        )

        categories = sorted(skills["Category"].dropna().unique().tolist())
        span = 360 / max(len(categories), 1)

        def _stable_jitter(value: str) -> float:
            digest = hashlib.md5(value.encode("utf-8")).hexdigest()
            return (int(digest[:8], 16) / 0xFFFFFFFF) - 0.5

        max_years_by_level = skills.groupby("level_idx")["Years_Used"].max().to_dict()
        max_years_overall = skills["Years_Used"].max() or 1

        def _radius(row: pd.Series) -> float:
            base = row["level_idx"] - 1
            max_years = max_years_by_level.get(row["level_idx"], 1) or 1
            return base + 0.15 + (row["Years_Used"] / max_years) * 0.7

        skills["r"] = skills.apply(_radius, axis=1)
        skills["size"] = 8 + (skills["Years_Used"] / max_years_overall) * 10
        skills["theta"] = skills.apply(
            lambda r: (
                categories.index(r["Category"]) * span
                + _stable_jitter(str(r["Skill"])) * (span * 0.8)
            ),
            axis=1,
        )

        palette = px.colors.qualitative.Set2
        color_map = {
            category: palette[i % len(palette)] for i, category in enumerate(categories)
        }
        skills["color"] = skills["Category"].map(color_map)

        fig = go.Figure()
        for category, group in skills.groupby("Category"):
            fig.add_trace(
                go.Scatterpolar(
                    r=group["r"],
                    theta=group["theta"],
                    mode="markers",
                    name=category,
                    marker=dict(
                        size=group["size"],
                        color=group["color"].iloc[0],
                        line=dict(color="rgba(17,24,39,0.35)", width=0.6),
                    ),
                    hovertemplate=(
                        "<b>%{customdata[0]}</b><br>"
                        "Category: %{customdata[1]}<br>"
                        "Level: %{customdata[2]}<br>"
                        "Years: %{customdata[3]}<extra></extra>"
                    ),
                    customdata=group[["Skill", "Category", "Level", "Years_Used"]],
                )
            )

        for idx, cat in enumerate(categories):
            angle = (idx + 0.5) * span
            fig.add_trace(
                go.Scatterpolar(
                    r=[2.1],
                    theta=[angle],
                    mode="text",
                    text=[f"<b>{cat}</b>"],
                    textfont=dict(size=12, color=color_map[cat], family="IBM Plex Sans"),
                    textposition="middle center",
                    hoverinfo="skip",
                    showlegend=False,
                )
            )

        fig.update_layout(
            height=520,
            margin=dict(l=0, r=0, t=10, b=0),
            polar=dict(
                radialaxis=dict(
                    range=[0, 3.2],
                    tickvals=[0.5, 1.5, 2.5],
                    ticktext=levels,
                    tickfont=dict(size=12, color="#4b5563"),
                    gridcolor="#e5e7eb",
                    linecolor="#d1d5db",
                ),
                angularaxis=dict(
                    showticklabels=False,
                    gridcolor="#f3f4f6",
                    linecolor="#e5e7eb",
                ),
                bgcolor="rgba(0,0,0,0)",
            ),
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No skills match the selected filters.")
