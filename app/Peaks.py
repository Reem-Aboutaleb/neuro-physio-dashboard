import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def load_ppg_data():
    return pd.read_csv("data/ppg_sample.csv")

def app():
    st.title("💓 PPG Peak Detection & Heart Rate")

    df = load_ppg_data()
    ppg = df['ppg_amplitude']
    peaks, _ = find_peaks(ppg, distance=10)  # adjust distance for real data

    st.write("### 📈 PPG Signal with Peaks")
    fig, ax = plt.subplots()
    ax.plot(ppg, label='PPG Signal')
    ax.plot(peaks, ppg[peaks], "x", label='Peaks', color='red')
    ax.legend()
    st.pyplot(fig)

    # Estimate Heart Rate (assuming 10s duration)
    peak_count = len(peaks)
    est_hr = peak_count * 6  # 6 = 60 sec / 10 sec of signal

    st.success(f"Estimated Heart Rate: {est_hr} BPM")
