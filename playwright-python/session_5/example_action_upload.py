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
    # https://playwright.dev/python/docs/input#upload-files

    await page.locator("//input[@id='uploadFile']").set_input_files("./download_folder/sampleFile.jpeg")
    # Remove all the selected files
    await page.locator("//input[@id='uploadFile']").set_input_files([])
    # Upload again
    await page.locator("//input[@id='uploadFile']").set_input_files("./download_folder/sampleFile.jpeg")
    await expect(page.locator("//p[@id='uploadedFilePath']")).to_contain_text("sampleFile.jpeg")
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())