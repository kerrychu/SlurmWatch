from typing import List, Dict

JOB_RECORDS = List[Dict[str, str]]


def strip_spaces(l: List[str]) -> List[str]:
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
