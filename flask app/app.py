import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, url_for
import pickle
from sklearn.linear_model import Lasso

model = pickle.load(open('model/lasso.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/graph')
def home():
    data = []

    labels = 
    values = 

    return render_template('graph.html', labels=labels, values=values) 

@app.route('/saleprice', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        features = np.array([[int(request.form['LotArea']), 
        int(request.form['OverallQual']), int(request.form['YearBuilt']), 
        int(request.form['YearRemodAdd']),int(request.form['MasVnrArea']), 
        int(request.form['BsmtFinSF1']), int(request.form['BsmtFinSF2']), 
        int(request.form['BsmtUnfSF']),int(request.form['TotalBsmtSF']), 
        int(request.form['1stFlrSF']), int(request.form['2ndFlrSF']), 
        int(request.form['LowQualFinSF']), int(request.form['BedroomAbvGr']), 
        int(request.form['TotRmsAbvGrd']), int(request.form['Fireplaces']), 
        int(request.form['GarageYrBlt']), int(request.form['GarageCars']), 
        int(request.form['GarageArea']), int(request.form['WoodDeckSF']), 
        int(request.form['OpenPorchSF']), int(request.form['EnclosedPorch']), 
        int(request.form['3SsnPorch']), int(request.form['ScreenPorch']), 
        int(request.form['PoolArea']), int(request.form['MoSold']),
        int(request.form['YrSold']), int(request.form['ExterQual_Enc']), 
        int(request.form['BsmtExposure_Enc']), int(request.form['BsmtFinType1_Enc']),
        int(request.form['BsmtFinType2_Enc']), int(request.form['HeatingQC_Enc']), 
        int(request.form['KitchenQual_Enc']), int(request.form['Functional_Enc']), 
        int(request.form['FireplaceQu_Enc']), int(request.form['GarageFinish_Enc']),
        int(request.form['GarageQual_Enc']), int(request.form['PavedDrive_Enc']), 
        int(request.form['PoolQC_Enc']), int(request.form['LandContour_HLS'])]])
        feat_dummi = pd.get_dummies()
        pred = model.predict(features)
        pred_fmt = '${:,.2f}'.format(pred[0])
        return render_template('index.html', pred=pred_fmt)

    return render_template('index.html')

@app.route('/house')
def house():
    return render_template('house.html')

@app.route('/team')
def team():
    return render_template('team.html')

    if __name__ == '__main__':
        app.run(debug=True)
