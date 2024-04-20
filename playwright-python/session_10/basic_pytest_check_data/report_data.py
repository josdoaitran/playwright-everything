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
    def generate_report(timeStamp: str, status: str, testCaseId: str):
        # generate and return a report
        GeneratingReport.delete_report_file("report.json")
        result_data = {
            "timeStamp": timeStamp,
            "status": status,
            "testCaseId": testCaseId
        }
        with open('report.json', 'w') as file:
            return json.dump(result_data, file)