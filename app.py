import streamlit as st

st.set_page_config(
    page_title="FBI Intelligence Center",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ FBI Intelligence Center")

st.caption("Professional OSINT • Cyber Intelligence • Investigation Platform")

st.divider()

st.header("Mission Control")

st.write(
    """
Welcome to the FBI Intelligence Center.

This project is being built to learn professional Python development,
Streamlit, Git, GitHub, OSINT, automation, and software engineering
through a real-world application.
"""
)

st.info("Project Status: Under Development")
st.divider()

st.header("Operations")

if st.button("Start Scan"):
    st.success("Scan Started Successfully.")