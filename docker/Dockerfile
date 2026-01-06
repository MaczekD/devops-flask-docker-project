FROM python:3.11-slim

WORKDIR /app

# zależności systemowe dla psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/src ./src

EXPOSE 5000

CMD ["python", "src/app.py"]
