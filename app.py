import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline + model
model = joblib.load("house_model.pkl")

st.title("🏠 House Price Prediction App")

# Collect user inputs
overallqual = st.slider("Overall Quality (1=Poor, 10=Excellent)", 1, 10, 5)
grlivarea = st.number_input("Ground Living Area (sq ft)", min_value=500, max_value=5000, value=1500, step=50)
garagecars = st.number_input("Garage Cars", min_value=0, max_value=4, value=2, step=1)
neighborhood = st.selectbox("Neighborhood", ["CollgCr","Veenker","Crawfor","NoRidge","Mitchel"])
housestyle = st.selectbox("House Style", ["1Story","2Story","1.5Fin","SLvl","SFoyer"])
kitchenqual = st.selectbox("Kitchen Quality", ["Ex","Gd","TA","Fa"])
salecondition = st.selectbox("Sale Condition", ["Normal","Abnorml","Partial","Family"])

# Build input DataFrame with lowercase names
input_data = pd.DataFrame({
    "overallqual":[overallqual],
    "grlivarea":[grlivarea],
    "garagecars":[garagecars],
    "neighborhood":[neighborhood],
    "housestyle":[housestyle],
    "kitchenqual":[kitchenqual],
    "salecondition":[salecondition]
})

# Debugging: show input columns
st.write("Input features:", input_data.columns.tolist())

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")
