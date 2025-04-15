import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

response = client.responses.create(model="gpt-4.1-nano", input="Hello, GPT!")

print(response.output_text)
