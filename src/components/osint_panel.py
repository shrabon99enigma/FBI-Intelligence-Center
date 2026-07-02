import streamlit as st


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

        st.success("Target Received Successfully.")

        st.write("Target :", target)

        st.write("Scan Type :", scan_type)
        