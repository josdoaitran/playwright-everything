# UI Testing Spacial Case



from playwright.sync_api import Page, expect

# 1. Dynamic ID
# Example:
# http://www.uitestingplayground.com/dynamicid
# https://shopee.vn/buyer/login
def test_dynamic_id_example(page: Page):
    page.goto("http://www.uitestingplayground.com/dynamicid")
    dynamic_id_button = page.get_by_role("button", name="Button with Dynamic ID")
    expect(dynamic_id_button).to_be_visible()
    dynamic_id_button.click()

# 2.  Elements have the same attribute class
# Example:
# http://www.uitestingplayground.com/classattr
# https://sellercenter.lazada.vn/apps/seller/login
# reference: https://fastbootstrap.com/components/button/
def test_attribute_class_example(page: Page):
    page.goto("http://www.uitestingplayground.com/classattr")
    # primary_button = page.locator("//button[@class='btn class2 btn-primary btn-test']")
    primary_button = page.locator("button.btn-primary")
    expect(primary_button).to_be_visible()
    primary_button.click()

    page.goto("https://sellercenter.lazada.vn/apps/seller/login")
    # page.locator("//button[@type='submit']").click()
    page.locator("//button[contains(@class, 'next-btn-primary')]")
    # page.locator("button.login-button").click()

# Test example: Element hidden
# Example: http://www.uitestingplayground.com/hiddenlayers
def test_hiden_layer_example(page: Page):
    page.goto("http://www.uitestingplayground.com/hiddenlayers")
    green_button = page.locator("//button[@id='greenButton']")
    # green_button = page.locator("button.btn-success")
    green_button.click()
    # green_button.click(timeout=1000)
    blue_button = page.locator("//button[@id='blueButton']")
    blue_button.click()

# Test load delay until element is ready
# Example: https://katalon.com/katalon-platform
def test_load_deplay_example(page: Page):
    page.goto("https://katalon.com/katalon-platform")
    page.locator("//button[@id='onetrust-accept-btn-handler']").click()
    page.mouse.down()
    onboarding_hub_link = page.get_by_role("link", name = "Onboarding Hub")
    onboarding_hub_link.scroll_into_view_if_needed(timeout=5000)
    onboarding_hub_link.click()

    social_google = page.locator("//*[@id='social-google']")
    # expect(social_google).to_be_visible(timeout=3000)
    social_google.click()

# Test wait for ajax data or data from backend
# Example:
# http://www.uitestingplayground.com/clientdelay
# http://www.uitestingplayground.com/ajax
def test_wait_ajax_data_example(page: Page):
    page.goto("http://www.uitestingplayground.com/ajax")
    page.locator("//button[@id='ajaxButton']").click()
    success_message = page.locator("//p[@class='bg-success']")
    success_message.wait_for()
    expect(success_message).to_be_visible()

# Test example about: Element change after an event
# Example:
# http://www.uitestingplayground.com/textinput
# http://www.uitestingplayground.com/click
def test_element_change_after_event(page: Page):
    page.goto("http://www.uitestingplayground.com/click")
    bad_button = page.locator("//button[@id='badButton']")
    expect(bad_button).to_have_class("btn btn-primary")
    bad_button.click()
    expect(bad_button).to_have_class("btn btn-success")

    page.goto("http://www.uitestingplayground.com/textinput")
    page.locator("//input").fill("Testing4everyone")
    primary_btn = page.locator("button.btn-primary")
    expect(primary_btn).to_have_text("Button That Should Change it's Name Based on Input Value")
    primary_btn.click()
    expect(primary_btn).to_have_text("Testing4everyone")

