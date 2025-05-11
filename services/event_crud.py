import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

SCOPES = os.getenv("SCOPES")
TOKEN_PATH = Path(__file__).resolve().parents[1] / "token.json"


def get_header() -> dict[str, str]:
    with open(TOKEN_PATH, mode="r") as f:
        token = json.load(f)
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }
    return headers


def create_event(schedule_info: dict):
    url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
    headers = get_header()
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


def delete_event():
    eventId = "1234"
    url = f"https://www.googleapis.com/calendar/v3/calendars/primary/events/{eventId}"
    with open(TOKEN_PATH, mode="r") as f:
        token = json.load(f)
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }


def get_event(schedule_info: dict) -> dict:
    url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
    headers = get_header()
    params = {
        "timeMax": "2025-04-29T23:00:00+09:00",
        "timeMin": "2025-04-29T15:00:00+09:00",
    }
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()
