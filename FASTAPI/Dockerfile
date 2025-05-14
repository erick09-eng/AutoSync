FROM python:3.9

COPY ./app /app
COPY .env /app/.env
COPY ./requirements.txt /app
COPY ./startup.sh /app/startup.sh
COPY ./alembic.ini /app
COPY ./alembic /app/alembic

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y mariadb-client && pip install mysqlclient

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN chmod +x /app/startup.sh

CMD ["/app/startup.sh"]