import pickle
import streamlit as st

model = pickle.load(open("LinearRegressionmode1.pkl",'rb'))
def main():
    st.title('car price prediction')

    car_model = st.text_input('car_model')
    company = st.text_input('company')
    year = st.text_input('year')
    fuel_type = st.text_input('fuel_type')
    kms_driven = st.text_input('kms_driven')

    #prediction code
    if st.button('predict'):
        makeprediction = model.predict([[car_model,company,year,fuel_type,kms_driven]])
        output = round(makeprediction[0],2)
        st.success('you can sell your car for {}'. format(output))

if __name__ =='__main__':
    main()
