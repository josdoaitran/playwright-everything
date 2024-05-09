# UI Testing Spacial Case
import time

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
    # https://en.wikipedia.org/wiki/Non-breaking_space
    page.locator("//button[text()='My\u00A0Button']").click(timeout=2000)


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

# 16. Shadow DOM
# http://www.uitestingplayground.com/shadowdom
def test_example_shadown_dom(page: Page):
    page.goto("http://www.uitestingplayground.com/shadowdom")
    # page.frame_locator("//guid-generator").locator("//button[@id='buttonGenerate']").first.click()
    page.locator("guid-generator .edit-field").fill("1234567890")
    page.locator("guid-generator .button-generate").click(timeout=3000)
    page.locator("guid-generator .button-copy").click(timeout=3000)
    time.sleep(5)

    page.goto("https://books-pwakit.appspot.com/")
    page.locator("book-app[apptitle='BOOKS'] #input").fill("Testing4Everyone")
    text = page.locator("book-app[apptitle='BOOKS'] .books-desc").text_content()
    print(text)
    time.sleep(5)

# 17. iframe example
# Example: https://ui.vision/demo/webtest/frames/
# Example: https://the-internet.herokuapp.com/iframe
def test_iframe_example(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    textbox = page.frame_locator("//*[@src='frame_1.html']").locator('//input')
    textbox.fill("Testing4Everyone")
    page.pause()

    page.goto("https://the-internet.herokuapp.com/iframe")
    email_textbox = page.frame_locator('//*[@id="mce_0_ifr"]').locator('//body')
    email_textbox.click(timeout=1500)
    email_textbox.fill(" Testing4Everyone", timeout=1500)
    page.pause()
