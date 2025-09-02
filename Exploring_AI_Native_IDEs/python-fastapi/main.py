from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Simple Items FastAPI")


class ItemIn(BaseModel):
    name: str


class Item(BaseModel):
    id: str
    name: str


items: List[Item] = []


@app.get("/items", response_model=List[Item])
def get_items() -> List[Item]:
    return items


@app.post("/items", response_model=Item, status_code=201)
def create_item(item_in: ItemIn) -> Item:
    if not item_in.name:
        raise HTTPException(status_code=400, detail="name is required")
    item = Item(id=str(len(items) + 1), name=item_in.name)
    items.append(item)
    return item


