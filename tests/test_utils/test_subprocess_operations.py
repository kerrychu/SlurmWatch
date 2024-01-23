from src.utils.subprocess_operations import (
    strip_empty_string,
    job_records_to_slack_message,
)


def test_strip_empty_string():
    assert strip_empty_string(["hello", "world", ""]) == ["hello", "world"]


def test_job_records_to_slack_message():
    header = "header"
    job_records = [{"key1": "value1", "key2": "value2", "key3": "value3"}]
    assert (
        job_records_to_slack_message(header, job_records)
        == "header\n\t⦿ key1: value1\n\t⦿ key2: value2\n\t⦿ key3: value3\n"
    )
