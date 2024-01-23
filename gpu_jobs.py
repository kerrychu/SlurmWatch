import os
from dotenv import load_dotenv
from utils.subprocess_operations import get_piped_stdout, stdout_to_gpu_records, job_records_to_slack_message
from hooks.slack import send_slack_message

load_dotenv()
SLACK_WEBHOOK = os.getenv("SLACK_GPU_JOBS_WEBHOOK")


def get_gpu_jobs() -> str:
    main_cmd = "squeue -t RUNNING"
    piped_cmd = "grep gpu_cuda"
    return get_piped_stdout(main_cmd, piped_cmd)


def monitor():
    gpu_jobs = get_gpu_jobs()
    gpu_records = stdout_to_gpu_records(gpu_jobs)
    slack_message = job_records_to_slack_message("🔉 Currently Running GPU Jobs\n", gpu_records)
    send_slack_message(slack_message, SLACK_WEBHOOK)


if __name__ == "__main__":
    monitor()
