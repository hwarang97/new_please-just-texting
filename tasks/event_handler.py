import json

from services.event_crud import create_event
from services.schedule_parser import parse_schedule_from_message


async def handle_event(event_data: dict):
    # Message parsing
    message = event_data.get("event").get("text")
    schedule_info = json.loads(parse_schedule_from_message(message))

    # Event handle
    # action = schedule_info.get("action", None)
    action = "create"

    # schedule_info 에서 CRUD 중 하나를 선택
    if action == "create":
        create_event(schedule_info)
    elif action == "read":
        pass
    elif action == "update":
        pass
    elif action == "remove":
        pass

    # 사용자에게 작업이 완료되었음을 알림
