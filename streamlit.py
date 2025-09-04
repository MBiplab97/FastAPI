# This is the streamlit code to call the api and see the results in a web app
import streamlit as st
import requests

def main():
    st.title("FastAPI and Streamlit Integration")

    # Input fields for the two numbers and operation
    a = st.text_input("Enter first number (a):", value="0")
    b = st.text_input("Enter second number (b):", value="0")
    operation = st.selectbox("Select operation:", ["add", "subtract", "multiply", "divide"])

    # Button to perform the calculation
    if st.button("Calculate"):
        try:
            payload = {"operation": operation, "a": a, "b": b}
            print(payload)
            response = requests.post("http://127.0.0.1:8000/calculate", json=payload)
            print(response)
            if response.status_code == 200:
                result = response.json().get("result")
                st.success(f"The result of {operation}ing {a} and {b} is: {result}")
            else:
                st.error(f"Error: {response.json().get('detail')}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

if __name__ == "__main__":
    main()