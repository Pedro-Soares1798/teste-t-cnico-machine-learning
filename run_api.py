# run_api.py

import os
import uvicorn

# 1. Configuração do PYTHONPATH:
# Defina a variável de ambiente PYTHONPATH para incluir o diretório atual ('.').
# Isso resolve o erro 'ModuleNotFoundError: No module named 'src'' 
os.environ['PYTHONPATH'] = '.'

# 2. Execução do Servidor Uvicorn:
if __name__ == "__main__":
    print("Iniciando o FastAPI com Uvicorn...")
    uvicorn.run("src.api:app", host="127.0.0.1", port=8000, reload=True)