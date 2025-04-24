import streamlit as st

pages = {
    "YouTube": [
        st.Page("route/download.py", title="Download"),
        st.Page("route/search.py", title="Search"),
        # st.Page("trial.py", title="Try it out"),
    ],
    # "Thank You For Coming": [
    #     st.Page("route/feedback.py", title="Feedback")
    # ],
    # "Campaign": [
    #     st.Page("route/vote.py", title="Vote your Candidate"),
    #     st.Page("route/stats.py", title="Campaign Statistics"),
    #     st.Page("route/support.py", title="Support your Candidate"),
    # ],
}

pg = st.navigation(pages, expanded=True)
pg.run()

# st.logo("assets/favicon.png")