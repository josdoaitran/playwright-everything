from playwright.sync_api import sync_playwright
import os


def delete_storage_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("The file does not exist.")


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    delete_storage_file("./auth/storage_stage.json")

    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click()
    # Save the authentication value
    page.pause()
    context.storage_state(path="./auth/storage_stage.json")
    context.close()
    print(page.url)
    page.close()


