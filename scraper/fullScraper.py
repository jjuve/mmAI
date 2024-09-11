from playwright.sync_api import sync_playwright, Playwright
from bs4 import BeautifulSoup

def scrape_data():
      with sync_playwright() as p:
             browser = p.chromium.launch(headless=True)
             page = browser.new_page()
             page.goto("https://www.espn.com/college-football/scoreboard/_/week/1/year/2024/seasontype/2")
             html_content = page.content()
             soup = BeautifulSoup(html_content, "html.parser")
             print(soup)

             browser.close()


if __name__ == "__main__":
	scrape_data()