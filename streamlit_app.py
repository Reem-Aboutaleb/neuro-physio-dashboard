import streamlit as st
from app import PPG, Peaks, EEG, Classifier, Upload  # ✅ All tabs imported

# Navigation tabs
PAGES = {
    "PPG Signal": PPG,
    "PPG + Peak Detection": Peaks,
    "EEG Viewer": EEG,
    "Stress Classifier": Classifier,
    "Upload Your Signal": Upload  # ✅ Upload tab added here
}

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
selection = st.sidebar.radio("Choose a section:", list(PAGES.keys()))
page = PAGES[selection]
page.app()


