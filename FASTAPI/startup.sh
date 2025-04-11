#!/bin/sh

# Start the backend...
uvicorn main:app --host 0.0.0.0 --reload --port 80