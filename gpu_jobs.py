import os
from dotenv import load_dotenv
from utils.subprocess_operations import get_piped_stdout, stdout_to_quota_records
from hooks.slack import send_slack_message

load_dotenv()
SLACK_WEBHOOK = os.getenv("SLACK_JOB_WEBHOOK")


def get_gpu_jobs() -> str:
    main_cmd = "squeue -t RUNNING"
    piped_cmd = "grep gpu_cuda"
    return get_piped_stdout(main_cmd, piped_cmd)


def monitor():
    gpu_jobs = get_gpu_jobs()
    return stdout_to_gpu_records(gpu_jobs)


if __name__ == "__main__":
    print(monitor())
