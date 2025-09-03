import os
from typing import Dict

from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import redis

load_dotenv()

PORT = int(os.getenv("PORT", "8000"))
DATABASE_URL = os.environ["DATABASE_URL"]
REDIS_URL = os.environ["REDIS_URL"]

engine = create_engine(DATABASE_URL, future=True)
redis_client = redis.Redis.from_url(REDIS_URL)

app = FastAPI()


def check_connections() -> None:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    redis_client.ping()


@app.on_event("startup")
def startup_event() -> None:
    check_connections()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello from API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=PORT)
