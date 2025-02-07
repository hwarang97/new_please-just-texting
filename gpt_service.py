from openai import OpenAI
from prompt import PROMPT

def extract_schedule_info(client: OpenAI, text: str, prompt: str) -> str | None:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "assistant",
             "content": PROMPT},
            {
                "role": "user",
                "content": text
            },
        ]
    )

    return completion.choices[0].message.content
