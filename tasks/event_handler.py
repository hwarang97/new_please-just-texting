from services.schedule_parser import parse_schedule_from_message

async def handle_event_creation(event_data: dict):
    message = event_data.get("event").get("text")
    schedule_info = parse_schedule_from_message(message)
    print(schedule_info)
