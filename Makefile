# Makefile - comandos úteis
.PHONY: prepare train run docker-build docker-run test

prepare:
	python src/prepare.py

train:
	python src/train.py

run:
	uvicorn src.api:app --host 0.0.0.0 --port 8000

docker-build:
	docker build -t water-quality-ml .

docker-run:
	docker run -p 8000:8000 water-quality-ml

test:
	pytest -q
