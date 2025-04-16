import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

# input에 들어가는 것을 jinja같은 템플렛을 이용해서 만들어보면 어떨까? 꼭 진자를 써야하나?

response = client.responses.create(model="gpt-4.1-nano-2025-04-14", input="Hello, GPT!")

print(response.output_text)
