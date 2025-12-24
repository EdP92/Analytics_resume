import streamlit as st


def apply_base_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=IBM+Plex+Sans:wght@300;400;500&display=swap');

        :root {
            --bg-1: #ffeaa6;
            --bg-2: #f8faf6;
            --ink-1: #111111;
            --ink-2: #5a5a5a;
            --ink-3: #9ca3af;
            --accent: #d97706;
            --accent-2: #2563eb;
            --card: #ffffff;
            --shadow: 0 20px 50px rgba(17, 17, 17, 0.08);
        }

        html, body, [class*="css"]  {
            font-family: 'IBM Plex Sans', 'Segoe UI', sans-serif;
            color: var(--ink-3);
        }

        body, p, span, div, li, a, label {
            color: var(--ink-1);
        }

        .stApp {
            background: radial-gradient(circle at top left, var(--bg-2), var(--bg-1));
        }

        .stApp > div {
            position: relative;
            z-index: 1;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Space Grotesk', 'Segoe UI', sans-serif;
            letter-spacing: -0.02em;
            color: var(--ink-1);
        }

        .hero-card {
            background: var(--card);
            border-radius: 24px;
            padding: 32px;
            box-shadow: var(--shadow);
            color: var(--ink-1);
        }

        .block-container {
            padding-top: 0.5rem;
        }

        .hero-card * {
            color: var(--ink-1);
        }

        .pill {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 999px;
            background: rgba(217, 119, 6, 0.12);
            color: var(--accent);
            font-size: 0.85rem;
            font-weight: 600;
            margin-right: 8px;
        }

        .contact-link {
            text-decoration: none;
            color: var(--accent-2);
        }


        .kpi-card {
            background: var(--card);
            border-radius: 18px;
            padding: 20px 22px;
            box-shadow: var(--shadow);
            text-align: center;
        }

        .kpi-label {
            font-size: 0.9rem;
            color: var(--ink-2);
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .kpi-value {
            font-size: 2.4rem;
            font-weight: 700;
            color: var(--accent-2);
            margin-top: 6px;
        }

        .kpi-card.compact {
            padding: 14px 16px;
        }

        .kpi-card.compact .kpi-label {
            font-size: 0.75rem;
        }

        .kpi-card.compact .kpi-value {
            font-size: 2rem;
        }

        .flip-card {
            background-color: transparent;
            width: 90%;
            height: 144px;
            perspective: 1000px;
            font-family: 'IBM Plex Sans', sans-serif;
            margin-bottom: 16px;
        }

        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.8s;
            transform-style: preserve-3d;
        }

        .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg);
        }

        .flip-card-front,
        .flip-card-back {
            box-shadow: 0 8px 14px 0 rgba(0, 0, 0, 0.2);
            position: absolute;
            display: flex;
            flex-direction: column;
            justify-content: center;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border: 1px solid #fb923c;
            border-radius: 1rem;
        }

        .flip-card-front {
            background: linear-gradient(
                120deg,
                #fef3c7 60%,
                #fff7ed 88%,
                #fed7aa 40%,
                rgba(251, 146, 60, 0.5) 48%
            );
            color: #ea580c;
        }

        .flip-card-back {
            background: linear-gradient(
                120deg,
                #fdba74 30%,
                #fb923c 88%,
                #fef3c7 40%,
                #fdba74 78%
            );
            color: #ffffff;
            transform: rotateY(180deg);
        }

        .flip-title {
            font-size: 20px !important;
            font-weight: 700;
            margin: 0;
        }

        .flip-value {
            font-size: 36px !important;
            font-weight: 1000 !important;
            margin: 0.2rem 0 0;
        }

        .flip-link {
            color: #ffffff;
            text-decoration: none;
            font-weight: 700;
        }

        .flip-link i {
            font-size: 3.2rem;
            color: #e5e7eb;
        }

        .info-card {
            width: 190px;
            height: 200px;
            margin: 0 auto;
            background: rgb(236, 236, 236);
            box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px,
                rgba(0, 0, 0, 0.3) 0px 7px 13px -3px,
                rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
        }

        .info-card .card__content {
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 16px;
            font-weight: 600;
            color: #111111;
        }

        header[data-testid="stHeader"] {
            background: transparent;
            box-shadow: none;
        }

        .stButton > button {
            background: #ffffff;
            color: #111827;
            border: 1px solid #d1d5db;
        }

        .stButton > button:hover {
            background: #f3f4f6;
            color: #111827;
            border-color: #9ca3af;
        }

        .stButton > button * {
            color: #111827 !important;
        }


        span:has(+input[type="checkbox"]) {
            background-color: #e5e7eb !important;
        }

        span:has(+input[type="checkbox"]:checked) {
            background-color: #374151 !important;
            border: 2px solid #000000 !important;
        }

        .stPlotlyChart,
        .stPlotlyChart > div,
        .stPlotlyChart > div > div {
            background: transparent !important;
        }

        .stPlotlyChart {
            border: 3px solid #9ca3af;
            border-radius: 4px;
        }

        div[data-testid="stComponent"] iframe {
            background: #f8faf6 !important;
            border: 0 !important;
            outline: 0 !important;
            box-shadow: none !important;
        }

        div[data-testid="stComponent"] {
            background: transparent !important;
            border: 0 !important;
            outline: 0 !important;
            box-shadow: none !important;
            padding: 0 !important;
        }

        .vega-embed text {
            fill: #000000 !important;
        }

        .vega-embed .mark-text text {
            fill: #000000 !important;
        }

        .vega-embed .axis text {
            fill: #000000 !important;
        }

        .vega-embed .legend text {
            fill: #000000 !important;
        }


        .name-small {
            font-size: 1.6rem;
            margin-bottom: 0.3rem;
        }

        .surname-large {
            font-size: 3.2rem;
            font-weight: 700;
            line-height: 1.05;
            margin-bottom: 1.5rem;
        }

        .profile-photo img {
            border-radius: 50%;
            object-fit: cover;
            width: 175px;
            height: 175px;
            transform: scale(1.15);
            transform-origin: center;
        }

        .profile-photo {
            margin-bottom: 14px;
        }

        .section-title {
            font-size: 1.2rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin: 0 0 0.6rem 0;
        }

        .section-sub {
            font-weight: 600;
            margin: 0.8rem 0 0.4rem 0;
        }

        .scale-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: -5px;
        }

        .scale-label {
            flex: 1;
        }

        .scale-dots {
            display: flex;
            gap: 3px;
        }

        .dot {
            width: 14px;
            height: 14px;
            border-radius: 20px;
            border: 2px solid #1f2937;
            background: transparent;
        }

        .dot.filled {
            background: #5b5b5c;
        }

        .text-block {
            margin: 0 0 0.6rem 0;
            font-size: 0.9rem;
        }

        /* Streamlit page_link styled like "button-89" */
        div[data-testid="stPageLink"] a {
        /* Button-89 variables */
        --b: 3px;          /* border thickness */
        --s: 0.45em;       /* size of the corner */
        --color: #373B44;  /* main color */

        display: inline-flex;
        align-items: center;
        justify-content: center;

        padding: calc(0.4em + var(--s)) calc(2.3em + var(--s));
        color: var(--color) !important;
        font-size: 16px;
        font-weight: 600;
        text-decoration: none !important;

        /* the border illusion */
        --_p: var(--s);
        background:
            conic-gradient(from 90deg at var(--b) var(--b),
            #0000 90deg,
            var(--color) 0)
            var(--_p) var(--_p) /
            calc(100% - var(--b) - 2 * var(--_p))
            calc(100% - var(--b) - 2 * var(--_p));

        transition: 0.3s linear, color 0s, background-color 0s;

        outline: var(--b) solid #0000;
        outline-offset: 0.6em;

        border: 0 !important;
        border-radius: 0; /* keep the sharp-corner style */

        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;

        /* optional: nicer spacing if link stretches */
        white-space: nowrap;

        }

        /* Ensure Streamlit's nested label elements inherit styles */
        div[data-testid="stPageLink"] a * {
        color: inherit !important;
        fill: currentColor !important;
        font-size: inherit !important;
        text-decoration: none !important;
        font-weight: inherit !important;
        }

        /* Hover / keyboard focus */
        div[data-testid="stPageLink"] a:hover,
        div[data-testid="stPageLink"] a:focus-visible {
        --_p: 0px;
        outline-color: var(--color);
        outline-offset: 0.05em;
        }

        /* Active (mouse down) */
        div[data-testid="stPageLink"] a:active {
        background: var(--color);
        color: #fff !important;
        }

        /* Optional: remove default focus outline in some browsers */
        div[data-testid="stPageLink"] a:focus {
        text-decoration: none !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
