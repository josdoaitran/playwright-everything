from playwright.sync_api import Page, Route

def on_route_to_mock(route: Route):
    route.fulfill(
        status=200,
        json={
            "id": 1,
            "name": "Testing4everyone"
        }
    )

def on_route_manipulate_reponse(route: Route):
    origin_response = route.fetch()
    update_data = origin_response.json()
    update_data["data"]["employee_name"] = "Testing4Everyone"
    update_data["data"]["employee_salary"] = 999999
    route.fulfill(
        response= origin_response,
        json=update_data
    )

def test_mocking_example(page: Page):
    BACK_END = "https://testing4everyone.com/lectures/1"
    page.route(BACK_END, on_route_to_mock)
    response = page.goto(BACK_END)
    assert response.status == 200
    assert response.json()['id'] == 1
    assert response.json()['name'] == 'Testing4everyone'


def test_manipulate_data(page: Page):
    URL = "https://dummy.restapiexample.com/api/v1/employee/1"
    page.route(URL, on_route_manipulate_reponse)
    response = page.goto(URL)
    assert response.status == 200
    users = response.json()
    print (users)
    assert users["status"] == "success"
    assert users["data"]["id"] == 1
    assert users["data"]["employee_name"] == "Testing4Everyone"
    assert users["data"]["employee_salary"] == 999999
    assert users["data"]["employee_age"] == 61
    assert users["message"] == "Successfully! Record has been fetched."


