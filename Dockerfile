FROM python:3.10-slim

WORKDIR /app

# Copy in the source code
COPY version.py .

CMD ["python","version.py"]