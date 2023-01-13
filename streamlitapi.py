import streamlit as st
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open("LinearRegressionmode1.pkl",'rb'))
car = pd.read_csv("cleaned car.csv")
companies = sorted(car['company'].unique())
car_models = sorted(car['name'].unique())

def main():
    st.title('car price prediction')

    car_model = st.selectbox('car_model', car_models)
    company = st.selectbox('company', companies)
    year = st.number_input('year')
    fuel_type = st.selectbox('fuel_type', ['Petrol', 'Diesel', 'CNG'])
    kms_driven = st.number_input('kms_driven')

    #conversion of input data
    car_model = car_models.index(car_model)
    company = companies.index(company)
    fuel_type = ['Petrol', 'Diesel', 'CNG'].index(fuel_type)
    
    #prediction code
    if st.button('predict'):
        makeprediction = model.predict(np.array([[car_model,company,year,fuel_type,kms_driven]]).reshape(1, -1))
        output = round(makeprediction[0],2)
        st.success('you can sell your car for {}'. format(output))

if __name__ =='__main__':
    main()
