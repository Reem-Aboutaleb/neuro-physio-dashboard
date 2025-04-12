# 🧠 Neuro-Physio Dashboard

🚀 A next-level biomedical dashboard that fuses signal science with real-time interactivity.  
Built by Reem Aboutaleb — a Biomedical Engineering Master's student at NYU — this app brings PPG and EEG analysis to life with machine learning, intuitive visualizations, and downloadable reports.

🔗 Live App: https://neuro-physio-dashboard-dkpzskqkcxnbccr94b5gxf.streamlit.app/

---

## 🎯 What This App Does

💓 PPG Signal Viewer  
→ View a clean photoplethysmogram (PPG) signal with amplitude patterns.

📈 Peak Detection + Heart Rate  
→ Automatically detect pulse peaks and estimate beats per minute (BPM).

🧠 EEG Viewer  
→ Simulate brainwave activity across Alpha and Beta bands — visualize 2 seconds of synthetic EEG.

🔬 Stress Classifier  
→ Real-time machine learning model that predicts calm vs stress based on signal features.

📂 Upload Your Signal  
→ Bring your own `.csv` data and explore it directly inside the app — no code required!

📤 Download Report  
→ Instantly download a session summary for further analysis or documentation.

---


---

🎬 DEMO

Watch the full Neuro-Physio Dashboard in action:

![Demo GIF](https://github.com/Reem-Aboutaleb/neuro-physio-dashboard/blob/main/images/neuro_physio_full_demo.gif?raw=true)


---


📸 SCREENSHOTS

### 💓 PPG Signal Viewer  
Shows a real-time photoplethysmogram signal.

![PPG Viewer](https://github.com/Reem-Aboutaleb/neuro-physio-dashboard/blob/main/images/ppg_viewer.png?raw=true)

---

### 📈 Peak Detection + Heart Rate  
Detects signal peaks and estimates BPM.

![Peak Detection](https://github.com/Reem-Aboutaleb/neuro-physio-dashboard/blob/main/images/peaks.png?raw=true)


## 🗂️ File Structure

neuro-physio-dashboard/  
├── app/  
│   ├── PPG.py  
│   ├── Peaks.py  
│   ├── EEG.py  
│   ├── Classifier.py  
│   ├── Upload.py  
│   └── Report.py  
├── data/  
│   └── ppg_sample.csv  
├── images/  
│   ├── ppg_viewer.png  
│   ├── peaks.png  
│   └── neuro_physio_demo.gif  
├── streamlit_app.py  
├── requirements.txt  
└── README.md

---

## 🛠️ Built With

- Streamlit — app framework
- Pandas & NumPy — data manipulation
- Matplotlib — visualizations
- Scipy — signal analysis
- Scikit-learn — machine learning

---

## 👩‍🔬 About the Creator

Hi! I’m **Reem Aboutaleb**, a Biomedical Engineering Master's student at NYU. I love combining science, health, and data into interactive experiences that make complex things feel simple — and useful.

This dashboard is one of my favorite projects so far. It brings together:
- ⚙️ Real physiological signals
- 🤖 ML-powered analysis
- 💡 Clean and friendly design

Whether you're a researcher, engineer, or just curious — I hope you enjoy exploring it as much as I enjoyed building it!

---

## 📬 Contact

📧 Email: Reemwalid222@gmail.com  
🔗 GitHub: https://github.com/Reem-Aboutaleb  
💼 LinkedIn: https://www.linkedin.com/in/your-link

---

⭐ Thank you for visiting — feel free to fork it, test it, or reach out if it inspires something in you!


