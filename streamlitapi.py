import streamlit as st
import pandas as pd
import pickle

def main():

    st.title("Car Price Prediction App")

    # Load Model
    model = pickle.load(open("car_price_model.pkl", "rb"))

    # Input fields
    car_model = st.selectbox("Select Car Model", ["i20", "Swift", "Baleno", "Alto"])
    company = st.selectbox("Select Company", ["Hyundai", "Maruti", "Tata", "Honda"])
    year = st.text_input("Enter Manufacturing Year")
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    kms_driven = st.text_input("Enter KMs Driven")

    # Predict Button
    if st.button("Predict Price"):
        try:
            year = int(year)
            kms_driven = int(kms_driven)

            # Create DataFrame
            input_df = pd.DataFrame({
                "car_model": [car_model],
                "company": [company],
                "year": [year],
                "fuel_type": [fuel_type],
                "kms_driven": [kms_driven]
            })

            st.write("DEBUG INPUT DF:")
            st.write(input_df)

            prediction = model.predict(input_df)
            st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")

        except Exception as e:
            st.error("ERROR OCCURRED:")
            st.write(e)

# Run the app
if __name__ == "__main__":
    main()
