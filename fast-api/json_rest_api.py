# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(ge=0)

DB: dict[int, Item] = {}

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in DB: raise HTTPException(409, "exists")
    DB[item.id] = item; return item


@app.get("/items/{iid}", response_model=Item)
def get_item(iid: int):
    it = DB.get(iid);
    if not it: raise HTTPException(404, "not found")
    return it