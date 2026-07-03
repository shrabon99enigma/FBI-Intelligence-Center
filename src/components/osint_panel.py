import pandas as pd
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

        if not target.strip():

            st.error("Please enter a target.")

            return

        result = run_scan(target, scan_type)

        st.success("Target Received Successfully.")

        st.write("Target :", result["target"])

        st.write("Scan Type :", result["scan_type"])

        st.write("Status :", result["status"])

        # ----------------------------
        # Debug Output
        # ----------------------------
        st.subheader("Raw Result")
        st.write(result)

        # ----------------------------
        # IP Information
        # ----------------------------
        if scan_type == "IP Intelligence":

            st.subheader("IP Information")

            st.write("IP :", result.get("ip"))

            st.write("City :", result.get("city"))

            st.write("Region :", result.get("region"))

            st.write("Country :", result.get("country"))

            st.write("ISP :", result.get("org"))

            st.write("Timezone :", result.get("timezone"))

        # ----------------------------
        # Location Map
        # ----------------------------
        if (
            result.get("latitude") is not None
            and result.get("longitude") is not None
        ):

            st.subheader("Location")

            st.write("Latitude :", result.get("latitude"))

            st.write("Longitude :", result.get("longitude"))

            location = pd.DataFrame(
                {
                    "lat": [float(result["latitude"])],
                    "lon": [float(result["longitude"])]
                }
            )

            st.write(location)

            st.map(location)

        # ----------------------------
        # Domain Information
        # ----------------------------
        if scan_type == "Domain Intelligence":

            st.subheader("Domain Information")

            st.write("Registrar :", result.get("registrar"))

            st.write("Creation Date :", result.get("creation_date"))

            st.write("Expiration Date :", result.get("expiration_date"))

            st.write("Name Servers :", result.get("name_servers"))