# Using python:3.13.3-slim due to security fixes (was 3.10.12-slim)

FROM python:3.13.3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# Start app
ENTRYPOINT ["flask"]
CMD ["--app", "app.main", "run", "--host=0.0.0.0", "--port=5000"]

