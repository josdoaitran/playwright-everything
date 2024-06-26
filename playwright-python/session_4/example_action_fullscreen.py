import asyncio
import os

from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    user_dir = 'tmp/playwright'
    user_dir = os.path.join(os.getcwd(), user_dir)

    chromium = playwright.chromium # or "firefox" or "webkit".
    # browser = await chromium.launch(headless=False, slow_mo=500)
    browser = await chromium.launch_persistent_context(user_dir, headless=False, slow_mo=500, args=['--start-maximized'], no_viewport=True)
    page = await browser.new_page()

    # await page.set_viewport_size({"width": 1920, "height": 1080})

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