#!/bin/bash

# Wait for MySQL to be ready
echo "Waiting for MySQL to be ready..."
until mysqladmin ping -h db --silent; do
  echo "MySQL is unavailable - sleeping"
  sleep 3
done

echo "MySQL is up - running migrations"

# Run Alembic migrations with logging and error handling
if alembic upgrade head; then
  echo "Alembic migrations applied successfully"
else
  echo "Alembic migrations failed"
  exit 1
fi

# Start the FastAPI server
echo "Starting FastAPI server"
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
