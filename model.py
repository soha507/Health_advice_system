import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('dataset/patient_health_records.csv')

X = df[['BloodSugarLevel', 'HbA1c', 'InsulinDose']]  # Features
y = df['HealthAdvice']  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

accuracy = rf_model.score(X_test, y_test)
print(f"Model accuracy: {accuracy}")

joblib.dump(rf_model, 'model/random_forest_model.pkl')
print("Model saved as 'random_forest_model.pkl'")
