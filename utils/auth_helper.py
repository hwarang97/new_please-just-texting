import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

TOKEN_PATH = Path(__file__).resolve().parents[1] / "token.json"

SCOPES = os.getenv("SCOPES")


def get_header() -> dict[str, str]:
    with open(TOKEN_PATH, mode="r") as f:
        token = json.load(f)
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }
    return headers
