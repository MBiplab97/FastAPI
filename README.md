# FastAPI and Streamlit Integration

This project demonstrates the integration of FastAPI and Streamlit to create a web application that performs basic arithmetic operations. The FastAPI backend handles the calculations, while the Streamlit frontend provides a user-friendly interface.

## Features
- Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
- Interactive web interface using Streamlit.
- REST API backend using FastAPI.

## Requirements
- Python 3.7+
- FastAPI
- Uvicorn
- Streamlit
- Requests

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MBiplab97/FastAPI.git
   cd FastAPI
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Start the FastAPI Backend
Run the FastAPI app using Uvicorn:
```bash or cmd
uvicorn app:app --reload
```
- The API will be available at `http://127.0.0.1:8000`.
- Swagger UI documentation: `http://127.0.0.1:8000/docs`.

### Start the Streamlit Frontend
Run the Streamlit app:
```bash or cmd
streamlit run streamlit.py
```
- The web interface will be available at `http://localhost:8501`.

## API Endpoints
- `POST /calculate`
  - Request Body:
    ```json
    {
      "operation": "add",
      "a": 5,
      "b": 3
    }
    ```
  - Response:
    ```json
    {
      "result": 8
    }
    ```

## Project Structure
```
FastAPI/
├── app.py          # FastAPI backend
├── calculator.py   # Calculation logic
├── streamlit.py    # Streamlit frontend
├── requirements.txt # Dependencies
├── README.md       # Project documentation
```

## License
This project is licensed under the MIT License.