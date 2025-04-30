FROM python:3.9

COPY ./app /app
COPY ./requirements.txt /app
COPY ./startup.sh /app

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y mariadb-client && pip install mysqlclient

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN chmod +x startup.sh

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "80"]