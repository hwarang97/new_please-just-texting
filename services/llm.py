from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano",
    input="Hello, GPT!"
)

print(response.output_text)
