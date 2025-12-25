from __future__ import annotations

from datetime import datetime
import base64
from pathlib import Path

import altair as alt
import pandas as pd
import plotly.express as px
import streamlit as st

from lib.data import load_resume_data
from lib.style import apply_base_styles

st.set_page_config(
    page_title="Career Overview",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)
apply_base_styles()

st.markdown(
    """
    <style>
    #vg-tooltip-element,
    .vega-tooltip {
        display: block !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    """,
    unsafe_allow_html=True,
)

data = load_resume_data()
exp = data.experience.copy()
lock_path = Path("assets/Hidden.png")
lock_src = ""
if lock_path.exists():
    lock_src = f"data:image/png;base64,{base64.b64encode(lock_path.read_bytes()).decode('utf-8')}"
all_experiences = exp["Experience"].dropna().unique().tolist()

alt.renderers.set_embed_options(actions=False)

exp["End_Date_Filled"] = exp["End_Date"].fillna(pd.Timestamp.today())

min_year = int(exp["Start_Date"].dt.year.min())
max_year = int(exp["End_Date_Filled"].dt.year.max())
range_start_year, range_end_year = st.session_state.get(
    "timeline_years", (min_year, max_year)
)
range_start = datetime(range_start_year, 1, 1)
range_end = datetime(range_end_year, 12, 31)


col_left, col_mid, col_right = st.columns([1.1, 2.8, 1], gap="large")

with col_left:
    st.page_link("Landing Page.py", label="← Landing Page")

with col_mid:
    st.markdown("# Career Overview", text_alignment="center")

exp_view = exp[(exp["Start_Date"] <= range_end) & (exp["End_Date_Filled"] >= range_start)].copy()
exp_view = exp_view.sort_values(["Type", "Start_Date"]).reset_index(drop=True)



if "selected_experience_id" not in st.session_state:
    st.session_state.selected_experience_id = None
selected_id = st.session_state.selected_experience_id

filter_col, top_left, top_right = st.columns([0.7, 3.5, 1], gap="large")

with filter_col:
    st.markdown("<div style='margin-top: 70px;'></div>", unsafe_allow_html=True)
    show_work = st.checkbox("Work", value=True, key="filter_work")
    show_education = st.checkbox("Education", value=True, key="filter_education")

selected_types = []
if show_work:
    selected_types.append("Work")
if show_education:
    selected_types.append("Education")

if selected_types:
    exp_view = exp_view[exp_view["Type"].isin(selected_types)].copy()
else:
    exp_view = exp_view.iloc[0:0].copy()

timeline_select = alt.selection_point(
    name="experience_select",
    fields=["ExperienceID"],
    on="click",
    toggle=True,
    empty="all",
)

timeline_chart = (
    alt.Chart(exp_view)
    .mark_bar(size=50, stroke="#25272c", strokeWidth=1)
    .encode(
        x=alt.X("Start_Date:T", axis=alt.Axis(format="%Y-%m", title=None)),
        x2="End_Date_Filled:T",
        y=alt.Y("Type:N", sort=["Education", "Work"], title=None),
        color=alt.Color(
            "Experience:N",
            legend=alt.Legend(title=None, orient="top", symbolStrokeWidth=1),
            scale=alt.Scale(
                domain=all_experiences,
                range=[
                    "#a71e3bc7",
                    "#e0a808c7",
                    "#87bc25c7",
                    "#1a0dabc7",
                    "#fe8623c7",
                    "#dd2500c7",
                    "#e377c2c7",
                    "#7f7f7fc7",
                    "#bcbd22c7",
                    "#17becfc7",
                ],
            ),
        ),
        opacity=alt.condition(timeline_select, alt.value(1.0), alt.value(0.35)),
        tooltip=[
            alt.Tooltip("Experience:N"),
            alt.Tooltip("Role:N"),
            alt.Tooltip("Start_Date:T", title="Start"),
            alt.Tooltip("End_Date_Filled:T", title="End"),
            alt.Tooltip("Location:N"),
        ],
    )
    .add_params(timeline_select)
    .properties(height=250)
    .configure_view(strokeOpacity=0, fill="#ffffff00")
    .configure_axis(grid=False, domain=False, tickSize=4)
    .configure_legend(labelColor="#000000", titleColor="#000000")
    .configure(background="#ffffff00")
)

with top_left:
    state = st.altair_chart(
        timeline_chart,
        use_container_width=True,
        on_select="rerun",
        selection_mode="experience_select",
    )

if state and "selection" in state and "experience_select" in state.selection:
    selection_state = state.selection["experience_select"]
    selected = None
    if isinstance(selection_state, dict):
        value = selection_state.get("ExperienceID")
        if isinstance(value, list):
            selected = value[0] if value else None
        elif value is not None:
            selected = value
    elif isinstance(selection_state, list):
        if selection_state and isinstance(selection_state[0], dict):
            selected = selection_state[0].get("ExperienceID")

    st.session_state.selected_experience_id = (
        int(selected) if selected is not None else None
    )

selected_id = st.session_state.selected_experience_id
selected_exp = None
active_ids = exp_view["ExperienceID"].dropna().unique().tolist()
if selected_id is not None and selected_id not in active_ids:
    st.session_state.selected_experience_id = None
    selected_id = None
if selected_id is not None:
    selected_exp = exp_view.loc[exp_view["ExperienceID"] == selected_id].head(1)

skills_df = data.skills
certs_df = data.certifications

if active_ids:
    skills_df = skills_df[skills_df["ExperienceID"].isin(active_ids)]
    certs_df = certs_df[certs_df["ExperienceID"].isin(active_ids)]

if selected_id is None:
    skills_count = skills_df["Skill"].nunique()
    certs_count = certs_df["Name"].nunique()
else:
    skills_count = skills_df.loc[skills_df["ExperienceID"] == selected_id, "Skill"].nunique()
    certs_count = certs_df.loc[certs_df["ExperienceID"] == selected_id, "Name"].nunique()

with top_right:
    skills_href = "/Skills"
    certs_href = "/Certifications"
    if selected_id is not None:
        skills_href = f"/Skills?experience_id={selected_id}"
        certs_href = f"/Certifications?experience_id={selected_id}"

    st.markdown(
        f"""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <p class="flip-title">Skills</p>
                    <p class="flip-value">{skills_count}</p>
                </div>
                <div class="flip-card-back">
                    <a class="flip-link" href="{skills_href}" target="_self"><i class="fa-solid fa-magnifying-glass"></i></a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <p class="flip-title">Certifications</p>
                    <p class="flip-value">{certs_count}</p>
                </div>
                <div class="flip-card-back">
                    <a class="flip-link" href="{certs_href}" target="_self"><i class="fa-solid fa-magnifying-glass"></i></a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)

if selected_exp is None or selected_exp.empty:
    st.markdown(
        f"""
        <div class="locked-wrap">
          <div class="locked-layer">
            <div class="locked-card left locked-tip" data-tip="Please select one experience from the timeline above to show more details.">
              <img class="locked-icon" src="{lock_src}" alt="Locked">
            </div>
            <div class="locked-card right locked-tip" data-tip="Please select one experience from the timeline above to show more details.">
              <img class="locked-icon" src="{lock_src}" alt="Locked">
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    row = selected_exp.iloc[0]
    detail_left, detail_right = st.columns([2, 1], gap="large")

    with detail_left:
        st.markdown(f"### {row['Experience']} · {row['Role']}")
        st.markdown(f"**Location:** {row['Location']}")
        st.markdown(row["Description"])
        tasks = str(row.get("Tasks", "")).strip()
        if tasks:
            st.markdown("**Highlights**")
            bullets = [t.strip("▪ ") for t in tasks.split("\n") if t.strip()]
            st.markdown("\n".join([f"- {b}" for b in bullets]))

    with detail_right:
        st.markdown("<div style='margin-top: 68px;'></div>", unsafe_allow_html=True)
        map_df = pd.DataFrame(
            {
                "lat": [row["Latitude"]],
                "lon": [row["Longitude"]],
                "label": [row["Location"]],
            }
        ).dropna()
        if not map_df.empty:
            map_fig = px.scatter_mapbox(
                map_df,
                lat="lat",
                lon="lon",
                hover_name="label",
                zoom=5,
                height=260,
            )
            map_fig.update_layout(
                mapbox_style="carto-positron",
                margin=dict(l=0, r=0, t=0, b=0),
                hovermode="closest",
            )
            map_fig.update_traces(
                marker=dict(size=16, color="#EB7F21", opacity=0.9),
                
            )

            st.plotly_chart(
                map_fig,
                use_container_width=True,
                config={"displayModeBar": False},
            )
