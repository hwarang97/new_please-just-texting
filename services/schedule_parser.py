import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_DIR = Path(__file__).resolve().parents[1]
PROMPT_PATH_DIR = BASE_DIR / "prompts"
PROMPT_FILE = "extract.jinja"
FORMAT = "RFC3339"
RFC3339_FORMAT_KOREA = "%Y-%m-%dT%H:%M:%S-09:00"

PROMPT_TEMPLATE_ENV = Environment(loader=FileSystemLoader(PROMPT_PATH_DIR))


client = OpenAI(api_key=API_KEY)


def render_template() -> str:
    template = PROMPT_TEMPLATE_ENV.get_template(PROMPT_FILE)
    current = datetime.now().strftime(RFC3339_FORMAT_KOREA)
    output = template.render(current=current)
    return output


def parse_schedule_from_message(message: str):
    prompt = render_template()

    response = client.responses.create(
        model="gpt-4.1-nano-2025-04-14", instructions=prompt, input=message
    )

    return response.output_text
