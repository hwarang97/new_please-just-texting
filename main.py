import json
import os
from pathlib import Path
from typing import Annotated
from urllib.parse import urlencode

import requests
import uvicorn
from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from pyngrok import ngrok

from tasks.event_handler import handle_event
from schemas.commands import SlashCommand

load_dotenv()
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_PASS = os.getenv("GOOGLE_CLIENT_PASS")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
GOOGLE_SCOPES = os.getenv("SCOPES")
TOKEN_PATH = Path(__file__).resolve().parent / "token.json"


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/slack/events")
async def slack_events(request: Request, background_task: BackgroundTasks):
    data = await request.json()
    event_type = data.get("type")

    if event_type == "event_callback":
        background_task.add_task(handle_event, data)
        return {"status": "ok"}

    if event_type == "url_verification":
        return {"challenge": data["challenge"]}


@app.post("/slack/commands/calendar")
async def handle_calendar_command(
    request: Annotated[SlashCommand, Form()], background_task: BackgroundTasks
):

    data = request.model_dump()
    background_task.add_task(handle_event, data)
    return {"status": "ok"}


@app.get("/auth/login")
async def auth_login():
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": GOOGLE_SCOPES,
        "access_type": "offline",
        "prompt": "consent",
    }
    auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode(params)
    return RedirectResponse(url=auth_url)


@app.get("/auth/callback")
async def auth_callback(code: str = "", error: str = ""):
    # Authorization Refuse
    if error:
        return {"error": error}

    # Request token
    params = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_PASS,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    # TODO: 네트워크 결과를 기다리는 과정인데 왜 await를 사용할 수 없는 거지?
    response = requests.post(
        url="https://oauth2.googleapis.com/token", data=params
    ).json()

    # store token
    with open(TOKEN_PATH, mode="w") as token:
        json.dump(response, token)


if __name__ == "__main__":
    port = 8000
    http_tunnel = ngrok.connect(addr=f"{port}", bind_tls=True)
    print(f"ngrok url: {http_tunnel}")
    uvicorn.run("main:app", port=port, reload=True)
