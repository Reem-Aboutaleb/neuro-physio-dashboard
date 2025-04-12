import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def simulate_eeg():
    fs = 250  # Hz
    t = np.linspace(0, 2, 2 * fs)  # 2 seconds
    eeg = (
        0.5 * np.sin(2 * np.pi * 10 * t) +  # Alpha
        0.3 * np.sin(2 * np.pi * 20 * t) +  # Beta
        0.2 * np.random.randn(len(t))      # Noise
    )
    df = pd.DataFrame({'Time': t, 'EEG': eeg})
    return df

def app():
    st.title("🧠 EEG Viewer")

    df = simulate_eeg()

    st.write("### Simulated EEG Signal (2 seconds)")
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['EEG'], color='purple')
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("EEG Signal")
    st.pyplot(fig)

    st.write("### Brainwave Bands in Signal")
    st.markdown("""
    - **Alpha (8–13 Hz)**: Relaxation
    - **Beta (14–30 Hz)**: Alertness
    - **Theta (4–7 Hz)**: Drowsiness
    - **Delta (<4 Hz)**: Deep sleep
    """)
