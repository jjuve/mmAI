from playwright.sync_api import sync_playwright, Playwright
from bs4 import BeautifulSoup

class ESPNscraper:
       def __init__(self):
              self.browser = None
              self.page = None

       def start_browser(self, headless = True):
                  self.browser = p.chromium.launch(headless=headless)
                  self.page = self.browser.new_page()
       
       def scrape_scores(self, url = "https://www.espn.com/college-football/scoreboard/_/week/1/year/2024/seasontype/2"):
              self.page.goto(url)
              html_content = self.page.content()
              soup = BeautifulSoup(html_content, "html.parser")

              print(soup.find('h1').get_text())
              teams = soup.find_all('div', class_='ScoreCell__TeamName')
              scores = soup.find_all('div', class_='ScoreCell__Score')

              team_names = [team.get_text() for team in teams]
              team_scores = [score.get_text() for score in scores]

              return team_names, team_scores
       
       def close_browser(self):
              if self.browser:
                     self.browser.close()
          
          
if __name__ == "__main__":
      with sync_playwright() as p:
            scraper = ESPNscraper()
            scraper.start_browser()
            teams, scores= scraper.scrape_scores()
            print(teams, scores)
            scraper.close_browser()