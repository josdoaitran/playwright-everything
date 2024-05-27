from playwright.sync_api import Page, Route
from session_31.utils.read_data import read_json_by_key, read_yml_by_key
import os

def on_route_modify_return_json(route: Route):
    route.fulfill(
        status=200,
        json={
            "data": "1234",
            "coca": "Testing4Everyone",
            "Environment": os.environ['Environment']
        }
    )


def test_example_read_json(page: Page):
    page.route("**", on_route_modify_return_json)
    environment = os.environ['Environment']
    response = page.goto(read_json_by_key(f"../data/json/{environment}.json", "url"))
    print(response.json())
    assert response.json()['Environment'] == os.environ['Environment']


def test_example_read_yml(page: Page):
    page.route("**", on_route_modify_return_json)
    environment = os.environ['Environment']
    response = page.goto(read_yml_by_key(f"../data/yml/{environment}.yml", "url"))
    print(response.json())
    assert response.json()['Environment'] == os.environ['Environment']
