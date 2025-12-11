import pandas as pd
import numpy as np
import streamlit as st
import pickle

def main():
    model = pickle.load(open("car_price_model.pkl", "rb"))

    car_model = st.selectbox("Select Car Model", options)
    company = st.selectbox("Select Company", company_options)
    year = st.text_input("Enter Year")
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    kms_driven = st.text_input("Kms Driven")

    if st.button("Predict Price"):
        year = int(year)
        kms_driven = int(kms_driven)

        input_df = pd.DataFrame({
            "car_model": [car_model],
            "company": [company],
            "year": [year],
            "fuel_type": [fuel_type],
            "kms_driven": [kms_driven]
        })

        prediction = model.predict(input_df)

        st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")

