import json

from services.event_crud import create_event, get_event
from services.schedule_parser import parse_schedule_from_message
import requests

from schemas.commands import SlashCommand


from services.slack_messanger import send_message

async def handle_event(request: SlashCommand):
    data: dict = request.model_dump()

    message = data.get("text")
    # schedule_info = json.loads(parse_schedule_from_message(message))
    schedule_info = {}

    # action = schedule_info.get("action", None)
    action = "read"

    # schedule_info 에서 CRUD 중 하나를 선택
    if action == "create":
        create_event(schedule_info)
    elif action == "read":
        event_list = get_event(schedule_info).get('items')
        channel_id = data.get("channel_id")
        send_message(event_list=event_list, channel_id=channel_id)
    elif action == "update":
        pass
    elif action == "remove":
        pass

    # 사용자에게 작업이 완료되었음을 알림
