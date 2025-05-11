#!/bin/bash

# Run Alembic migrations
alembic upgrade head

# Start the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
