from playwright.sync_api._generated import ElementHandle
from playwright.sync_api import expect, Page
from session_28.pages.base_page import Base

class LoginPage(Base):
    @property
    def username_input(self) -> ElementHandle:
        return self.page.locator("//input[@id='user-name']")

    @property
    def password_input(self) -> ElementHandle:
        return self.page.locator("//input[@id='password']")

    @property
    def login_button(self) -> ElementHandle:
        return self.page.locator("//input[@id='login-button']")

    @property
    def error_message(self) -> ElementHandle:
        return self.page.locator("//h3[@data-test='error']")

    def goto_base_url(self):
        self.page.goto(self.base_url)

    def verify_login_page(self, page: Page):
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()

    def login(self, username, password):
        self.goto_base_url()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_failed_alert_message(self):
        expect(self.error_message).to_be_visible()

    def verify_login_failed_content_message(self, message):
        expect(self.error_message).to_have_text(message)