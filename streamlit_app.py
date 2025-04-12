import streamlit as st
from app import PPG, Peaks, EEG, Classifier  # ✅ Imported all current tabs

# Navigation tabs
PAGES = {
    "PPG Signal": PPG,
    "PPG + Peak Detection": Peaks,
    "EEG Viewer": EEG,
    "Stress Classifier": Classifier
}

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
selection = st.sidebar.radio("Choose a section:", list(PAGES.keys()))
page = PAGES[selection]
page.app()


