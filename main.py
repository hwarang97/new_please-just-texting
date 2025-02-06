from typing import Union

from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class User(BaseModel):
    name: str
    email: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, user: User):
    return {"item_name": item.name, "item_price": item.price, "item_id": item_id, "user_name": user.name}

@app.post("/slack/events")
async def slack_events(request: Request):
    data = await request.json()

    if data.get("type") == "url_verification":
        return {"challenge": data.get("challenge")}

    if data.get("type") == "event_callback":
        event = data.get("event")
        print("message: ", event.get("text"))

        return {"status": "ok"}

    return {"status": "ignored"}
