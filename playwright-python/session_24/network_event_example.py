from playwright.sync_api import Page, Request, Response, Route
import pytest
# import os
# import logging
#
# logger = logging.getLogger('__Test Login__')
# logger.setLevel(logging.INFO)
# def delete_storage_file(file_path):
#     if os.path.exists(file_path):
#         os.remove(file_path)
#         logger.info("File deleted successfully.")
#     else:
#         logger.info("The file does not exist.")

def on_request(request: Request):
    print("Sent Request: ", request)

def on_response(response: Response):
    print("Got Response: ", response)

def on_route_filter_by_request(route: Route):
    print("Request aborted: ", route.request)
    route.abort()

def on_route_filter_by_type_image(route: Route):
    if(route.request.resource_type == "image"):
        route.abort()
    else:
        route.continue_()

def on_route_modify_return_html(route: Route):
    route.fulfill(
        status=200,
        body = "<html><body><h1>Example Response to end user: Testing4everyone</h1></body></html>"
    )

def on_route_modify_return_json(route: Route):
    route.fulfill(
        status=200,
       json= {
           "data": "1234",
           "coca": "Testing4Everyone"
       }
    )
def on_route_modify_rename(route: Route):
    response = route.fetch()
    # I am Sorry http://www.uitestingplayground.com/ :)
    body = response.text().replace("UI Test Automation", "UI Test Automation  - Supper Guideline")
    route.fulfill(response=response, body=body)

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

    page.goto("http://www.uitestingplayground.com/")
    page.screenshot(path="./logs/image.jpg", full_page=True)
    page.close()

def test_example_network_event_filter(page: Page):
    # page.route("http://www.uitestingplayground.com/static/cube.png", on_route_filter_by_request)
    page.route("**/*.png", on_route_filter_by_request)

    page.goto("http://www.uitestingplayground.com/")
    page.screenshot(path="./logs/image.jpg", full_page= True)
    page.close()

def test_example_network_event_filter_by_type(page: Page):
    page.route("**", on_route_filter_by_type_image)

    page.goto("http://www.uitestingplayground.com/")
    page.screenshot(path="./logs/image.jpg", full_page= True)
    page.close()

def test_example_network_event_modify_reponse_to_html(page: Page):
    page.route("http://www.uitestingplayground.com/", on_route_modify_return_html)

    page.goto("http://www.uitestingplayground.com/")
    page.screenshot(path="./logs/image.jpg", full_page= True)
    page.pause()
    page.close()

def test_example_network_event_modify_reponse_to_json(page: Page):
    page.route("http://www.uitestingplayground.com/", on_route_modify_return_json)
    page.goto("http://www.uitestingplayground.com/")
    page.screenshot(path="./logs/image.jpg", full_page= True)
    page.pause()
    page.close()

def test_example_network_event_replace_text(page: Page):
    page.route("http://www.uitestingplayground.com/", on_route_modify_rename)
    page.goto("http://www.uitestingplayground.com/")
    page.screenshot(path="./logs/image.jpg", full_page=True)
    page.pause()