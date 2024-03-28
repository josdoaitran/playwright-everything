import asyncio
import tkinter

from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    app = tkinter.Tk()
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()
    print("width=", width)
    print("height=", height)

    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.set_viewport_size({"width": int(width), "height": int(height)})

    await page.goto("https://www.google.com/")
    # https://playwright.dev/python/docs/input#upload-files
    # Click by Search by image
    await page.locator("//div[@class='nDcEnd']").click()

    async with page.expect_file_chooser() as fc_info:
        await page.locator("//span[@class='DV7the']").click()
    file_chooser = await fc_info.value
    await file_chooser.set_files("./download_folder/sampleFile.jpeg")

    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())