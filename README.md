# Analytics Resume Dashboard

A custom, interactive CV built with Streamlit. The goal is to replace Tableau with a fully‑custom web app that runs locally (or can be deployed) and lets you explore career history, skills, and certifications through an analytics‑style experience.

## What’s implemented

- **Landing Page**
  - Profile photo, contact links, and about text.
  - Right column sections for skills, technical domains, soft skills, languages, and interests.
  - Animated network‑style background (canvas).

- **Career Overview**
  - Timeline chart (Altair) of work/education with click‑to‑select.
  - Filters for experience type (Work/Education).
  - Detail panel with description and map.
  - KPI cards (Skills / Certifications) as flip cards with hover effect.

- **Skills / Certifications Pages**
  - Filterable detail tables.
  - Summary charts (bar/pie).

- **Languages Page**
  - Simple cards/table view.

## Data model

The app currently reads from:
- `Resume_for_analytics_v4.xlsx` (Experience, Skills, Certifications, Languages, Calendar)

Experience is treated as the fact table; Skills/Certifications are dimensions. Languages are standalone for now.

## How to run

1) Create and activate a virtualenv:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install deps:

```bash
pip install -r requirements.txt
```

3) Launch:

```bash
streamlit run "Landing Page.py"
```

## Project structure

```
.
├─ Landing Page.py
├─ pages/
│  ├─ 1_Career_Overview.py
│  ├─ 2_Skills.py
│  └─ 3_Certifications.py
├─ lib/
│  ├─ background.py
│  ├─ data.py
│  └─ style.py
├─ assets/
│  └─ DalPiaz_Edoardo_2.jpg
├─ Resume_for_analytics_v4.xlsx
└─ requirements.txt
```

## Notes / current UX

- Timeline colors are fixed to avoid reshuffling when filters change.
- Click a bar in the timeline to populate the detail panel.
- Flip cards link to the Skills/Certifications pages.

## Next ideas

- Replace the standard checkboxes with a fully custom UI (if desired).
- More polished navigation and page transitions.
- Add additional “deep dive” pages (projects, tools, education details).
- Optional deploy config (Streamlit Cloud / private hosting).

---

If you want changes to the README tone, structure, or more screenshots, just say the word.
