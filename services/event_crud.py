import os
from pathlib import Path

import requests

from schemas.calendar_resoponse import CalendarEventsResponse
from utils.auth_helper import get_header


def create_event(schedule_info: dict):
    url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
    headers = get_header("google")
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


def get_event(schedule_info: dict) -> CalendarEventsResponse:
    url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
    headers = get_header("google")
    params = {
        "timeMax": "2025-04-29T23:00:00+09:00",
        "timeMin": "2025-04-29T15:00:00+09:00",
    }
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    calendar_event_response = CalendarEventsResponse(**response.json())
    return calendar_event_response

    return response.json()
