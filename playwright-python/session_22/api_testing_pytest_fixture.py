# https://dummy.restapiexample.com/
from playwright.sync_api import Page, Playwright, APIRequest
import pytest

@pytest.fixture
def api_context(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url="https://dummy.restapiexample.com"
    )
    yield api_context
    api_context.dispose()

def test_example_api_context(api_context: APIRequest):
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


def test_example_post(api_context: APIRequest):
    headers = {
        'Context-Type': 'application/json'
    }
    body = {
        "name": "Testing4everyone",
        "salary": 20000,
        "age": 23
    }
    response = api_context.post("/api/v1/create", data=body, headers=headers)
    assert response.status == 200
    users = response.json()
    assert users["status"] == "success"
    assert users["data"]["name"] == "Testing4everyone"
    assert users["data"]["salary"] == 20000
    assert users["data"]["age"] == 23
    assert users["message"] == "Successfully! Record has been added."

def test_example_get_by_id(api_context: APIRequest):
    id = 1
    response = api_context.get(f"/api/v1/employee/{id}")
    assert response.status == 200
    users = response.json()
    assert users["status"] == "success"
    assert users["data"]["id"] == id
    assert users["data"]["employee_name"] == "Tiger Nixon"
    assert users["data"]["employee_salary"] == 320800
    assert users["data"]["employee_age"] == 61
    assert users["message"] == "Successfully! Record has been fetched."
