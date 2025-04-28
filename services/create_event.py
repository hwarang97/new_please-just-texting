import os
from pathlib import Path
from datetime import datetime
from datetime import timedelta

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar.events.owned"]
BASE_DIR = Path(__file__).resolve().parents[1]
TOKEN_PATH = BASE_DIR / "token.json"
CREDENTIALS_PATH = BASE_DIR / "credentials.json"

creds = None

# Load token from local
if os.path.exists(TOKEN_PATH):
    creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

# No Token or Invalid
if not creds or not creds.valid:

    # Token are expired
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # No Refresh token
    else:
        # Proceed authorization with credentials.json
        flow = InstalledAppFlow.from_client_secrets_file(
            str(CREDENTIALS_PATH), SCOPES
        )
        flow.redirect_uri = "http://localhost:8000/auth/callback"
        creds = flow.run_local_server(port=8000)

    # Rewrite token
    with open(str(TOKEN_PATH), "w") as token:
        token.write(creds.to_json())

# Initiate client
service = build("calendar", "v3", credentials=creds)

event = {
    "summary": "GPT 미팅 테스트",
    "location": "서울 마포구",
    "description": "구글 캘린더 API 테스트 미팅",
    "start": {
        "dateTime": (datetime.now() + timedelta(hours=1)).isoformat() + 'Z',
        "timezone": "Asia/Seoul",
    },
    "end": {
        "dateTime": (datetime.now() + timedelta(hours=2)).isoformat() + 'Z',
        "timezone": "Asia/Seoul",
    },
    "reminder": {
        "useDefault": True
    }
}

event_result = service.events().insert(calendarId="primary", body=event).execute()
print(event.get('htmlLink'))


