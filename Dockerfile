FROM python:3.10-slim

WORKDIR /sensor-data

COPY requirements.txt . 

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD ["flask", "--app=app.main", "run", "--host=0.0.0.0", "--port=5000"]