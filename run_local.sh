#!/usr/bin/env bash
set -e
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/prepare.py
python src/train.py
uvicorn src.api:app --host 0.0.0.0 --port 8000

#### lembrando que é opcional essa ação ! ####
