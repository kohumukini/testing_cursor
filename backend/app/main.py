from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import ENGINE, init_db

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

    print("Tables Created!")
    yield

app = FastAPI(lifespan = lifespan)

@app.get("/")
def read_root(): 
    return {"status": "Database Connection Initialized"}