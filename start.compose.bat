@echo off
echo Iniciando script Python para subir o Docker Compose...

REM === Caminho completo para o Python ===
set PYTHON_PATH="C:\Users\PEDRO\AppData\Local\Programs\Python\Python314\python.exe"

REM === Ir para a pasta onde o .bat está ===
cd /d "%~dp0"

REM === Executar o script ===
%PYTHON_PATH% run.compose.py

pause
