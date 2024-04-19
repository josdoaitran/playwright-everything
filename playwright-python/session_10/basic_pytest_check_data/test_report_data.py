import json
from session_10.basic_pytest_check_data.report_data import GeneratingReport

def test_report_data():
    GeneratingReport.generate_report()
    with open('report.json') as file:
        data = json.load(file)
        assert type(data) == dict
        assert len(data) == 3
        assert "timeStamp" in data

