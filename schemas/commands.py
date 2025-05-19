from pydantic import BaseModel


class SlashCommand(BaseModel):
    channel_id: str
    command: str
    text: str
    response_url: str
