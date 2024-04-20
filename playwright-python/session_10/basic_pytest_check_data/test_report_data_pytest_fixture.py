import json
import pytest
from session_10.basic_pytest_check_data.report_data import GeneratingReport


def test_report_data(report_data):
    print("\n Verify Test Case 01")
    assert type(report_data) == dict
    assert len(report_data) == 3

def test_report_data_key(report_data):
    print("\n Verify Test Case 02")
    assert "timeStamp" in report_data
    assert "status" in report_data

def test_report_data_value(report_data):
    print("\n Verify Test Case 03")
    assert "Passed" ==  report_data["status"]
    assert "2024-4-20 12-37-9" == report_data["timeStamp"]

@pytest.fixture()
def report_data():
    print("\n Generate report in pytest fixture")
    GeneratingReport.generate_report("2024-4-20 12-37-9",
                                     "Passed",
                                     "TC-001 Covering Our test case example")
    with open("report.json") as file:
        return json.load(file)
