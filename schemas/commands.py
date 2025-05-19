from pydantic import BaseModel


class SlashCommand(BaseModel):
    """
    reference: https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId
    """

    channel_id: str
    command: str
    text: str
    response_url: str
