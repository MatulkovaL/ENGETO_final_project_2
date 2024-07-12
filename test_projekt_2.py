import re
from playwright.sync_api import Page, expect

def test_redirect_to_job_page(page: Page):
    page.goto("https://www.tescan.cz")
    page.click("#menu-item-13167")
    expect(page).to_have_url("https://jobs.tescan.com/")

def test_check_contacts(page:Page):
    page.goto("https://www.tescan.cz")
    expect(page.locator("#menu-item-13029")).to_be_visible()
    page.click("#menu-item-13029")
    expect(page.get_by_text("Libušina tř. 21")).to_have_count(1)

def test_check_multilanguage(page:Page):
    page.goto("https://jobs.tescan.com")
    page.locator(".header-language-current").click()
    language_selector = page.get_by_text("en",exact=True)
    language_selector.click()
    expect(page.locator("#menu-item-11088")).to_have_text("Contact")