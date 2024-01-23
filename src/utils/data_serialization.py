import json
from .subprocess_operations import RECORDS


def write_job_records_to_json(records: RECORDS, filepath: str):
    json_data = json.dumps(records, indent=2)
    with open(filepath, "w") as outfile:
        outfile.write(json_data)


def read_json_as_job_records(filepath: str) -> RECORDS:
    f = open(filepath, "r")
    return json.loads(f.read())
