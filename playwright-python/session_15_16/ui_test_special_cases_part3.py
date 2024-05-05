# UI Testing Spacial Case
from playwright.sync_api import Page, expect

# 7. Test Scroll to Element and Scroll up and scroll down
# http://www.uitestingplayground.com/scrollbars
# https://katalon.com/katalon-platform
def test_load_deplay_example(page: Page):
    page.goto("http://www.uitestingplayground.com/scrollbars")
    scroll_btn = page.locator("button.btn-primary")
    scroll_btn.scroll_into_view_if_needed()
    page.screenshot(path='./logs/screenshot_page.png')

    # page.goto("https://katalon.com/katalon-platform")
    # page.locator("//button[@id='onetrust-accept-btn-handler']").click()
    # page.mouse.down()
    # onboarding_hub_link = page.get_by_role("link", name = "Onboarding Hub")
    # onboarding_hub_link.scroll_into_view_if_needed(timeout=5000)
    # onboarding_hub_link.click()
    #
    # social_google = page.locator("//*[@id='social-google']")
    # # expect(social_google).to_be_visible(timeout=3000)
    # social_google.click()


