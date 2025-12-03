# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# copiar apenas requirements para aproveitar cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copiar código
COPY . .

# criar pasta data/model
RUN mkdir -p /app/data /app/model

# gerar dados e treinar durante build 
RUN python src/prepare.py && python src/train.py

EXPOSE 8000

# rodar uvicorn
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
