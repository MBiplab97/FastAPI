"""
This module defines a FastAPI application for performing basic arithmetic operations.

Endpoints:
- POST /calculate: Perform a calculation based on the provided operation and operands.
"""

# Import necessary modules
from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate

# Create a FastAPI instance
app = FastAPI()

# Define the request model for calculation
class CalculationRequest(BaseModel):
    operation: str  # The operation to perform (e.g., add, subtract, multiply, divide)
    a: float        # The first operand
    b: float        # The second operand

@app.post("/calculate")
def perform_calculation(request: CalculationRequest):
    """
    Perform a calculation based on the provided operation and operands.

    Args:
        request (CalculationRequest): The calculation request containing the operation and operands.

    Returns:
        dict: A dictionary containing the result or an error message.
    """
    try:
        result = calculate(request.operation, request.a, request.b)
        return {"result": result}
    except ValueError as e:
        return {"error": str(e)}