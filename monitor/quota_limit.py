import os
from dotenv import load_dotenv
from hooks.slack import send_slack_message
from utils.subprocess_operations import get_cmd_stdout

load_dotenv()

PROJECT_IDs: list[str] = os.getenv("PROJECT_IDS").split(',')
SLACK_WEBHOOK: str = os.getenv("SLACK_QUOTA_WEBHOOK")


def get_fileset_quota(project_id: str) -> str:
    cmd = f"rquota | grep ${project_id}"
    stdout: str = get_cmd_stdout(cmd)
    return stdout


def monitor():
    ...


if __name__ == "__main__":
    for project_id in PROJECT_IDs:
        get_fileset_quota(project_id)
