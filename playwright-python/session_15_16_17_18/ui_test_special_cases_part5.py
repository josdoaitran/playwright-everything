# UI Testing Spacial Case
from playwright.sync_api import Page, expect
import pytest

# 13. Verify progress bar

def test_example_mouse_over(page: Page):
    page.goto("http://www.uitestingplayground.com/mouseover")
    hover_link = page.locator("//a[@title='Click me']")
    hover_link.hover()
    text_warming = page.locator("//a[@class='text-warning']")
    text_warming.click(click_count=4)
    expect(page.locator("//span[@id='clickCount']")).to_have_text("4")

# 14. Special Case: Non-breaking space
def test_example_non_breaking_space(page: Page):
    page.goto("http://www.uitestingplayground.com/nbsp")
    # page.locator("//button[text()='My Button']").click(timeout=2000)
    page.locator("//button[text()='My&nbsp;Button']").click(timeout=2000)

# 15. Overlapped element
# http://www.uitestingplayground.com/overlapped
def test_example_overlapped_element(page: Page):
    page.goto("http://www.uitestingplayground.com/overlapped")
    name_text_bot = page.get_by_placeholder("Name")
    # name_text_bot.scroll_into_view_if_needed()
    # name_text_bot.fill("Testing4Everyone")
    # expect(name_text_bot).to_have_value("Testing4Everyone")

    # div = page.locator("//div[@style='overflow-y: scroll; height:100px;']")
    div = name_text_bot.locator("..")
    div.hover()
    page.mouse.wheel(0,200)
    name_text_bot.click()
    name_text_bot.fill("Testing4Everyone")
    expect(name_text_bot).to_have_value("Testing4Everyone")

