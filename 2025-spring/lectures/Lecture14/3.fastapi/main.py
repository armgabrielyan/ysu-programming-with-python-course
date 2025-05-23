from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


items_db: dict[int, Item] = {}


@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    item_id = len(items_db) + 1
    items_db[item_id] = item

    return {"id": item_id, **item.model_dump()}


@app.get("/items/", response_model=list[Item])
def get_items():
    return list(items_db.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return items_db[item_id]


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    del items_db[item_id]
