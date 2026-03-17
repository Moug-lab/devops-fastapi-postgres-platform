from fastapi import FastAPI
import psycopg2
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter("request_count","Total API Requests")

def connect_db():
    return psycopg2.connect(
        host="db",
        database="devopsdb",
        user="postgres",
        password="postgres"
    )

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"message": "DevOps FastAPI Server Running"}

@app.get("/db")
def database_test():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    conn.close()

    return {"PostgreSQL": version}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
