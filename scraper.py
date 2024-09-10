from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.espn.com/college-football/scoreboard")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)