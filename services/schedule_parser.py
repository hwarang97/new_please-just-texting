import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_DIR = Path(__file__).resolve().parents[1]
EXTRACT_PROMPT_PATH = BASE_DIR / "prompts" / "extract.jinja"

client = OpenAI(api_key=API_KEY)


def render_template() -> str:
    env = Environment(
        loader=FileSystemLoader("../prompts")
    )  # 이거 매번 생성하기보다는 한번 생성한것을 재활용하는게 좋지 않을까?
    template = env.get_template("extract.jinja")  # 하드 코딩하지 말고 상수로 대체하자

    current = datetime.now().strftime("%Y-%m-%dT%H:%M:%S-09:00")
    output = template.render(current=current)
    return output


def parse_schedule_from_message(message: str):
    prompt = render_template()

    response = client.responses.create(
        model="gpt-4.1-nano-2025-04-14", instructions=prompt, input=message
    )

    return response.output_text

if __name__ == "__main__":
    print(render_template())
