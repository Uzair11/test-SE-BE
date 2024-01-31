FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["sh", "-c", "cd /app && flask run"]
