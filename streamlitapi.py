if st.button("Predict Price"):
    try:
        year = int(year)
        kms_driven = int(kms_driven)

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
