import os
from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar.events.owned"]
BASE_DIR = Path(__file__).resolve().parents[1]
TOKEN_PATH = BASE_DIR / "token.json"
CREDENTIALS_PATH = BASE_DIR / "credentails.json"

creds = None
if os.path.exists(TOKEN_PATH):
    creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

# No Token are expired
if not creds or creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        # proceed authorization
        flow = InstalledAppFlow.from_client_secrets_file(
            str(CREDENTIALS_PATH), SCOPES
        )
        creds = flow.run_local_server(port=0)

    with open(str(TOKEN_PATH), "w") as token:
        token.write(creds.to_json())

try:
    # initiate client
    service = build("calendar", "v3", credentials=creds)



