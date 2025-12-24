from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "Resume_for_analytics_v4.xlsx"


@dataclass
class ResumeData:
    experience: pd.DataFrame
    skills: pd.DataFrame
    certifications: pd.DataFrame
    languages: pd.DataFrame
    calendar: pd.DataFrame


def _clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    keep_cols = []
    for col in df.columns:
        if col is None:
            continue
        col_str = str(col).strip()
        if not col_str or col_str.startswith("Unnamed"):
            continue
        keep_cols.append(col)
    return df.loc[:, keep_cols]


def _excel_date(series: pd.Series) -> pd.Series:
    if pd.api.types.is_datetime64_any_dtype(series):
        return pd.to_datetime(series, errors="coerce")
    series_num = pd.to_numeric(series, errors="coerce")
    return pd.to_datetime(series_num, unit="D", origin="1899-12-30", errors="coerce")


@st.cache_data
def load_resume_data() -> ResumeData:
    xls = pd.ExcelFile(DATA_PATH)
    experience = pd.read_excel(xls, "Experience")
    skills = pd.read_excel(xls, "Skills")
    certifications = pd.read_excel(xls, "Certifications")
    languages = pd.read_excel(xls, "Languages")
    calendar = pd.read_excel(xls, "Calendar")

    experience = _clean_columns(experience)
    skills = _clean_columns(skills)
    certifications = _clean_columns(certifications)
    languages = _clean_columns(languages)
    calendar = _clean_columns(calendar)

    experience["ExperienceID"] = pd.to_numeric(experience["ExperienceID"], errors="coerce").astype("Int64")
    experience["Start_Date"] = _excel_date(experience["Start_Month"])
    experience["End_Date"] = _excel_date(experience["End_Month"])
    experience["Latitude"] = pd.to_numeric(experience["Latitude"], errors="coerce")
    experience["Longitude"] = pd.to_numeric(experience["Longitude"], errors="coerce")

    skills["ExperienceID"] = pd.to_numeric(skills["ExperienceID"], errors="coerce").astype("Int64")
    skills["Years_Used"] = pd.to_numeric(skills["Years_Used"], errors="coerce")

    certifications["ExperienceID"] = pd.to_numeric(certifications["ExperienceID"], errors="coerce").astype("Int64")

    return ResumeData(
        experience=experience,
        skills=skills,
        certifications=certifications,
        languages=languages,
        calendar=calendar,
    )
