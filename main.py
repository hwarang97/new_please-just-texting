import os
from urllib.parse import urlencode

import uvicorn
from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, Request
from fastapi.responses import RedirectResponse
from pyngrok import ngrok

from tasks.event_handler import handle_event_creation

load_dotenv()
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_PASS = os.getenv("GOOGLE_CLIENT_PASS")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
GOOGLE_SCOPES = os.getenv("SCOPES")

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/slack/events")
async def slack_events(request: Request, background_task: BackgroundTasks):
    data = await request.json()
    event_type = data.get("type")

    if event_type == "event_callback":
        background_task.add_task(handle_event_creation, data)
        return {"status": "ok"}

    if event_type == "url_verification":
        return {"challenge": data["challenge"]}


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
async def auth_callback():
    pass


if __name__ == "__main__":
    port = 8000
    http_tunnel = ngrok.connect(addr=f"{port}", bind_tls=True)
    print(f"ngrok url: {http_tunnel}")
    uvicorn.run("main:app", port=port, reload=True)
