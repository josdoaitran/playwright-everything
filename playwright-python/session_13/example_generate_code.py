import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.saucedemo.com/")
    await page.locator("[data-test=\"username\"]").click()
    await page.locator("[data-test=\"username\"]").fill("standard_user")
    await page.locator("[data-test=\"password\"]").click()
    await page.locator("[data-test=\"password\"]").fill("secret_sauce")
    await page.locator("[data-test=\"login-button\"]").click()
    await page.locator("[data-test=\"product-sort-container\"]").select_option("za")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
