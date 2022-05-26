import json
from flask import Flask, request, jsonify
from model import load, predict
import pandas as pd

app = Flask(__name__)

logged_model = 'runs:/13edcaa1670540948b350d0e1702efef/model'

# Load model as a PyFuncModel.
model = load(logged_model)

columns =  ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"]

@app.route("/")
def home():
    return "ok"

@app.route("/invocations", methods=["POST"])
def predict():
    data = request.get_json()
    data_input = [[data[col] for col in columns]]  

    predict = model.predict(pd.DataFrame(data_input))
    result = {
        "predict": predict[0]
    }
    return result

app.run(host="0.0.0.0", port=8080)