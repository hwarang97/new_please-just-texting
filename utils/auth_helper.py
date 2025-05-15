import json
import os
from abc import ABC, abstractmethod
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

TOKEN_PATH = Path(__file__).resolve().parents[1] / "token.json"

SCOPES = os.getenv("SCOPES")


class HeaderStrategy(ABC):

    @abstractmethod
    def get_header(self):
        pass


class GoogleHeader(HeaderStrategy):
    def get_header(self):
        with open(TOKEN_PATH, mode="r") as f:
            token = json.load(f)
            headers = {
                "Authorization": f"Bearer {token['access_token']}",
                "Content-Type": "application/json",
            }
        return headers


_HEADER_STRATEGIES: dict[str, HeaderStrategy] = {"google": GoogleHeader()}


def get_header(domain_name: str) -> dict[str, str]:
    header_instance = _HEADER_STRATEGIES[domain_name]
    return header_instance.get_header()
