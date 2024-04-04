from playwright.sync_api import sync_playwright

def on_event_chooser_file(file_chooser):
    print("I will choose a file")
    file_chooser.set_files("./files/sampleFile.jpeg")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    # page.on("load", on_load)
    page.on("filechooser", on_event_chooser_file)
    page.goto("https://www.google.com/")

    page.locator("//div[@class='nDcEnd']").click()
    page.locator("//span[@class='DV7the']").click()

    page.close()





