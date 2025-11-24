📘 Loan Prediction App

A Machine Learning web application built with Streamlit that predicts whether a loan application will be approved or rejected.
The model uses Logistic Regression along with StandardScaler for feature normalization.

🚀 Features

🧮 Real-time loan approval prediction

🤖 Logistic Regression ML model (model.pkl)

📊 Feature scaling using StandardScaler (scaler.pkl)

🧑‍💻 Clean and interactive Streamlit UI

⚡ Fast and lightweight

🌐 Easy deployment on Streamlit Cloud

🧠 Machine Learning Approach
1. Logistic Regression

This is a simple and effective binary classification algorithm used to predict whether a loan will be Approved or Rejected.

2. StandardScaler (Feature Normalization)

Different input features (income, loan amount, CIBIL score, dependents) have different ranges.
To avoid imbalance and improve model learning, we use StandardScaler, which transforms features to:

Mean = 0

Standard Deviation = 1

This helps the Logistic Regression model converge faster and perform better.

Formula used by StandardScaler:

𝑧
=
𝑥
−
mean
std
z=
std
x−mean
	​


This ensures all features are on the same scale.

📂 Features Used in the Model

Dependents

Education

Employment Status

Annual Income

Loan Amount

Loan Duration

CIBIL Score

Total Assets

📂 Project Structure
.
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md

▶️ How to Run Locally
1. Install dependencies
pip install -r requirements.txt

2. Run the Streamlit application
python -m streamlit run app.py

🌐 Deployment (Streamlit Cloud)

Push this project to GitHub

Go to https://share.streamlit.io

Select your repository

Choose app.py as the entry file

Deploy 🚀

🛠 Tech Stack

Python

Streamlit

Logistic Regression (Scikit-learn)

Pandas / NumPy

🤝 Contributing

Contributions are welcome!
Feel free to improve the model, UI, or add additional features.

📄 License

This project is licensed under the MIT License.
