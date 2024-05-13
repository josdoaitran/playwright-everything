from playwright.sync_api import Page, Request, Response
import pytest


def on_request(request: Request):
    print("Sent Request: ", request)

def on_response(response: Response):
    print("Got Response: ", response)

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }

def test_example_network_event(page: Page):
    page.on("request", on_request)
    page.on("response", on_response)

    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click()
    print(page.url)
    page.close()


