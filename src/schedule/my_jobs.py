import os
from typing import Optional

from dotenv import load_dotenv
from src.hooks.slack import send_slack_message
from src.utils.data_serialization import (
    read_json_as_job_records,
    write_job_records_to_json,
)
from src.utils.subprocess_operations import (
    stdout_to_job_records,
    RECORDS,
    job_records_to_slack_message,
    get_cmd_stdout,
)

load_dotenv()

JOB_FOLDER = "jobs"
JOB_FILE = "last_updated.json"
JOB_FILE_PATH = os.path.join(JOB_FOLDER, JOB_FILE)
ENABLE_DEBUG_MODE = os.getenv("ENABLE_JOB_DEBUG_MODE").lower() == "true"
SLACK_WEBHOOK = os.getenv("SLACK_JOB_WEBHOOK")


def list_my_job_records() -> RECORDS:
    """_summary_ list current jobs of mine

    Returns:
        pd.DataFrame: dataframe of current sbatch job details
    """
    stdout: str = get_cmd_stdout("squeue --me")
    return stdout_to_job_records(stdout)


def get_last_updated_job_records() -> Optional[RECORDS]:
    if not os.path.exists(JOB_FOLDER):
        os.mkdir(JOB_FOLDER)
        return None
    if not os.path.exists(JOB_FILE_PATH):
        return None
    return read_json_as_job_records(JOB_FILE_PATH)


def monitor_my_jobs():
    """monitor all jobs"""

    last_updated_job_records = get_last_updated_job_records()

    if last_updated_job_records:
        current_jobs_records = list_my_job_records()
        current_job_ids = {record["JOBID"] for record in current_jobs_records}
        last_updated_job_ids = {record["JOBID"] for record in last_updated_job_records}

        if current_job_ids != last_updated_job_ids:
            new_job_ids = current_job_ids.difference(last_updated_job_ids)
            finished_job_ids = last_updated_job_ids.difference(current_job_ids)
            if new_job_ids != set():
                new_job_records = [
                    record
                    for record in current_jobs_records
                    if record["JOBID"] in new_job_ids
                ]

                slack_message = job_records_to_slack_message(
                    "🔉 Update: New Jobs\n", new_job_records
                )
                send_slack_message(message=slack_message, webhook=SLACK_WEBHOOK)
            if finished_job_ids != set():
                finished_job_records = [
                    record
                    for record in last_updated_job_records
                    if record["JOBID"] in finished_job_ids
                ]
                slack_message = job_records_to_slack_message(
                    "🔉 Update: Complete Jobs\n", finished_job_records
                )
                send_slack_message(message=slack_message, webhook=SLACK_WEBHOOK)
            write_job_records_to_json(current_jobs_records, JOB_FILE_PATH)
    else:
        last_updated_job_records = list_my_job_records()
        write_job_records_to_json(last_updated_job_records, JOB_FILE_PATH)


if __name__ == "__main__":
    if not ENABLE_DEBUG_MODE:
        monitor_my_jobs()
