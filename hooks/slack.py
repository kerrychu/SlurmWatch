import requests
import json


def send_slack_message(data: dict[str, str], webhook: str) -> str:
    text= ""
    for key, value in data.items():
        if isinstance(value, list):
            for element in value:
                for subkey, subvalue in element.items():
                    text += f"\t⦿ {subkey}: {subvalue}\n"
        text += f"⦿ {key}: {value}\n"

    payload = {"text": text}
    payload_json = json.dumps(payload)
    headers = {"Content-type": "application/json"}
    response = requests.request(
        "POST", webhook, headers=headers, data=payload_json, timeout=3600
    )
    print(payload_json)
    print({"response": response.text, "response_code": response.status_code})
    return response.text
