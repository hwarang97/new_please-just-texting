import requests

from utils.auth_helper import get_header

url = "https://slack.com/api/chat.postMessage"


def send_message(event_list: list, channel_id: str, url: str = url):
    headers = get_header("slack")

    blocks = []
    for idx, event in enumerate(event_list):
        title = event.summary
        start_time = event.start.dateTime
        end_time = event.end.dateTime
        line = f"{idx+1} - {title} ({start_time} - {end_time})"
        block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": line,
            },
        }
        blocks.append(block)

    body = {
        "channel": channel_id,
        "blocks": blocks,
    }

    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
