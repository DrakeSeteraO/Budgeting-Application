from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Drake", age=19),
    Person(id=2, name="John Doe", age=21),
    Person(id=3, name="Timmy", age=99)
]


@app.get("/api")
def read_root():
    return DB


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}