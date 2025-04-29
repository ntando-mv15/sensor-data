# Using python:3.13.3-slim due to security fixes (was 3.10.12-slim)

FROM python:3.13.3-slim

# Create a non-root user to follow the principle of least privilege
RUN adduser --disabled-password --gecos "" python-user

WORKDIR /sensor-data

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# Change ownership to the non-root user
RUN chown -R python-user:python-user /sensor-data

# Switch to non-root user
USER python-user

# Set up container start behavior
ENTRYPOINT ["flask"]
CMD ["--app", "app.main", "run", "--host=0.0.0.0", "--port=5000"]


