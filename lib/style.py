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

        html, body {
            background: transparent !important;
        }

        .stApp {
            background: transparent !important;
        }

        .stApp > div {
            position: relative;
            z-index: 1;
        }


        h1, h2, h3, h4, h5, h6 {
            font-family: 'Space Grotesk', 'Segoe UI', sans-serif;
            letter-spacing: -0.02em;
            color: var(--ink-1);
            margin: 0 0 0.6rem 0;
        }

        h3 {
            margin-bottom: 0.45rem;
        }

        p, ul, ol {
            margin: 0 0 0.8rem 0;
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
            box-shadow: 0 16px 24px 0 rgba(0, 0, 0, 0.2);
            position: absolute;
            display: flex;
            flex-direction: column;
            justify-content: center;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border: 1px solid #cbd5f5;
            border-radius: 1rem;
        }

        .flip-card-front {
            background: linear-gradient(
                120deg,
                #f8fafc 55%,
                #ffffff 85%,
                #e5e7eb 40%,
                rgba(209, 213, 219, 0.6) 48%
            );
            color: #111827;
        }

        .flip-card-back {
            background: linear-gradient(
                120deg,
                #9ca3af 25%,
                #878d99 85%,
                #e5e7eb 40%,
                #9ca3af 78%
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
            width: 270px;
            height: 150px;
            margin: 0 auto;
            background-color: #f4f4f3;
            border-radius: 8px;
            z-index: 1;
            position: relative;
            display: flex;
            flex-direction: column;
        }

        .info-card::after {
            position: absolute;
            content: '';
            background-color: #454a50;
            width: 50px;
            height: 100px;
            z-index: -1;
            border-radius: 8px;
        }

        .info-card .tools {
            display: flex;
            align-items: center;
            padding: 9px;
            border-radius: 8px;
            background: #454a50;
            margin-top: -30px;
        }

        .info-card .circle {
            padding: 0 4px;
        }

        .info-card .card__content {
            height: 100%;
            margin: 0px;
            border-radius: 8px;
            background: #f4f4f3;
            padding: 10px;
        }

        .info-card .title {
            font-size: 20px;
            font-weight: 700;
            margin: 0;
        }

        .info-card .content {
            margin-top: -20px;
            font-size: 14px;
            color: #111111;
        }

        .info-card .box {
            display: inline-block;
            align-items: center;
            width: 10px;
            height: 10px;
            padding: 1px;
            border-radius: 50%;
        }

        .info-card .red {
            background-color: #ff605c;
        }

        .info-card .yellow {
            background-color: #ffbd44;
        }

        .info-card .green {
            background-color: #00ca4e;
        }

        .locked-wrap {
            position: relative;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 220px;
        }

        .locked-layer {
            position: absolute;
            display: flex;
            gap: 22px;
            z-index: 0;
            opacity: 0.45;
            filter: blur(0.2px);
            width: 100%;
            justify-content: center;
            transform: translateY(66px);
        }

        .locked-card {
            height: 300px;
            border-radius: 18px;
            background: linear-gradient(145deg, #f1f5f950, #e2e8f050);
            box-shadow: 0 30px 35px rgba(15, 23, 42, 0.32);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        .locked-card:hover {
            transform: scale(1.03);
            box-shadow: 0 32px 38px rgba(15, 23, 42, 0.36);
        }

        .locked-tip {
            position: relative;
        }

        .locked-tip::after {
            content: attr(data-tip);
            position: absolute;
            left: 50%;
            bottom: 60%;
            transform: translate(-50%, -12px);
            background: #111827;
            color: #f9fafb;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.95rem;
            line-height: 1.2;
            text-align: center;
            width: max-content;
            max-width: 220px;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.2s ease, transform 0.2s ease;
            z-index: 3;
            box-shadow: 0 12px 20px rgba(15, 23, 42, 0.18);
        }

        .locked-tip:hover::after {
            opacity: 1;
            transform: translate(-50%, -16px);
        }

        .locked-card.left {
            width: 66.7%;
        }

        .locked-card.right {
            width: 33.3%;
        }

        .locked-icon {
            width: 72px;
            height: 72px;
            opacity: 0.35;
        }

        .locked-front {
            position: relative;
            z-index: 1;
        }

        header[data-testid="stHeader"] {
            background: transparent;
            box-shadow: none;
        }

        .stButton > button {
            --b: 3px;
            --s: 0.45em;
            --color: #373B44;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: calc(0.4em + var(--s)) calc(2.3em + var(--s));
            color: var(--color);
            font-size: 16px;
            font-weight: 600;
            text-decoration: none;
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
            border: 0;
            border-radius: 0;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            white-space: nowrap;
        }

        .stButton > button:hover,
        .stButton > button:focus-visible {
            --_p: 0px;
            outline-color: var(--color);
            outline-offset: 0.05em;
        }

        .stButton > button:active {
            background: var(--color);
            color: #fff;
        }

        .stButton > button * {
            color: inherit !important;
        }

        .icon-clear .stButton > button {
            --b: 2px;
            --s: 0.2em;
            width: 30px;
            height: 30px;
            min-width: 30px;
            padding: 0;
            font-size: 20px;
            line-height: 1;
            font-weight: 700;
            color: #7f1d1d;
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

        .download-button {
            position: relative;
            border-width: 0;
            color: white;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            border-radius: 4px;
            z-index: 1;
            display: inline-block;
            text-decoration: none;
        }

        .download-button .docs {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            min-height: 40px;
            padding: 0 10px;
            border-radius: 4px;
            z-index: 1;
            background-color: #ffffff;
            border: solid 1px #111111;
            transition: all 0.5s cubic-bezier(0.77, 0, 0.175, 1);
        }

        .download-button:hover {
            box-shadow:
                rgba(0, 0, 0, 0.25) 0px 54px 55px,
                rgba(0, 0, 0, 0.12) 0px -12px 30px,
                rgba(0, 0, 0, 0.12) 0px 4px 6px,
                rgba(0, 0, 0, 0.17) 0px 12px 13px,
                rgba(0, 0, 0, 0.09) 0px -3px 5px;
        }

        .download {
            position: absolute;
            inset: 5% 0;
            display: flex;
            align-items: center;
            justify-content: center;
            max-width: 90%;
            margin: 0 auto;
            z-index: -1;
            border-radius: 4px;
            transform: translateY(0%);
            background-color: #01e056;
            border: solid 1px #01e0572d;
            transition: all 0.5s cubic-bezier(0.77, 0, 0.175, 1);
            color: #ffffff;
        }

        .download-button:hover .download {
            transform: translateY(100%);
        }

        .download svg polyline,
        .download svg line {
            animation: docs 1s infinite;
        }

        @keyframes docs {
            0% {
                transform: translateY(0%);
            }

            50% {
                transform: translateY(-15%);
            }

            100% {
                transform: translateY(0%);
            }
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
