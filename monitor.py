import subprocess
from typing import Optional
import os
from hooks.slack import send_slack_message
from utils.stdout_processing import stdout_to_job_records, JOB_RECORDS
from utils.data_serialization import (
    read_json_as_job_records,
    write_job_records_to_json,
)

URL = (
    "https://hooks.slack.com/services/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"
)
JOB_FOLDER = "jobs"
JOB_FILE = "last_updated.json"
JOB_FILE_PATH = os.path.join(JOB_FOLDER, JOB_FILE)


def list_user_job_records() -> JOB_RECORDS:
    """_summary_ list current jobs of mine

    Returns:
        pd.DataFrame: dataframe of current sbatch job details
    """
    result = subprocess.run(
        ["squeue", "--me"], capture_output=True, text=True, check=False
    )
    return stdout_to_job_records(result.stdout)


def get_last_updated_job_records() -> Optional[JOB_RECORDS]:
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
        current_jobs_records = list_user_job_records()
        current_job_ids = set([record["JOBID"] for record in current_jobs_records])
        last_updated_job_ids = set(
            [record["JOBID"] for record in last_updated_job_records]
        )

        if current_job_ids != last_updated_job_ids:
            new_job_ids = current_job_ids.difference(last_updated_job_ids)
            finished_job_ids = last_updated_job_ids.difference(current_job_ids)

            if new_job_ids != set():
                new_job_records = [
                    record
                    for record in current_jobs_records
                    if record["JOBID"] in new_job_ids
                ]
                payload = {"status": "NEW JOBS", "jobs": new_job_records}
                send_slack_message(data=payload, url=URL)
            if finished_job_ids != set():
                finished_job_records = [
                    record
                    for record in last_updated_job_records
                    if record["JOBID"] in finished_job_ids
                ]
                payload = {"status": "Finished JOBS", "jobs": finished_job_records}
                send_slack_message(data=payload, url=URL)
    else:
        last_updated_job_records = list_user_job_records()
        write_job_records_to_json(last_updated_job_records, JOB_FILE_PATH)


if __name__ == "__main__":
    monitor_my_jobs()
