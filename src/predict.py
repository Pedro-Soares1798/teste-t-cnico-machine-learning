# src/predict.py
"""
Função de inferência usada pela API e testes.
Recebe um dicionário com as features e retorna 'quality' (0 ou 1) e probabilidade.
"""
import os
import joblib
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model", "model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Modelo não encontrado. Rode src/train.py primeiro.")
    return joblib.load(MODEL_PATH)

def predict_single(model, payload):
    # Espera payload dict com chaves: ph, turbidity, dissolved_oxygen, temperature, conductivity
    features = ["ph", "turbidity", "dissolved_oxygen", "temperature", "conductivity"]
    x = np.array([[payload.get(f, 0.0) for f in features]])
    pred = model.predict(x)[0]
    prob = float(model.predict_proba(x).max())
    return {"prediction": int(pred), "probability": prob}
