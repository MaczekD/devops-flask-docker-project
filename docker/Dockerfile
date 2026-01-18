# ==========================
# STAGE 1: builder
# ==========================
FROM python:3.11-slim AS builder

WORKDIR /app

# deps dla postgres (psycopg2)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# ==========================
# STAGE 2: test
# ==========================
FROM builder AS test

COPY app /app

ENV PYTHONPATH=/app

RUN pytest app/tests


# ==========================
# STAGE 3: final
# ==========================
FROM python:3.11-slim AS final

WORKDIR /app

# kopiujemy zbudowane zależności z buildera
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

COPY app /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python", "src/app.py"]
