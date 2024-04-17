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
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    page.pause()
    print(page.url)

    # context = browser.new_context(storage_state="./auth/storage_stage.json")
    # page = context.new_page()
    # page.goto("https://www.saucedemo.com/inventory.html")
    # page.pause()
    # print(page.url)
    # page.close()


