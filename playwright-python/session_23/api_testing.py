# https://dummy.restapiexample.com/
from playwright.sync_api import Page

def test_example_get_method(page: Page):
    response = page.goto("	https://dummy.restapiexample.com/api/v1/employees")
    assert response.status == 200
    users = response.json()
    assert users["status"] == "success"
    datas = users["data"]
    for data in datas:
        if data["id"] == 1:
            assert data["employee_name"] == "Tiger Nixon"
            assert data["employee_salary"] == 320800
            assert data["employee_age"] == 61
        if data["id"] == 2:
            assert data["employee_name"] == "Garrett Winters"
            assert data["employee_salary"] == 170750
            assert data["employee_age"] == 63
    assert users["message"] == "Successfully! All records has been fetched."
