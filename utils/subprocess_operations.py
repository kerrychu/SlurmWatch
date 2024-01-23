import subprocess

JOB_RECORDS = list[dict[str, str]]


def get_cmd_stdout(command: str) -> str:
    return subprocess.run(
        command.split(" "), capture_output=True, text=True, check=False
    ).stdout


def strip_spaces(l: list[str]) -> list[str]:
    return [x for x in l if x != ""]


def stdout_to_job_records(s: str) -> JOB_RECORDS:
    s = s.strip()
    s_list = s.split("\n")
    headers = strip_spaces(s_list[0].split(" "))
    data = [strip_spaces(element.split(" ")) for element in s_list[1:]]
    job_records = []
    for l in data:
        d = dict()
        for key, value in zip(headers, l):
            d[key] = value
        job_records.append(d)

    return job_records
