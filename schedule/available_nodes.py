import os
from dotenv import load_dotenv
from schedule.utils.subprocess_operations import (
    get_piped_stdout,
    stdout_to_records,
    job_records_to_slack_message,
)
from schedule.hooks.slack import send_slack_message

load_dotenv()
SLACK_WEBHOOK = os.getenv("SLACK_GPU_JOBS_WEBHOOK")
PARTITIONS: list[str] = os.getenv("PARTITIONS").split(",")
HEADER = ["PARTITION", "AVAILABILITY", "TIMELIMIT", "NODES", "STATE", "NODELIST"]


def get_idle_nodes() -> str:
    main_cmd = "sinfo -t idle"
    piped_cmd = "grep gpu"
    return get_piped_stdout(main_cmd, piped_cmd)


def monitor():
    idle_nodes = get_idle_nodes()
    idle_node_records = stdout_to_records(HEADER, idle_nodes)
    header = "🟢Available nodes in Bunya\n\n"
    filtered_idle_node_records = list(filter(lambda x: x["PARTITION"] in PARTITIONS, idle_node_records))
    slack_message = job_records_to_slack_message(header, filtered_idle_node_records)
    send_slack_message(slack_message, SLACK_WEBHOOK)


if __name__ == "__main__":
    monitor()
