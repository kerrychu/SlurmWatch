import subprocess
from itertools import zip_longest
from typing import Optional

JOB_RECORD = dict[str, str]
JOB_RECORDS = list[JOB_RECORD]
QUOTA_RECORD = dict[str, str]
QUOTA_RECORDS = list(QUOTA_RECORD)


def get_cmd_stdout(command: str) -> str:
    result = subprocess.run(
        command.split(" "), capture_output=True, text=True, check=False
    )

    if result.returncode == 0:
        return result.stdout
    else:
        print(f"Command: {command} failed with error: {result.stderr}")


def get_piped_stdout(main_command: str, piped_command: str) -> Optional[str]:
    initial_command_result = subprocess.run(main_command.split(), stdout=subprocess.PIPE, text=True, check=False)

    if initial_command_result.returncode == 0:
        initial_stdout = initial_command_result.stdout
        piped_result = subprocess.run(piped_command.split(" "), input=initial_stdout, stdout=subprocess.PIPE, text=True,
                                      check=False)

        if piped_result.returncode == 0:
            return piped_result.stdout
    else:
        print(f"Command: {main_command} | {piped_command} failed with error: {initial_command_result.stderr}")


def strip_spaces(l: list[str]) -> list[str]:
    return [x for x in l if x != ""]


def stdout_to_job_records(s: str) -> JOB_RECORDS:
    s = s.strip()
    s_list = s.split("\n")
    headers = strip_spaces(s_list[0].split(" "))
    data = [strip_spaces(element.split(" ")) for element in s_list[1:]]
    job_records = []
    for l in data:
        d = {}
        for key, value in zip(headers, l):
            d[key] = value
        job_records.append(d)

    return job_records


def stdout_to_quota_records(s: str) -> QUOTA_RECORD:
    s = s.strip()
    s_list = s.split()
    headers = ["Used Storage (GB)", "Storage Limit (GB)", "Current File Number", "File Number Limit"]
    quota_record = {}
    assert len(s_list) == len(
        headers), f"unexpected error: quota size different from headers size. quota: {s_list}, headers: {headers}"
    for header, quota in zip_longest(headers, s_list[1:]):
        quota_record[header] = quota
    return quota_record
