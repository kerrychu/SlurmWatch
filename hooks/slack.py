import requests
import json


def send_slack_message(data: dict[str, str], webhook: str) -> str:
    """
    send slack message with given data
    Args:
        data: job records

    Returns: request response
    """
    payload = {"text": json.dumps(data)}
    payload_json = json.dumps(payload)
    headers = {"Content-type": "application/json"}
    response = requests.request(
        "POST", webhook, headers=headers, data=payload_json, timeout=3600
    )
    print(payload_json)
    print({"response": response.text, "response_code": response.status_code})
    return response.text
