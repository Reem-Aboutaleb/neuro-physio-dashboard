import streamlit as st
from app import PPG, Peaks  # 👈 Add Peaks here

PAGES = {
    "PPG Signal": PPG,
    "PPG + Peak Detection": Peaks  # 👈 Add this line
}

st.sidebar.title("🧭 Navigation")
selection = st.sidebar.radio("Choose a section:", list(PAGES.keys()))
page = PAGES[selection]
page.app()
