
import asyncio
from playwright.async_api import async_playwright, Playwright
from time import perf_counter
async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    start_time = perf_counter()

    await page.goto("https://playwright.dev/", wait_until="load")
    doc_link = page.get_by_role("link", name="Docs")
    await doc_link.click()
    time_taken = perf_counter() - start_time
    print(f"Page is loaded  in {round(time_taken, 2)}")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())