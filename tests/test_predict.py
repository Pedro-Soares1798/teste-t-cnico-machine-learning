# tests/test_predict.py
from src.prepare import generate_data, save_csv
from src.train import train_and_save
from src.predict import load_model, predict_single
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def test_end_to_end(tmp_path):
    # Gera dataset pequeno e salva
    df = generate_data(n=50, random_state=1)
    save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "water_quality.csv")
    df.to_csv(save_path, index=False)

    # Treina
    train_and_save(random_state=1)

    # Carrega modelo e faz uma predição simples
    model = load_model()
    sample = {
        "ph": 7.0,
        "turbidity": 1.0,
        "dissolved_oxygen": 8.0,
        "temperature": 20.0,
        "conductivity": 180.0
    }
    out = predict_single(model, sample)
    assert "prediction" in out
    assert "probability" in out
