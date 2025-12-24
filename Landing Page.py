import base64
import textwrap
from pathlib import Path

import streamlit as st

from lib.background import render_network_background
from lib.data import load_resume_data
from lib.style import apply_base_styles


st.set_page_config(
    page_title="Landing page",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)
apply_base_styles()
render_network_background()

st.title("My Analytics Resume", text_alignment="center")

st.markdown(
    """
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    """,
    unsafe_allow_html=True
)

_ = load_resume_data()

def render_scale(items, max_level=5):
    rows = []
    for name, level in items:
        dots = "".join(
            f'<span class="dot{" filled" if i < level else ""}"></span>'
            for i in range(max_level)
        )
        rows.append(
            textwrap.dedent(
                f"""
                <div class="scale-row">
                    <div class="scale-label">{name}</div>
                    <div class="scale-dots">{dots}</div>
                </div>
                """
            ).strip()
        )
    return "\n".join(rows)


col_left, col_mid, col_right = st.columns([1.1, 2.8, 1], gap="large")

with col_left:
    
    photo_path = Path("assets/DalPiaz_Edoardo_2.jpg")
    if photo_path.exists():
        encoded = base64.b64encode(photo_path.read_bytes()).decode("utf-8")
        st.markdown(
            f"""
            <div class="profile-photo">
                <img src="data:image/jpeg;base64,{encoded}" width="150" height="150" />
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.caption("Add `assets/DalPiaz_Edoardo_2.jpg` to show your photo.")

    st.markdown(
        """
        <div style="padding-top: 16px;">
            <div class="name-small"><strong>Edoardo</strong></div>
            <div class="surname-large">dal Piaz</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div>
            <p>
                <i class="fa-solid fa-location-dot" style="margin-right: 4px; color: #000000;"></i>
                    <strong>València, Spain</strong>
                </a>
            </p>
            <p>
                <i class="fa-solid fa-mobile" style="margin-right: 8px; color: #000000;"></i>
                <a class="contact-link" href="tel:+34658661865">
                    +34 658 661 865
                </a>
            </p>
            <p>
                <i class="fa-solid fa-envelope" style="margin-right: 8px; color: #000000;"></i>
                <a class="contact-link" href="mailto:edoardo.dalpiaz@gmail.com">edoardo.dalpiaz@gmail.com</a>
            </p>
            <p>
                <i class="fa-brands fa-linkedin-in" style="margin-right: 8px; color: #000000;"></i>
                <a class="contact-link" href="https://www.linkedin.com/in/edoardo-dal-piaz/" target="_blank">linkedin.com/in/edoardo-dal-piaz/</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    languages = [
        ("Italian", 5),
        ("English", 4),
        ("Spanish", 4),
        ("French", 3),
    ]

    st.markdown('<hr style="border: none; border-top: 1px solid #d1d5db; margin: 16px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Languages</div>', unsafe_allow_html=True)
    st.markdown(render_scale(languages), unsafe_allow_html=True)


with col_mid:
    st.markdown("## About Me")
    st.markdown(
        """
		Passionate Data Engineer with a strong foundation in finance, focused on transforming complex data into reliable and actionable insights to support strategic decision-making. I specialize in designing scalable, analytics-ready data architectures and foster collaboration between technical teams and business stakeholders.

		My experience spans data engineering, analytics engineering, and consulting roles across international environments, delivering end-to-end solutions from ingestion to visualization. I place strong emphasis on data quality, maintainability, and performance, ensuring that downstream analytics remain trustworthy and scalable.

		Beyond hands-on delivery, I act as a bridge between technical teams and non-technical stakeholders, helping align data initiatives with real business outcomes. I have contributed to both small, agile teams and larger, more structured data organizations, gaining perspective on different operating models and team dynamics.

		Curious by nature, I am driven by continuous learning and knowledge sharing. I enjoy refining data models, experimenting with new tools, improving analytics workflows, and enabling self-service analytics. Over time, my goal is to combine deep technical expertise with ownership, mentorship, and strategic thinking to help organizations fully realize the value of their data.
        """
    )
    
    st.markdown("<div style='padding-top: 25px;'></div>", unsafe_allow_html=True)

    inner_left, inner_center, inner_right = st.columns([1, 1, 1])

    with inner_center:        
        st.page_link("pages/1_Career_Overview.py", label="Career Overview →")



with col_right:
    programming = [
        ("Python", 5),
        ("SQL", 5),
        ("DAX", 4),
        ("HTML/CSS", 3),
        ("MATLAB", 2),
        ("VBA", 2),
    ]

    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Programming Languages</div>', unsafe_allow_html=True)
    st.markdown(render_scale(programming), unsafe_allow_html=True)

    st.markdown('<div class="section-sub">Technical Skills</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="text-block"><strong>Cloud & Orchestration:</strong> MS Azure (Synapse, Data Factory), GCP (BigQuery, Airflow), AWS (Comprehend, SageMaker)</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="text-block"><strong>Data & Analytics:</strong> Qlik Sense, Looker, Power BI, SSIS, Tabular Editor, dbt, SAP HANA, PostgreSQL, MySQL, Oracle</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="text-block"><strong>Development & Tools:</strong> GitHub, GitLab, Azure DevOps, PyCharm, Jupyter, VS/VS Code, Postman, SSMS</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-sub">Soft Skills</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="text-block">Analytical mindset, Problem-solving, Team collaboration, Proactive attitude</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<hr style="border: none; border-top: 1px solid #d1d5db; margin: 16px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Interests</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="text-block">Finance & trading, Reading, Traveling, Languages, Sports & wellbeing</div>',
        unsafe_allow_html=True,
    )
