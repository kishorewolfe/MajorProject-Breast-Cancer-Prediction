# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'classfier.pkl'
logismodel = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':


        radius_mean = float(request.form['radius_mean'])
        texture_mean = float(request.form['texture_mean'])
        perimeter_mean = float(request.form['perimeter_mean'])
        area_mean = float(request.form['area_mean'])
        smoothness_mean = float(request.form['smoothness_mean'])
        compactness_mean = float(request.form['compactness_mean'])

        concavity_mean = float(request.form['concavity_mean'])
        concave = float(request.form['concave points_mean'])
        symmetry_mean = float(request.form['symmetry_mean'])
        fractal_dimension_mean = float(request.form['fractal_dimension_mean'])
        radius_se = float(request.form['radius_se'])
        texture_se = float(request.form['texture_se'])
#######################################################################################
        perimeter_se = float(request.form['perimeter_se'])
        area_se = float(request.form['area_se'])
        smoothness_se = float(request.form['smoothness_se'])
        compactness_se = float(request.form['compactness_se'])
        concavity_se = float(request.form['concavity_se'])
        concavese = float(request.form['concave points_se'])
        symmetry_se= float(request.form['symmetry_se'])

        fractal_dimension_se = float(request.form['fractal_dimension_se'])
        radius_worst = float(request.form['radius_worst'])
        texture_worst = float(request.form['texture_worst'])
        perimeter_worst = float(request.form['perimeter_worst'])
        area_worst = float(request.form['area_worst'])
        smoothness_worst = float(request.form['smoothness_worst'])
        ##########################################################
        compactness_worst = float(request.form['compactness_worst'])
        concavity_worst = float(request.form['concavity_worst'])
        concavepw = float(request.form['concave points_worst'])



        symmetry_worst = float(request.form['symmetry_worst'])
        fractal_dimension_worst = float(request.form['fractal_dimension_worst'])


        data = np.array([[radius_mean, texture_mean, perimeter_mean,
       area_mean, smoothness_mean, compactness_mean, concavity_mean,
       concave, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, perimeter_se, area_se, smoothness_se,
       compactness_se, concavity_se, concavese, symmetry_se,
       fractal_dimension_se, radius_worst, texture_worst,
       perimeter_worst, area_worst, smoothness_worst,

       compactness_worst, concavity_worst, concavepw,
       symmetry_worst, fractal_dimension_worst]])
        my_prediction = logismodel.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)