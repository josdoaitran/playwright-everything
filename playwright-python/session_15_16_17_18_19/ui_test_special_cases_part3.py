# UI Testing Spacial Case
from playwright.sync_api import Page, expect

# 7. Test Scroll to Element and Scroll up and scroll down
# http://www.uitestingplayground.com/scrollbars
# https://katalon.com/katalon-platform
def test_load_scroll_to_element_example_1(page: Page):
    page.goto("http://www.uitestingplayground.com/scrollbars")
    scroll_btn = page.locator("button.btn-primary")
    scroll_btn.scroll_into_view_if_needed()
    page.screenshot(path='./logs/screenshot_page.png')

def test_load_scroll_to_element_example_2(page: Page):
    page.goto("https://katalon.com/katalon-platform")
    page.locator("//button[@id='onetrust-accept-btn-handler']").click()
    page.pause()
    # Scroll down 1000 pixels
    page.evaluate("window.scrollTo(0, 1000)")
    page.screenshot(path='./logs/screenshot_page_down.png')
    page.pause()
    # Scroll up 500 pixels
    page.evaluate("window.scrollTo(0, -500)")
    page.pause()
    page.screenshot(path='./logs/screenshot_page_up.png')
    onboarding_hub_link = page.get_by_role("link", name = "Onboarding Hub")
    onboarding_hub_link.scroll_into_view_if_needed(timeout=5000)
    onboarding_hub_link.click()

    social_google = page.locator("//*[@id='social-google']")
    # expect(social_google).to_be_visible(timeout=3000)
    social_google.click()


# 8. Dynamic Tables
#  http://www.uitestingplayground.com/dynamictable

def test_elements_dynamic_table_example(page: Page):
    page.goto("http://www.uitestingplayground.com/dynamictable")
    comparable_text = page.locator("p.bg-warning").inner_text()
    cpu_comparable_text = comparable_text.split()[-1]
    print(cpu_comparable_text)

    cpu_column = None
    column_header = page.get_by_role("columnheader")
    for index in range(column_header.count()):

        if (column_header.nth(index).inner_text() == 'CPU'):
            cpu_column = index
            break
    assert cpu_column is not None

    chrome_row = None
    list_of_row = page.get_by_role("rowgroup").last.get_by_role("row")
    # chrome_row = list_of_row.filter(has_text="Chrome")

    for row in range(list_of_row.count()):
        list_of_cell = list_of_row.nth(row).get_by_role("cell")
        for cell in range(list_of_cell.count()):
            if list_of_cell.nth(cell).inner_text() == 'Chrome':
                chrome_row = list_of_row.nth(row)
                break

    # assert chrome_row is not None
    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)
    expect(chrome_cpu).to_have_text(cpu_comparable_text)

# 8. Special Cases in Verifying text of element
#  http://www.uitestingplayground.com/verifytext

def test_special_case_verify_text(page: Page):
    page.goto("http://www.uitestingplayground.com/verifytext")
    # Normal case
    title = page.locator("//h3")
    expect(title).to_have_text("Verify Text")
    # Special Case => Using get_by_text to get Elements

    content_to_verify = "Welcome UserName!"
    text_verify = page.locator("//div[@class='bg-primary']").get_by_text("Welcome")
    expect(text_verify).to_have_text(content_to_verify)