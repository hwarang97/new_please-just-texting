async def handle_event_creation(event_data: dict):
    message = event_data.get("event").get("text")
    print(message)
