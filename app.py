import streamlit as st

st.set_page_config(page_title="My Year in Review", page_icon="✨", layout="wide")

# ============================================================
# EDIT ME: profile / header info
# ============================================================
PROFILE = {
    "name": "Your Name",
    "title": "Your Role / Title",
    "year": "2026",
    "summary": "A short one or two sentence summary of your year — the focus areas, "
    "themes, or highlights you want people to take away first.",
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
        "title": "Example: Recognition/award name",
        "date": "Month 2026",
        "description": "Who gave it and why.",
        "impact": "",
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
