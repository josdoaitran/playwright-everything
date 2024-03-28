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

    await page.goto("https://demoqa.com/links")
    # Click Me button
    link_text = page.locator("//a[@id='simpleLink']")

    await link_text.highlight()
    await expect(link_text).to_have_text("Home")
    await link_text.click()

    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())