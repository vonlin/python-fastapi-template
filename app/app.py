import logging
import os
import uvicorn
import sys

from fastapi import FastAPI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logging_config import configure_logging
logger = configure_logging(__name__)

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
