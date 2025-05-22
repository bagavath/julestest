# FastAPI Hello App

A simple FastAPI application with a /hello/{name} endpoint.

## Setup

1.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the application

To run the application, use Uvicorn:
```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000/hello/{name}`.
For example, `http://127.0.0.1:8000/hello/Jules` will return:
```json
{"message": "Hello Jules"}
```
