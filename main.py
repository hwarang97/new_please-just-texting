from typing import Union
import os

from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "assistant",
                 "content": PROMPT},
                {
                    "role": "user",
                    "content": event.get("text")
                },
            ]
        )

        print(completion.choices[0].message.content)

        return {"status": "ok"}

    return {"status": "ignored"}
