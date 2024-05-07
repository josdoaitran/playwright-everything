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

