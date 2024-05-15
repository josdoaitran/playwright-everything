# https://dummy.restapiexample.com/
from playwright.sync_api import Page, Playwright


def test_example_api_goto(page: Page):
    response = page.goto("https://dummy.restapiexample.com/api/v1/employees")
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


def test_example_api_context(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url="https://dummy.restapiexample.com"
    )
    response = api_context.get("/api/v1/employees")
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


def test_example_get_by_id(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url="https://dummy.restapiexample.com"
    )
    body = {
        "name": "Testing4everyone",
        "salary": 20000,
        "age": 23
    }
    response = api_context.post("/api/v1/create", data=body)
    assert response.status == 200
    users = response.json()
    assert users["status"] == "success"
    datas = users["data"]
    for data in datas:
        if data["name"] == 'Testing4everyone':
            assert data["employee_name"] == "Tiger Nixon"
            assert data["employee_salary"] == 20000
            assert data["employee_age"] == 23
    assert users["message"] == "Successfully! All records has been fetched."
