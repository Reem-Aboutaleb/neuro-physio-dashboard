import streamlit as st
from app import PPG, Peaks, EEG, Classifier, Upload, Report  # ✅ All tabs imported

# Sidebar navigation
PAGES = {
    "PPG Signal": PPG,
    "PPG + Peak Detection": Peaks,
    "EEG Viewer": EEG,
    "Stress Classifier": Classifier,
    "Upload Your Signal": Upload,
    "Download Report": Report  # ✅ New report tab added
}

st.sidebar.title("🧭 Navigation")
selection = st.sidebar.radio("Choose a section:", list(PAGES.keys()))
page = PAGES[selection]
page.app()



