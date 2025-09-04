"""
This module contains the calculation logic for basic arithmetic operations.

Functions:
- calculate: Perform the specified arithmetic operation on two operands.
"""

def calculate(operation: str, a: float, b: float) -> float:
    """
    Perform the specified arithmetic operation on two operands.

    Args:
        operation (str): The operation to perform (add, subtract, multiply, divide).
        a (float): The first operand.
        b (float): The second operand.

    Returns:
        float: The result of the operation.

    Raises:
        ValueError: If the operation is invalid or if division by zero is attempted.
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")