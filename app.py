from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
model=pickle.load(open('random_forest_model.pkl','rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        house_age=float(request.form['house_age'])
        distance_to_the_nearest_mrt_station=float(request.form['distance_to_the_nearest_mrt_station'])
        no_of_convenience_stores=int(request.form['no_of_convenience_stores'])
        latitude=float(request.form['latitude'])
        longitude=float(request.form['longitude'])
        house_price_of_unit_area=float(request.form['house_price_of_unit_area'])
        
        prediction=model.predict([[house_age,distance_to_the_nearest_mrt_station,no_of_convenience_stores,latitude,longitude,house_price_of_unit_area]])
        output=round(prediction[0],2)
        
        if output<0:
            return render_template('index.html',prediction_texts="No house available")
        else:
            return render_template('index.html',prediction_texts="The available house price is $ {} million  ".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)