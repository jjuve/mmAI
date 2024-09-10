from playwright.sync_api import sync_playwright, Playwright

def scrape_scores():
      with sync_playwright() as p:
             browser = p.chromium.launch(headless=False)
             page = browser.new_page()
             page.goto("https://www.espn.com/college-football/scoreboard")
             
             browser.close()
          
          
if __name__ == "__main__":
	scrape_scores()