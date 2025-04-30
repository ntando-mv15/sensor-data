# Added multi-stage build to reduce final image size and add layer of security.
# --------- Builder ---------

# Using python:3.13.3-slim due to security fixes (was 3.10.12-slim)   
FROM python:3.13.3-slim AS builder

#Updated WORKDIR to industry standards
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# --------- Final Stage ---------

FROM python:3.13.3-slim AS runtime

RUN adduser --disabled-password --gecos "" python-user

WORKDIR /app

# Copied app source code from builder
COPY --from=builder /app /app

# Copied Python install from builder
COPY --from=builder /usr/local /usr/local

RUN chown -R python-user:python-user /app

# Switched to non-root user
USER python-user

# Started the app
ENTRYPOINT ["flask"]
CMD ["--app", "app.main", "run", "--host=0.0.0.0", "--port=5000"]    