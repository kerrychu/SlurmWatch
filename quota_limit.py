import os
from dotenv import load_dotenv
from utils.subprocess_operations import get_piped_stdout

load_dotenv()

PROJECT_IDs: list[str] = os.getenv("PROJECT_IDS").split(',')
SLACK_WEBHOOK: str = os.getenv("SLACK_QUOTA_WEBHOOK")


def get_fileset_quota(project_id: str) -> str:
    main_cmd = "rquota"
    piped_cmd = f"grep {project_id}"

    stdout: str = get_piped_stdout(main_command=main_cmd, piped_command=piped_cmd)
    return stdout


def monitor():
    ...


if __name__ == "__main__":
    for project_id in PROJECT_IDs:
        print(get_fileset_quota(project_id))
