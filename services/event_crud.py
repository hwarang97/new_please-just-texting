import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

SCOPES = os.getenv("SCOPES")
TOKEN_PATH = Path(__file__).resolve().parents[1] / "token.json"


def create_event(schedule_info: dict):
    url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
    with open(TOKEN_PATH, mode="r") as f:
        token = json.load(f)
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }
    data = {
        "location": f"{schedule_info.get("location")}",
        "summary": "test",
        "end": {
            "dateTime": "2025-04-29T18:00:00+09:00",
            "timeZone": "Asia/Seoul",
        },
        "start": {
            "dateTime": "2025-04-29T17:00:00+09:00",
            "timeZone": "Asia/Seoul",
        },
    }
    response = requests.post(url=url, json=data, headers=headers)
    response.raise_for_status()
