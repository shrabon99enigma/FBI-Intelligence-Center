import streamlit as st

from src.config.settings import (
    APP_NAME,
    APP_ICON,
    APP_DESCRIPTION
)


def render_header():

    st.title(f"{APP_ICON} {APP_NAME}")

    st.caption(APP_DESCRIPTION)

    st.divider()