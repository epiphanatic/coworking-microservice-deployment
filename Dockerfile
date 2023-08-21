FROM python:3.10-slim-buster

WORKDIR /src

COPY ./analytics/requirements.txt requirements.txt

# Dependencies required for psycopg2 #
RUN apt update -y && apt install -y build-essential libpq-dev

RUN pip install -r requirements.txt

COPY ./analytics .

EXPOSE 5153

CMD python app.py

