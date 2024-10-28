from flask import Flask, request, jsonify, render_template
import re
import joblib
import os

app = Flask(__name__)

model_path = 'model/random_forest_model.pkl'
if os.path.exists(model_path):
    rf_model = joblib.load(model_path)
else:
    raise FileNotFoundError("Model file not found. Please train the model first.")

def log_recognized_text(voice_input):
    print(f"Recognized Text: {voice_input}")

def extract_health_parameters(voice_input):
    blood_sugar = 120
    hba1c = 7.0
    insulin_dose = 10

    log_recognized_text(voice_input)

    blood_sugar_match = re.search(r'(?i)(blood sugar|sugar level|glucose)\s*(?:is|was|level|at)?\s*(\d+)', voice_input)
    hba1c_match = re.search(r'(?i)(A1c|HbA1c)\s*(?:is|was|level|at)?\s*(\d+\.?\d*)', voice_input)
    insulin_match = re.search(r'(?i)(insulin|dose|I take|I am taking)\s*(?:is|was|taking)?\s*(\d+)', voice_input)

    if blood_sugar_match:
        blood_sugar = int(blood_sugar_match.group(2))

    if hba1c_match:
        hba1c = float(hba1c_match.group(2))

    if insulin_match:
        insulin_dose = int(insulin_match.group(2))

    return blood_sugar, hba1c, insulin_dose

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/consult', methods=['POST'])
def consult():
    data = request.get_json()
    voice_input = data.get('voice_input', '')

    blood_sugar, hba1c, insulin_dose = extract_health_parameters(voice_input)

    model_prediction = rf_model.predict([[blood_sugar, hba1c, insulin_dose]])[0]

    return jsonify({
        'recognized_text': voice_input,
        'blood_sugar': blood_sugar,
        'hba1c': hba1c,
        'insulin_dose': insulin_dose,
        'health_advice': model_prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)
