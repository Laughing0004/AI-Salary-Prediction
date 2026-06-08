import streamlit as st
import joblib
import pandas as pd

model = joblib.load(
    'salary_prediction_pipeline.pkl'
)

st.title(
    "AI Job Salary Prediction"
)

years_experience = st.number_input(
    "Years Experience",
    min_value=0
)

benefits_score = st.number_input(
    "Benefits Score",
    min_value=0
)

remote_ratio = st.number_input(
    "Remote Ratio",
    min_value=0,
    max_value=100
)

if st.button("Predict Salary"):

    data = pd.DataFrame({
        'years_experience':[years_experience],
        'benefits_score':[benefits_score],
        'remote_ratio':[remote_ratio]
    })

    prediction = model.predict(data)

    st.success(
        f"Predicted Salary: ${prediction[0]:,.2f}"
    )