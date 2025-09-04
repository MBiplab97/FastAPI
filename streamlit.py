"""
This module defines a Streamlit application for interacting with the FastAPI backend.

Features:
- Accept user input for two numbers and an operation.
- Send the input to the FastAPI backend for calculation.
- Display the result or error message to the user.
"""

# Import necessary modules
import streamlit as st
import requests

def main():
    """
    Main function to render the Streamlit application.

    Features:
    - Accept user input for two numbers and an operation.
    - Send the input to the FastAPI backend for calculation.
    - Display the result or error message to the user.
    """
    st.title("FastAPI and Streamlit Integration")

    # Input fields for the two numbers and operation
    a = st.text_input("Enter first number (a):", value="0")
    b = st.text_input("Enter second number (b):", value="0")
    operation = st.selectbox("Select operation:", ["add", "subtract", "multiply", "divide"])

    # Button to perform the calculation
    if st.button("Calculate"):
        try:
            payload = {"operation": operation, "a": a, "b": b}
            response = requests.post("http://127.0.0.1:8000/calculate", json=payload)

            if response.status_code == 200:
                result = response.json().get("result")
                st.success(f"The result of {operation}ing {a} and {b} is: {result}")
            else:
                st.error(f"Error: {response.json().get('detail')}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

if __name__ == "__main__":
    main()