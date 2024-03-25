from flask import Flask, render_template, request
from joblib import load
import numpy as np

# Load the model
model = load('iris_model.joblib')


def predict_iris(features):
    # Convert the features into a numpy array and reshape it into a 2D array with 1 row
    features = np.array(features).reshape(1, -1)

    # Use the loaded model to make a prediction
    prediction = model.predict(features)

    return prediction[0]


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', prediction=None)


@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = predict_iris(features)

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)


