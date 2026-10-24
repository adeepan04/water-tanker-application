from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="My Water Tracker",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default padding and chrome so the tracker fills the page.
st.markdown(
    """
    <style>
      #MainMenu, footer, header {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")

# The tracker is a self-contained page. Progress is saved in the visitor's
# own browser (localStorage), so each person sees only their own data.
components.html(html, height=1300, scrolling=True)
