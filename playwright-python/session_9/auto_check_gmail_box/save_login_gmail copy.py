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

    page.goto("https://accounts.google.com/")

    email_value = os.environ['EMAIL']
    page.locator("//input[@type='email']").fill(email_value)
    page.locator("//*[@id='identifierNext']/div/button").click()

    password_value = os.environ['PASSWORD']
    page.locator("//input[@type='password']").fill(password_value)
    page.locator("//*[@id='passwordNext']/div/button").click()
    page.pause()
    #### Here is the
    context.storage_state(path="./auth/storage_stage.json")
    context.close()
    print(page.url)
    page.close()


