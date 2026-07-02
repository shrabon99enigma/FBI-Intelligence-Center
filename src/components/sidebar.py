import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🛰️ Navigation")

        st.divider()

        st.button("🏠 Dashboard")

        st.markdown("### Intelligence")

        st.button("🌐 Domain Intelligence")

        st.button("🌍 IP Intelligence")

        st.button("📧 Email Intelligence")

        st.button("👤 Username Intelligence")

        st.divider()

        st.markdown("### System")

        st.button("📁 Reports")

        st.button("⚙ Settings")