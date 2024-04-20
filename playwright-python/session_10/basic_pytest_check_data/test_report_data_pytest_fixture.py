import json
import pytest
from session_10.basic_pytest_check_data.report_data import GeneratingReport


def test_report_data(report_data):
        assert type(report_data) == dict
        assert len(report_data) == 3

def test_report_data_key(report_data):
    assert "timeStamp" in report_data
    assert "status" in report_data

def test_report_data_value(report_data):
    assert "Passed" ==  report_data["status"]
    assert "2024-4-20 12-37-9" == report_data["timeStamp"]

@pytest.fixture()
def report_data():
    GeneratingReport.generate_report("2024-4-20 12-37-9",
                                     "Passed",
                                     "TC-001 Covering Our test case example")
    with open("report.json") as file:
        return json.load(file)
