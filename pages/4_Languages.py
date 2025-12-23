from __future__ import annotations

import streamlit as st

from lib.data import load_resume_data
from lib.style import apply_base_styles


st.set_page_config(
    page_title="Languages",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)
apply_base_styles()

data = load_resume_data()
lang = data.languages.copy()

st.markdown("# Languages")

lang = lang.rename(columns={"Language ": "Language"})

cols = st.columns(len(lang), gap="large") if not lang.empty else []
for col, (_, row) in zip(cols, lang.iterrows()):
    with col:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">{row['Language']}</div>
                <div class="kpi-value">{row['Level']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")
st.dataframe(lang, use_container_width=True, hide_index=True)
