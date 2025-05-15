import requests

from utils.auth_helper import get_header

url = "https://slack.com/api/chat.postMessage"
channel = "C08CRFN5B5W"

def send_message(event_list: list, url=url, channel=channel):
    headers = get_header("slack")

    blocks = []
    for idx, event in enumerate(event_list):
        title = event.get("summary")
        start_time = event.get("start").get("dateTime")
        end_time = event.get("end").get("dateTime")
        line = f"{idx+1} - {title} ({start_time} - {end_time})"
        block = {
            "type": "section",
            "text" : {
                "type": "mrkdwn",
                "text": line,
            }
        }
        blocks.append(block)

    body = {
        "channel": channel,
        "blocks": blocks,
    }

    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
