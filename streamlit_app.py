import streamlit as st
from app import PPG, Peaks, EEG  # ✅ Add EEG here

PAGES = {
    "PPG Signal": PPG,
    "PPG + Peak Detection": Peaks,
    "EEG Viewer": EEG  # ✅ Add EEG tab here
}

st.sidebar.title("🧭 Navigation")
selection = st.sidebar.radio("Choose a section:", list(PAGES.keys()))
page = PAGES[selection]
page.app()

