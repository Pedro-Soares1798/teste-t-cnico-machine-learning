"""
FastAPI  com endpoint /predict
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


from src.predict import load_model, predict_single

app = FastAPI(title="Water Quality - Simple ML API")


class InputData(BaseModel):
    ph: float
    turbidity: float
    dissolved_oxygen: float
    temperature: float
    conductivity: float


model = None


@app.on_event("startup")
def startup_event():
    global model

    model = load_model()


@app.post("/predict")
def predict_endpoint(data: InputData):
    try:

        result = predict_single(model, data.dict())
        return {"result": result}
    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))
