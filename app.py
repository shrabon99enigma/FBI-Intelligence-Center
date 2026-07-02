import streamlit as st
from src.config.settings import (
    APP_NAME,
    APP_ICON,
    APP_DESCRIPTION
)
st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide"
)

st.title(f"{APP_ICON} {APP_NAME}")

st.caption(APP_DESCRIPTION)

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
    st.divider()

st.header("OSINT Search Panel")

target = st.text_input(
    "Target",
    placeholder="Enter domain, IP, email, username..."
)

scan_type = st.selectbox(
    "Scan Type",
    [
        "Domain Intelligence",
        "IP Intelligence",
        "Email Intelligence",
        "Username Intelligence"
    ]
)

if st.button("Run Intelligence"):

    st.success("Target Received Successfully.")

    st.write("Target :", target)

    st.write("Scan Type :", scan_type)