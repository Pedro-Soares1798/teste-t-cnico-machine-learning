# src/prepare.py
"""
Gera e salva um dataset sintético simples de qualidade da água.
Produz: data/water_quality.csv
"""
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split # Esta importação não está sendo usada, mas é ok

RANDOM_SEED = 42

# --- CORREÇÃO DO CAMINHO ---
# Garante que o caminho para 'data' seja resolvido corretamente.
# Sobe um nível para o diretório raiz do projeto e anexa 'data'.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(ROOT_DIR)
OUT = os.path.join(PROJECT_DIR, "data")
os.makedirs(OUT, exist_ok=True)
# ---------------------------

def generate_data(n=500, random_state=RANDOM_SEED):
    rng = np.random.RandomState(random_state)
    # Features plausíveis
    ph = rng.normal(loc=7.0, scale=0.8, size=n) 	 # pH
    turbidity = rng.exponential(scale=1.5, size=n) 	 # turbidez
    dissolved_oxygen = rng.normal(loc=8.0, scale=1.2, size=n) # O2
    temp = rng.normal(loc=20.0, scale=3.0, size=n) 	 # temperatura
    conductivity = rng.normal(loc=200.0, scale=80.0, size=n) # condutividade

    # Regra simples para criar label (apenas para exemplo)
    score = (
        (ph >= 6.5) & (ph <= 8.5)
    ).astype(int) + (turbidity < 3.0).astype(int) + (dissolved_oxygen > 6.0).astype(int)
    quality = (score >= 2).astype(int) 	# 1 = boa, 0 = ruim

    df = pd.DataFrame({
        "ph": ph,
        "turbidity": turbidity,
        "dissolved_oxygen": dissolved_oxygen,
        "temperature": temp,
        "conductivity": conductivity,
        "quality": quality
    })

    return df

def save_csv(df, filename="water_quality.csv"):
    path = os.path.join(OUT, filename)
    df.to_csv(path, index=False)
    print(f"Saved dataset to: {path}")

if __name__ == "__main__":
    df = generate_data(n=500)
    save_csv(df)