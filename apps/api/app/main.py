import os
from typing import Dict
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", "8000"))

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello from API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=PORT)
