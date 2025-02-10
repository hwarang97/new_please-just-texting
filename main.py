import os

from fastapi import FastAPI
from fastapi import Request
from openai import OpenAI
from dotenv import load_dotenv

from prompt import PROMPT
from gpt_service import extract_schedule_info


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
        print(extract_schedule_info(client, event.get("text"), PROMPT))

        return {"status": "ok"}

    return {"status": "ignored"}
