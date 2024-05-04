# UI Testing Spacial Case

# 1. Dynamic ID
# http://www.uitestingplayground.com/dynamicid

from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"
def test_dynamic_id_example(page: Page):
    page.goto("http://www.uitestingplayground.com/dynamicid")
    dynamic_id_button = page.get_by_role("button", name="Button with Dynamic ID")
    expect(dynamic_id_button).to_be_visible()
    dynamic_id_button.click()

