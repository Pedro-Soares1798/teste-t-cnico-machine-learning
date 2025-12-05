# Water Quality - MLOps Project

**Resumo:** Projeto para o desafio técnico — classifica água como "boa" (1) ou "ruim" (0).

## Como o projeto está organizado
- `src/prepare.py` → gera dataset sintético (data/water_quality.csv)
- `src/train.py` → treina RandomForest e salva em model/model.pkl
- `src/predict.py` → função de inferência
- `src/api.py` → FastAPI com POST /predict
- `Dockerfile` → container com a API
- `Makefile` → comandos úteis

## Requisitos obrigatórios
1. **Python + ML**: modelo treinado com scikit-learn (RandomForest).
2. **Pipeline de MLOps**: (prepare/train/predict) e métricas (accuracy, F1).
3. **Deploy**: container Docker com API FastAPI.
4. **README**: instruções de execução e uso.

## Como executar 
1. Instalar Python 3.10+ e pip.
2. Clonar o repo.
3. Criar e ativar virtualenv (opcional):
   ```
   python -m venv venv
   source venv/bin/activate  # linux/mac
   venv\Scripts\activate     # windows
   ```
4. Instalar dependências:
   ```
   pip install -r requirements.txt
   ```
5. Gerar dados e treinar:
   ```
   `src/prepare.py` → gera dataset sintético (data/water_quality.csv)
-  `src/train.py` → treina RandomForest e salva em model/model.pkl

   ```
6. Rodar API local:
# utilizar caso não funcione o arquivo start.compose.bat
run_api.py

# para acessar a API
   ```
   Acesse `http://localhost:8000/docs` e teste o endpoint `/predict`.

## Exemplo de uso da API
POST `http://localhost:8000/docs`
Body (JSON):
```json
{
  "ph": 7.1,
  "turbidity": 1.2,
  "dissolved_oxygen": 8.0,
  "temperature": 20.0,
  "conductivity": 180.0
}
```
Resposta:
```json
{
  "result": {
    "prediction": 1,
    "probability": 0.87
  }
}
```

## Possíveis melhorias (diferenciais)
- Registrar modelos com MLflow.
- Orquestrar pipeline com Prefect ou Airflow.
- Adicionar monitoramento de drift dos dados com Evidently.
- Pipeline CI/CD com GitHub Actions.
- Interface simples com Streamlit para visualização.
