from  playwright.sync_api import Page, Route
import pytest

RESOURCE_WILL_BE_FILTERED = {
    "image",
    "font",
    "stylesheet"
}
def on_route_to_filter_resource(route: Route):
    if (route.request.resource_type in RESOURCE_WILL_BE_FILTERED):
        route.abort()
    else:
        route.continue_()
    
@pytest.fixture(autouse=True)
def skip_resource(page: Page):
    page.route("**", on_route_to_filter_resource)

def test_example_filter_all_iamge_css(page: Page):
    page.goto("https://bstackdemo.com/")
    page.pause()
    page.screenshot(path="./logs/image.jpg", full_page=True)