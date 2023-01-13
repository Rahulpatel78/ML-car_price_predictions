import streamlit as st
import pickle

model = pickle.load(open("LinearRegressionmode1.pkl",'rb'))
car = pd.read_csv("cleaned car.csv")
companies = sorted(car['company'].unique())
car_models = sorted(car['name'].unique())

def main():
    st.title('car price prediction')

    car_model = st.selectbox('car_model', car_models)
    company = st.selectbox('company', companies)
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
