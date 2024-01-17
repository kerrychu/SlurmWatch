import requests
import json
from typing import Dict
from dotenv import load_dotenv
import os

load_dotenv()
slack_webhook = os.getenv("slack_webhook")


def send_slack_message(data: Dict[str, str]) -> str:
    """
    send slack message with given data
    Args:
        data: job records

    Returns: request response
    """
    payload = json.dumps({'text': data})
    headers = {"Content-type": "application/json"}
    response = requests.request(
        "POST", slack_webhook, headers=headers, data=payload, timeout=3600
    )
    print({"response": response.text, "response_code": response.status_code})
    return response.text
