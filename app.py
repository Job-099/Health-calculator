from flask import Flask, request, jsonify
from utils import add, subtract
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Arithmetic API!"})

@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.get_json()
    height = data["height"]
    weight = data["weight"]
    bmi_value = calculate_bmi(height, weight)
    return jsonify({"bmi": bmi_value})

@app.route("/bmr", methods=["POST"])
def bmr():
    data = request.get_json()
    height = data["height"]
    weight = data["weight"]
    age = data["age"]
    gender = data["gender"]
    bmr_value = calculate_bmr(height, weight, age, gender)
    return jsonify({"bmr": bmr_value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)