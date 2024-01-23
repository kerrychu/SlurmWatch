import json

import requests


def send_slack_message(message: str, webhook: str) -> str:
    payload = {"text": message}
    payload_json = json.dumps(payload)
    headers = {"Content-type": "application/json"}
    response = requests.request(
        "POST", webhook, headers=headers, data=payload_json, timeout=3600
    )
    print(payload_json)
    print({"response": response.text, "response_code": response.status_code})
    return response.text
