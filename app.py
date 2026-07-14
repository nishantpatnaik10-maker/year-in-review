import streamlit as st

st.set_page_config(page_title="My Year in Review", page_icon="✨", layout="wide")

# ============================================================
# EDIT ME: profile / header info
# ============================================================
PROFILE = {
    "name": "Nishant Patnaik",
    "title": "DemoX Manager APJ",
    "year": "2026",
    "summary": "H1 2026 was anchored by hands-on workshops and experiential selling with "
    "BUPA, CBA, Telstra, and National Archives of Australia, alongside internal enablement "
    "through bootcamps, GTM overviews, and rebranded PW Simulation assets. I also grew the "
    "team by hiring the first batch of DemoX Live Solution Consultants while mentoring the "
    "existing team, delivered three customer builds, and was recognized six times through "
    "Pega Praise for the impact of this work.",
}

# ============================================================
# EDIT ME: each section is a list of entries.
# Add, remove, or edit entries as needed. Fields you don't need
# can be left as an empty string "".
# ============================================================

EVENTS_WORKSHOPS = [
    {
        "title": "BUPA AI Learning Week",
        "date": "February 2026",
        "description": "Sharing the floor with other vendors to showcase our product offerings and blueprint.",
        "impact": "Attendees were impressed with the Platform blueprint as well as Customer Engagement blueprint.",
    },
    {
        "title": "Pega Innovate - Sydney",
        "date": "March 2026",
        "description": "An annual marketing event, where we have booths showcasing our product offerings to our partners, customers and prospects. Set up booths for Customer Service and Back Office simulations, also rented equipment for it.",
        "impact": "A lot of customers tried out the experiences and were impressed with how we had gamified the feature functions. Great chats around adopting some of the feature functions with customers.",
    },
    {
        "title": "BUPA Modernization Workshop",
        "date": "April 2026",
        "description": "In the modernization program we showed how using Pega's case management, Gen AI and Agentic capabilities, BUPA can reduce the manual tasks, process claims in a timely manner with complete auditability and traceability.",
        "impact": "Got an opportunity to do a more detailed workshop and also a POC to gauge the Doc Agent capabilities.",
    },
    {
        "title": "CBA Hands-on Workshop",
        "date": "May 2026",
        "description": "Getting CBA's architects and engineers hands-on with Pega blueprint and Pega's agentic and Generative AI capabilities across two locations, Sydney and Bengaluru.",
        "impact": "There were great conversations again; they were impressed to see the latest and greatest in Pega, and were happy to take their learnings and sell them internally.",
    },
    {
        "title": "Telstra Experiential Workshop",
        "date": "June 2026",
        "description": "After doing a Blueprint workshop with them and defining a hi-fidelity blueprint, we used the experiential assets and integration with Salesforce to showcase how we can not only improve the customer experience but also how we can enable the customer to do more on their own. We also showed how we can integrate with their microservices and some of our agentic capabilities.",
        "impact": "The execs liked it and wanted us to do the same presentation to other key stakeholders in Telstra.",
    },
    {
        "title": "National Archives of Australia",
        "date": "June 2026",
        "description": "Showed the customer our experiential assets after demonstrating our Blueprint capabilities.",
        "impact": "There was great engagement from the customers.",
    },
]

INTERNAL_SELLING = [
    {
        "title": "Test Drive Bootcamp - APJ",
        "date": "May 2026",
        "description": "Presented in the bootcamps across three regions AUS/NZ, Asia & Japan about the experiential assets and how it can help in the selling motion.",
        "impact": "There was immediate adoption, and a lot of requests to provision experiential assets have been trickling in.",
    },
    {
        "title": "GTM Product Overview and BP/1:1 CE BP Overview",
        "date": "Every month",
        "description": "A great opportunity to introduce DemoX's product offerings to newbies in their early days at Pega.",
        "impact": "Immediate understanding of when to partner with DemoX.",
    },
]

PEOPLE_TEAM_MANAGEMENT = [
    {
        "title": "Hiring first batch of DemoX Live Solution Consultants",
        "date": "May/June 2026",
        "description": "Scouting and being part of the interview process to select the new team members.",
        "impact": "These new team members would help in spreading the brand awareness of DemoX across the region as well as more customer engagement hours from a DemoX perspective.",
    },
    {
        "title": "Continuous mentoring of the current team",
        "date": "All months 2026",
        "description": "Mentoring the current team members, regular 1:1s, bringing the team together in team meetings.",
        "impact": "To help them to deliver their best in the field and also make sure they are up to date with the latest and greatest.",
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

CUSTOMER_BUILDS = [
    "O-2513293 - Small Business Connect",
    "O-3101277 - BOQ - Agentic AI expansion into lending and complex servicing process",
    "O-2506349 - DTP SPP Renewal",
]

INTERNAL_DEMOX_OPERATIONS = [
    "Led and completed rebranding of PW Simulation experiences, so that these can be used across multiple customer events.",
    "Presented in tech talk sessions and shared experiences of customer engagements.",
]

SECTIONS = {
    "Events / Workshops / Experiential Selling": EVENTS_WORKSHOPS,
    "Internal Selling": INTERNAL_SELLING,
    "People & Team Management": PEOPLE_TEAM_MANAGEMENT,
    "Recognitions": RECOGNITIONS,
    "Customer Builds": CUSTOMER_BUILDS,
    "Internal DemoX Operations": INTERNAL_DEMOX_OPERATIONS,
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
            if isinstance(entry, str):
                st.markdown(f"- {entry}")
                continue
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
