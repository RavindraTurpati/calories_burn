from flask import Flask, request, jsonify
import util


app = Flask(__name__)
from flask.json import JSONEncoder
import numpy as np

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.float32):
            return float(obj)
        return super(CustomJSONEncoder, self).default(obj)

app.json_encoder = CustomJSONEncoder


@app.route('/get_gender_names', methods=['GET'])
def get_gender_names():
    response = jsonify({
        'genders': util.get_gender_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_cal', methods=['GET', 'POST'])
def predict_cal():
    gender = request.form['gender']
    age = int(request.form['age'])
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    duration = int(request.form['duration'])
    heart_rate = int(request.form['heart_rate'])
    body_temp = int(request.form['body_temp'])

    response = jsonify({
        'estimated_calories': util.get_estimated_calories(gender, age, height, weight, duration, heart_rate, body_temp)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For calory burn Prediction...")
    util.load_saved_artifacts()
    app.run()
