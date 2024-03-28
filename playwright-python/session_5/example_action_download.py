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

    await page.goto("https://demoqa.com/upload-download")

    # https://playwright.dev/python/docs/downloads

    # Start waiting for the download
    async with page.expect_download() as download_info:
        # Perform the action that initiates download
        # Click Download button
        await page.locator("//a[@id='downloadButton']").click()
    download = await download_info.value

    # Wait for the download process to complete and save the downloaded file somewhere
    await download.save_as("./download_folder/" + download.suggested_filename)
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())