import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def generate_data():
    np.random.seed(42)
    n_samples = 100

    # Simulated features: mean, std
    calm = np.random.normal(loc=0.1, scale=0.02, size=(n_samples, 2))
    stress = np.random.normal(loc=0.2, scale=0.03, size=(n_samples, 2))

    X = np.vstack([calm, stress])
    y = np.array([0]*n_samples + [1]*n_samples)

    return pd.DataFrame(X, columns=['MeanAmplitude', 'StdAmplitude']), y

def app():
    st.title("🔬 Stress Classifier")

    st.write("This ML model classifies if a signal indicates **Calm** or **Stress** based on amplitude features.")

    X, y = generate_data()

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    st.write("### Try It Yourself")
    mean_val = st.slider("Mean Amplitude", 0.05, 0.30, 0.15, step=0.01)
    std_val = st.slider("Std Amplitude", 0.01, 0.08, 0.03, step=0.01)

    prediction = model.predict([[mean_val, std_val]])[0]
    label = "Stress" if prediction == 1 else "Calm"

    st.success(f"Prediction: **{label}**")
