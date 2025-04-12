import streamlit as st
import pandas as pd

def load_ppg_data():
    return pd.read_csv("data/ppg_sample.csv")

def app():
    st.title("❤️ PPG Signal Viewer")

    df = load_ppg_data()

    st.write("### 📊 Sample PPG Signal (10 seconds)")
    st.line_chart(df['ppg_amplitude'])

    st.write("### 📈 Signal Summary")
    st.dataframe(df.describe())

    st.write("### 🧠 Quick Insight")
    avg_amp = df['ppg_amplitude'].mean()
    st.success(f"Average PPG amplitude: {avg_amp:.4f}")

