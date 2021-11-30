import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, url_for
import pickle
from sklearn.linear_model import LinearRegression, BayesianRidge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


app = Flask(__name__)

# Predictor Tool
def SalePrice_Range(to_predict_list):
    ols = pickle.load(open('models/Linear.sav'))
    br = pickle.load(open('models/BayesianRidge.sav'))
    rf = pickle.load(open('models/RandomForest.sav'))
    gb = pickle.load(open('models/GBooster.sav'))
    pred_list = [ols.predict(to_predict), 
                 br.predict(to_predict), 
                 rf.predict(to_predict),
                 gb.predict(to_predict)]
    low = min(pred_list)
    low_fmt = '${:,.2f}'.format(low[0])
    high = max(pred_list)
    high_fmt = '${:,.2f}'.format(high[0])
    return str(low_fmt)+' - '+str(high_fmt)

# def ValuePredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1,4)
#     loaded_model = pickle.load(open('../fakeLinear.sav'))
#     result = loaded_model.predict(to_predict)
#     return result[0]

def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        to_predict_list = np.array(to_predict_list).reshape(1,105)
        prediction = SalePrice_Range(to_predict_list)
        return render_template('index.html', prediction=prediction)



# Pages / Template Rendering
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/', methods = ['GET','POST'])
def index():
    prediction = SalePrice_Range(to_predict_list) 
    return render_template('index.html', prediction=prediction)

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/team')
def team():
    return render_template('team.html')

    if __name__ == '__main__':
        app.run(debug=True)
