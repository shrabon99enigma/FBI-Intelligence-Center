import streamlit as st

from src.config.settings import (
    APP_NAME,
    APP_ICON,
)

from src.components.header import render_header
from src.components.sidebar import render_sidebar
from src.components.mission import render_mission
from src.components.osint_panel import render_osint_panel

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide"
)

render_sidebar()

render_header()

render_mission()

st.header("Operations")

if st.button("Start Scan"):
    st.success("Scan Started Successfully.")

render_osint_panel()