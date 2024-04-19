import json
import os

class GeneratingReport:
    def delete_report_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            print("File deleted successfully.")
        else:
            print("The file does not exist.")

    @staticmethod
    def generate_report():
        # generate and return a report
        GeneratingReport.delete_report_file("report.json")
        result_data = {
            "timeStamp": "2024-4-20 12-37-9",
            "status": "PASSED",
            "testCaseId": "TC-001 Covering Our test case example"
        }
        with open('report.json', 'w') as file:
            return json.dump(result_data, file)