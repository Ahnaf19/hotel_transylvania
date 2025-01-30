import fastapi
import uvicorn
import pydantic
# import loguru
import pytest
import httpx

def print_versions():
    print(f"FastAPI version: {fastapi.__version__}")
    print(f"Uvicorn version: {uvicorn.__version__}")
    print(f"Pydantic version: {pydantic.__version__}")
    # print(f"Loguru version: {loguru.__version__}")
    print(f"Pytest version: {pytest.__version__}")
    print(f"HTTPX version: {httpx.__version__}")

if __name__ == "__main__":
    print_versions()