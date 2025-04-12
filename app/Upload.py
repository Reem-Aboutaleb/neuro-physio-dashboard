import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("📂 Upload Your Own Signal")

    uploaded_file = st.file_uploader("Upload your PPG .csv file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            st.success("✅ File uploaded successfully!")
            st.write("### 📈 Preview of Uploaded Data")
            st.line_chart(df.iloc[:, 1])  # Assume second column is signal

            st.write("### 📊 Summary Statistics")
            st.dataframe(df.describe())

        except Exception as e:
            st.error(f"⚠️ Could not read file: {e}")
    else:
        st.info("Please upload a `.csv` file with PPG amplitude values.")
