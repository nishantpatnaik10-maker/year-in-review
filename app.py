import streamlit as st

st.set_page_config(page_title="My Year in Review", page_icon="✨", layout="wide")

# ============================================================
# EDIT ME: profile / header info
# ============================================================
PROFILE = {
    "name": "Nishant Patnaik",
    "title": "DemoX Manager APJ",
    "year": "2026",
    "summary": "H1 was quite busy with customer engagements/workshops, demo builds, "
    "recruitment, building brand awareness of DemoX, participating in marketing "
    "events, and also looking at partnerships to have more people on the ground.",
}

# ============================================================
# EDIT ME: each section is a list of entries.
# Add, remove, or edit entries as needed. Fields you don't need
# can be left as an empty string "".
# ============================================================

EVENTS_WORKSHOPS = [
    {
        "title": "Example: Experiential Selling Workshop — [Client/Event Name]",
        "date": "Month 2026",
        "description": "What the event/workshop was and your role in it.",
        "impact": "Outcome or impact (e.g. attendees, deals influenced, feedback).",
    },
    {
        "title": "Example: PegaWorld Demo/Session",
        "date": "Month 2026",
        "description": "Brief description of the session or demo.",
        "impact": "Outcome or impact.",
    },
]

INTERNAL_SELLING = [
    {
        "title": "Example: Internal enablement session for [Team]",
        "date": "Month 2026",
        "description": "What you did to sell an idea, tool, or approach internally.",
        "impact": "Result — adoption, buy-in, follow-on work.",
    },
]

PEOPLE_TEAM_MANAGEMENT = [
    {
        "title": "Example: Mentoring / onboarding [name or team]",
        "date": "Month 2026",
        "description": "What the people/team management activity involved.",
        "impact": "Outcome for the person/team.",
    },
]

RECOGNITIONS = [
    {
        "title": "Pega Praise Recognition #1",
        "date": "",
        "description": "",
        "impact": "",
        "link": "https://pegasystems.rewardgateway.com/SocialRecognition/ViewNomination/cbd748d2-e370-40c1-8d16-e5c95e22c358",
    },
    {
        "title": "Pega Praise Recognition #2",
        "date": "",
        "description": "",
        "impact": "",
        "link": "https://pegasystems.rewardgateway.com/SocialRecognition/ViewNomination/5508cf17-dd7c-4d07-bfd7-679e9094bb23",
    },
    {
        "title": "Pega Praise Recognition #3",
        "date": "",
        "description": "",
        "impact": "",
        "link": "https://pegasystems.rewardgateway.com/SocialRecognition/ViewNomination/98058c3a-7df1-4ea7-bd1d-3ae0d3f57796",
    },
    {
        "title": "Pega Praise Recognition #4",
        "date": "",
        "description": "",
        "impact": "",
        "link": "https://pegasystems.rewardgateway.com/SocialRecognition/ViewNomination/726ad373-d57c-4b1b-8819-a6a7ada2f560",
    },
    {
        "title": "Pega Praise Recognition #5",
        "date": "",
        "description": "",
        "impact": "",
        "link": "https://pegasystems.rewardgateway.com/SocialRecognition/ViewNomination/123d3cb2-ed49-4b56-b0f4-313463a8072c",
    },
    {
        "title": "Pega Praise Recognition #6",
        "date": "",
        "description": "",
        "impact": "",
        "link": "https://pegasystems.rewardgateway.com/SocialRecognition/ViewNomination/0600cf2c-285f-44e3-ac73-9cacdf8fc08d",
    },
]

SECTIONS = {
    "Events / Workshops / Experiential Selling": EVENTS_WORKSHOPS,
    "Internal Selling": INTERNAL_SELLING,
    "People & Team Management": PEOPLE_TEAM_MANAGEMENT,
    "Recognitions": RECOGNITIONS,
}

# ============================================================
# UI
# ============================================================

st.title(f"✨ {PROFILE['name']} — {PROFILE['year']} in Review")
st.subheader(PROFILE["title"])
st.write(PROFILE["summary"])

st.divider()

cols = st.columns(len(SECTIONS))
for col, (name, entries) in zip(cols, SECTIONS.items()):
    col.metric(name, len(entries))

st.divider()

tabs = st.tabs(list(SECTIONS.keys()))

for tab, (section_name, entries) in zip(tabs, SECTIONS.items()):
    with tab:
        if not entries:
            st.info("No entries yet — add some in app.py.")
            continue
        for entry in entries:
            with st.container(border=True):
                header_col, date_col = st.columns([4, 1])
                header_col.markdown(f"**{entry['title']}**")
                if entry.get("date"):
                    date_col.caption(entry["date"])
                if entry.get("description"):
                    st.write(entry["description"])
                if entry.get("impact"):
                    st.caption(f"Impact: {entry['impact']}")
                if entry.get("link"):
                    st.markdown(f"[View details]({entry['link']})")
