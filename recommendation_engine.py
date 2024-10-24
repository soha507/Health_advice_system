import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

import joblib

rf_model = joblib.load('model/random_forest_model.pkl')

le_gender = LabelEncoder()
le_gender.fit(['M', 'F'])

def get_health_advice(age, gender, blood_sugar, hba1c, insulin_dose, exercise):
    gender_encoded = le_gender.transform([gender])[0]

    prediction = rf_model.predict([[age, gender_encoded, blood_sugar, hba1c, insulin_dose, exercise]])

    return prediction[0]
