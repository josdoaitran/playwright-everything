import asyncio
from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/buttons")
    # Click Me button
    click_me_button = page.locator("//div[3]/button")
    await click_me_button.highlight()
    await click_me_button.click()
    await expect(click_me_button).to_be_visible()
    # Double Click Button
    double_click_button = page.get_by_role("button", name= "Double Click Me")
    await double_click_button.highlight()
    await double_click_button.dblclick()
    ## Right Click button
    right_click_button = page.get_by_role("button", name="Right Click Me")
    await right_click_button.highlight()
    await right_click_button.click(button="right")

    await click_me_button.click(delay=500)

    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())