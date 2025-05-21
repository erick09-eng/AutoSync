FROM python:3.9

COPY ./app /app
COPY ./requirements.txt /app
COPY ./alembic.ini /app
COPY ./alembic /app/alembic

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y mariadb-client && pip install mysqlclient

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["sh", "-c", "\
echo 'Waiting for MySQL to be ready...' && \
until mysqladmin ping -h db --silent; do \
  echo 'MySQL is unavailable - sleeping' && sleep 3; \
done && \
echo 'MySQL is up - running migrations' && \
if alembic upgrade head; then \
  echo 'Alembic migrations applied successfully'; \
else \
  echo 'Alembic migrations failed'; \
  exit 1; \
fi && \
echo 'Starting FastAPI server' && \
uvicorn main:app --host 0.0.0.0 --port 8000 --reload \
"]
