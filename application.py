from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np


app=Flask(__name__)
cors=CORS(app)

model = pickle.load(open("LinearRegressionmode1.pkl",'rb'))
car = pd.read_csv("cleaned car.csv")


@app.route('/' , methods = ['GET','POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique() , reverse=True)
    fuel_types = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    return render_template('index.html' , companies=companies,car_models=car_models,years=years,fuel_types=fuel_types)



@app.route('/predict' , methods=['POST'])
@cross_origin()
def predict():
    car_model = request.form.get('car_model')
    company = request.form.get('company')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    kms_driven = request.form.get('kms_driven')
    print(car_model,company,year,kms_driven,fuel_type)
    prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                                              columns=['name','company','year','kms_driven','fuel_type']))

    return str(np.round(prediction[0],2))

if __name__ == "__main__":
    app.run(debug=True)
