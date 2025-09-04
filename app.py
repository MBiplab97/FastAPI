# basic FastAPI app
from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate

app = FastAPI()

class CalculationRequest(BaseModel):
    operation: str
    a: float
    b: float

@app.post("/calculate")
def perform_calculation(request: CalculationRequest):
    try:
        result = calculate(request.operation, request.a, request.b)
        return {"result": result}
    except ValueError as e:
        return {"error": str(e)}