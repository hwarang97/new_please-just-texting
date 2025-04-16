import os

from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_DIR = Path(__file__).resolve().parents[1]
EXTRACT_PROMPT_PATH = BASE_DIR / "prompts" / "extract.xml"

client = OpenAI(api_key=API_KEY)

def parse_schedule_from_message(message: str):
    with open(EXTRACT_PROMPT_PATH) as f:
        prompt = f.read()

    response = client.responses.create(
        model="gpt-4.1-nano-2025-04-14",
        instructions=prompt,
        input=message)

    return response.output_text
