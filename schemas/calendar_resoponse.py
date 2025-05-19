from datetime import date, datetime
from typing import Annotated

from pydantic import BaseModel, Field


class EventDate(BaseModel):
    """
    reference: https://developers.google.com/workspace/calendar/api/v3/reference/events?hl=ko#resource-representations
    """

    date: Annotated[date | None, Field(default=None)]
    dateTime: datetime = Field(...)
    timeZone: Annotated[str | None, Field(default=None)]


class EventItem(BaseModel):
    """
    reference: https://developers.google.com/workspace/calendar/api/v3/reference/events?hl=ko#resource-representations
    """

    id: str
    status: str
    htmlLink: str
    summary: Annotated[str, Field(description="event title", default="")]
    description: Annotated[str, Field(description="event description", default="")]
    location: Annotated[str, Field(default="")]
    creator: dict
    start: EventDate
    end: EventDate
    visibility: Annotated[str, Field(default="")]


class CalendarEventsResponse(BaseModel):
    """
    reference: https://developers.google.com/workspace/calendar/api/v3/reference/events/list?hl=ko#response
    """

    summary: Annotated[str, Field(description="calendar name")]
    items: Annotated[list[EventItem], Field(default_factory=list)]
