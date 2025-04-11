FROM python:3.9

COPY ./app /app
COPY ./startup.sh /app
COPY ./requirements.txt /app

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y mariadb-client && pip install mysqlclient

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN chmod +x startup.sh

CMD ["./startup.sh"]