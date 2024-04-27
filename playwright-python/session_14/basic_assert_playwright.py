from playwright.sync_api import Page, expect
import logging

logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

BASE_URL = "https://www.saucedemo.com/"
def test_website_login_standard_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    logger.info(msg="============== Assert url =============")
    logger.info(page.url)
    assert page.url == BASE_URL
    expect (page).to_have_url(BASE_URL)
    logger.info("Current Title `%s`", page.title())
    expect(page).to_have_title("Swag Labs")

    logger.info(msg="============== Assert Element editable, enable, visible =============")
    # Verify Element visible
    logo = page.locator("//div[@class='login_logo']")
    expect(logo).to_be_visible()

    logger.info(msg="Input Username")
    username = page.locator("//input[@id='user-name']")
    expect(username).to_be_editable()
    expect(username).to_be_enabled()
    expect(username).to_be_visible()
    # expect(username).to_be_checked()
    username.fill("standard_user")
    expect(username).to_have_value("standard_user")

    logger.info(msg="============== Assert Text of Element =============")
    username_title = page.locator("//div[@class='login_credentials']/h4")
    expect(username_title).to_have_text("Accepted usernames are:")

    password_title = page.locator("//div[@class='login_password']/h4")
    expect(password_title).to_contain_text("Password")

    logger.info(msg="============== Assert CSS of Element =============")
    expect(password_title).to_have_css("color", "rgb(255, 255, 255)")
    expect(password_title).to_have_css("font-size", "16px")
    expect(password_title).to_have_css("font-family", "\"DM Mono\", \"sans-serif\"")

    # logger.info(msg="Input password")
    # page.locator("//input[@id='password']").fill("secret_sauce")
    # logger.info(msg="Click login")
    login_button = page.locator("//input[@id='login-button']")
    expect(login_button).to_have_class("submit-button btn_action")


