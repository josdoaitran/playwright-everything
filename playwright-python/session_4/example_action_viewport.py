import asyncio

from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    ### View port:
    ### https://whatismyviewport.com/
    await page.set_viewport_size({"width": 393, "height": 852})

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