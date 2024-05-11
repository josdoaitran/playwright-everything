from playwright.sync_api import Page, expect
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://www.saucedemo.com/")
        self.username = self.page.locator("//input[@id='user-name']")
        self.password = self.page.locator("//input[@id='password']")
        self.login_btn = self.page.locator("//input[@id='login-button']")
        self.alert_messsage = self.page.locator("//h3[@data-test='error']")

    def verify_login_page(self, page: Page):
        expect(self.username).to_be_visible()
        expect(self.password).to_be_visible()

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

    def verify_login_failed_alert_message(self):
        expect(self.alert_messsage).to_be_visible()