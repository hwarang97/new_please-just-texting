import json
import os
from datetime import datetime
from pathlib import Path

import requests

from schemas.calendar_resoponse import CalendarEventsResponse, EventDate
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


def delete_event(event_id: str):
    calendarId = "primary"
    eventId = event_id
    url = f"https://www.googleapis.com/calendar/v3/calendars/{calendarId}/events/{eventId}"
    headers = get_header("google")
    response = requests.delete(url=url, headers=headers)
    response.raise_for_status()


def update_event(event_id: str):
    calendarId = "primary"
    eventId = event_id
    url = f"https://www.googleapis.com/calendar/v3/calendars/{calendarId}/events/{eventId}"
    headers = get_header("google")
    new_summary = "updated_event"
    new_start_time = EventDate(
        dateTime=datetime.strptime("2025-04-29 18:30", "%Y-%m-%d %H:%M"),
        date=None,
        timeZone="Asia/Seoul",
    ).model_dump(mode="json")
    new_end_time = EventDate(
        dateTime=datetime.strptime("2025-04-29 19:30", "%Y-%m-%d %H:%M"),
        date=None,
        timeZone="Asia/Seoul",
    ).model_dump(mode="json")

    data = {
        "summary": new_summary,
        "start": new_start_time,
        "end": new_end_time,
    }
    response = requests.put(url=url, headers=headers, json=data)
    response.raise_for_status()
