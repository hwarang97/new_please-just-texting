import os

from fastapi import FastAPI
from fastapi import Request
from openai import OpenAI
from dotenv import load_dotenv

from prompt import PROMPT

load_dotenv()
app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
