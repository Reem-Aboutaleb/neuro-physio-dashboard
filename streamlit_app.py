import streamlit as st
from app import PPG

PAGES = {
    "PPG Signal": PPG
}

st.sidebar.title("🧭 Navigation")
selection = st.sidebar.radio("Choose a section:", list(PAGES.keys()))
page = PAGES[selection]
page.app()
