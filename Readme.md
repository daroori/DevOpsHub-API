# DevOpsHub API

This is the backend API for the DevOpsHub project, built with Python and FastAPI.

## Description

The API provides endpoints to monitor and interact with CI/CD pipelines. It's designed to be a central hub for development operations.

## Getting Started

### Prerequisites

- Python 3.10+
- Pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd devopshub-api
    ```

2.  **Create and activate a virtual environment:**
    - On Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\Activate.ps1
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

-   `GET /`: Welcome message.
-   `GET /health`: Health check for the API.
-   `GET /api/pipelines`: Returns a list of mock pipeline data.

## Dependencies

This project uses the following major libraries:

-   [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance) web framework for building APIs.
-   [Uvicorn](https://www.uvicorn.org/): A lightning-fast ASGI server.
-   [Pydantic](https://docs.pydantic.dev/): Data validation and settings management using Python type annotations.

For a full list of dependencies, see `requirements.txt`.