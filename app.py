import streamlit as st
import pandas as pd
import pickle as pk
import os

# Set Streamlit page settings
st.set_page_config(page_title="Loan Prediction App", page_icon="💰", layout="centered")

# Resolve file paths relative to this file (important for deployment)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_file(file_name):
    return pk.load(open(os.path.join(BASE_DIR, file_name), "rb"))

# Load model and scaler
model = load_file("model.pkl")
scaler = load_file("scaler.pkl")

# App Title
st.title("💰 Loan Prediction App")
st.write("Fill the details below to check whether your loan is likely to be approved.")

# Inputs
no_of_dep = st.slider("Number of Dependents", 0, 5)
grad = st.selectbox("Education", ["Graduated", "Not Graduated"])
self_emp = st.selectbox("Self Employed?", ["Yes", "No"])
Annual_Income = st.number_input("Annual Income", min_value=0, max_value=10_000_000, step=5000)
Loan_Amount = st.number_input("Loan Amount", min_value=0, max_value=10_000_000, step=5000)
Loan_Dur = st.slider("Loan Duration (Years)", 0, 30)
Cibil = st.slider("CIBIL Score", 0, 900)
Assets = st.number_input("Total Assets Value", min_value=0, max_value=10_000_000, step=5000)

# Encoding
grad_s = 0 if grad == "Graduated" else 1
emp_s = 1 if self_emp == "Yes" else 0

# Prediction Button
if st.button("Predict"):
    # Prepare data as DataFrame
    pred_data = pd.DataFrame(
        [[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]],
        columns=[
            "no_of_dependents",
            "education",
            "self_employed",
            "income_annum",
            "loan_amount",
            "loan_term",
            "cibil_score",
            "Assets",
        ],
    )

    # Scale input
    scaled_data = scaler.transform(pred_data)

    # Predict output
    prediction = model.predict(scaled_data)[0]

    # Display result
    if prediction == 1:
        st.success("✅ Loan Is Approved")
    else:
        st.error("❌ Loan Is Rejected")