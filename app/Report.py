import streamlit as st
import pandas as pd
import io

def create_fake_summary():
    data = {
        'Metric': ['Mean Amplitude', 'Std Dev', 'Peak Count'],
        'Value': [0.142, 0.035, 12]
    }
    df = pd.DataFrame(data)
    return df

def app():
    st.title("📤 Download Summary Report")

    st.write("This tool allows users to download a demo signal report or generate one after upload.")

    summary_df = create_fake_summary()
    st.write("### 📊 Example Report")
    st.dataframe(summary_df)

    # Convert to CSV for download
    csv = summary_df.to_csv(index=False)
    b = io.BytesIO()
    b.write(csv.encode())
    b.seek(0)

    st.download_button(
        label="📥 Download Report as CSV",
        data=b,
        file_name='ppg_summary_report.csv',
        mime='text/csv'
    )
