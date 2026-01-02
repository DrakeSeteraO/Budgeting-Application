from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel

from peewee import *
from database import db
from model import Transaction
from contextlib import asynccontextmanager

app = FastAPI()



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to database
    db.connect()
    db.create_tables([Transaction], safe=True)
    print("Database connected and tables created")
    
    yield  # Application runs here
    
    # Shutdown: Close database connection
    if not db.is_closed():
        db.close()
    print("Database connection closed")



@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.get("/api/transaction/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}