import streamlit as st

from src.services.osint_service import run_scan


def render_osint_panel():

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

        result = run_scan(target, scan_type)

        st.success("Target Received Successfully.")

        st.write("Target :", result["target"])

        st.write("Scan Type :", result["scan_type"])

        st.write("Status :", result["status"])