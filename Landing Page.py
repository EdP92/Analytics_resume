import base64
import textwrap
from pathlib import Path

import streamlit as st

from lib.data import load_resume_data
from lib.style import apply_base_styles
from lib.auth import authenticate, logout


st.set_page_config(
    page_title="Landing page",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)
apply_base_styles()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.markdown(
    """
    <style>
    #vg-tooltip-element,
    .vega-tooltip {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

for key in ("selected_experience_id", "experience_select"):
    if key in st.session_state:
        st.session_state.pop(key)

if not st.session_state.authenticated:
    st.markdown(
        """
        <style>
        .login-card {
            background: transparent;
            border-radius: 0;
            padding: 0;
            box-shadow: none;
            max-width: 420px;
            margin: 10px auto 0;
        }
        .login-card hr {
            border: none;
            border-top: 2px solid #d1d5db;
            margin: 10px 0 16px;
        }
        .login-card label {
            font-weight: 600;
            color: #374151;
        }
        .login-card .stForm {
            width: 100%;
        }
        .login-card [data-testid="stTextInput"] {
            width: 100%;
        }
        .login-card [data-testid="stForm"] {
            margin-top: 0;
        }
        .login-card [data-testid="stTextInput"] > div > div {
            background: #f3f4f6;
        }
        .login-card [data-testid="stForm"] small,
        .login-card [data-testid="stTextInput"] small {
            display: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    icon_src = ""
    left, center, right = st.columns([1.2, 0.9, 1.2])
    with center:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown("## Sign In")
        st.markdown("<hr />", unsafe_allow_html=True)
        with st.form("login_form", clear_on_submit=False):
            st.markdown('<div class="login-fields">', unsafe_allow_html=True)
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Sign in")
            st.markdown("</div>", unsafe_allow_html=True)
        if submitted:
            if authenticate(username, password):
                st.success("Welcome back!")
                st.rerun()
            else:
                st.error("Invalid credentials.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

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
    about_left, about_right = st.columns([3, 1], gap="large")

    with about_left:
        st.markdown("## About Me")


    with about_right:
        resume_path = Path("assets/Resume_Edoardo_dalPiaz_2025.pdf")
        if resume_path.exists():
            resume_b64 = base64.b64encode(resume_path.read_bytes()).decode("utf-8")
            st.markdown(
                f"""
                <div style="margin-top: -83px; margin-right: 40px; display: flex; justify-content: flex-end;">
                  <a class="download-button" href="data:application/pdf;base64,{resume_b64}" download="Resume_Edoardo_dalPiaz_2025.pdf">
                    <div class="docs">
                      <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10 9 9 9 8 9"></polyline>
                      </svg>
                      PDF 
                    </div>
                    <div class="download">
                      <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="7 10 12 15 17 10"></polyline>
                        <line x1="12" y1="15" x2="12" y2="3"></line>
                      </svg>
                    </div>
                  </a>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.caption("Add `assets/Resume_Edoardo_dalPiaz_2025.pdf` to enable download.")
    
    st.markdown(
        """
        <div style="font-size: 1.125rem; line-height: 1.7;">
          <p>Passionate Data Engineer with a strong foundation in finance, focused on transforming complex data into reliable, actionable insights for decision-making. I design scalable, analytics-ready data architectures and foster collaboration between technical teams and business stakeholders.</p>
          <p>My experience spans data engineering, analytics engineering, and consulting roles across international environments, delivering end-to-end solutions from ingestion to visualization. I emphasize data quality, maintainability, and performance so analytics stay trustworthy and scalable.</p>
          <p>Beyond delivery, I act as a bridge between technical teams and non-technical stakeholders, aligning data initiatives with real business outcomes. I enjoy refining data models, experimenting with new tools, improving analytics workflows, and enabling self-service analytics.</p>
        </div>
        """,
        unsafe_allow_html=True,
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
