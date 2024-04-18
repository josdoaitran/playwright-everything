from playwright.sync_api import sync_playwright
import os


def delete_storage_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("The file does not exist.")


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=True, slow_mo=500)
    context = browser.new_context(storage_state="./auth/storage_stage.json")
    page = context.new_page()
    page.goto("https://gmail.com")
    print(page.url)
    #Expect returned valeu will be: https://mail.google.com/mail/u/0/#inbox

    # Now, we automatically check new mail to our mailbox
    emails = page.locator("//div[@class='Cp']//table//tr")
    emails.highlight()
    new_emails = []
    for email in emails.all():
        is_new_email = email.locator("//td/ul[@class='bqY']/li[@data-tooltip='Mark as read']").count() == 1

        if is_new_email:
            sender = email.locator("//td//div[@class='yW']//span[@class='zF']").inner_text()
            title = email.locator("//td//span/span[@class='bqe']").inner_text()
            new_emails.append([sender, title])

    if len(new_emails) == 0:
        print("No email in your mails box")
    else:
        print(f"{len(new_emails)} new emails")
        print("-" * 40)
        for new_email in new_emails:
            print(f"Mail: From: {new_email[0]} title: {new_email[1]}")
            print("*"*60)


    page.close()


