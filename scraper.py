from playwright.sync_api import sync_playwright, Playwright
from bs4 import BeautifulSoup
import json, time

def scrape_scores():
      with sync_playwright() as p:
             browser = p.chromium.launch(headless=False)
             page = browser.new_page()
             page.goto("https://www.espn.com/college-football/scoreboard/_/week/1/year/2024/seasontype/2")
             html_content = page.content()
             soup = BeautifulSoup(html_content, "html.parser")
             print(soup.find('h1').get_text())
             teams = soup.find_all('div', class_='ScoreCell__TeamName')
             scores = soup.find_all('div', class_='ScoreCell__Score')
             for team in teams:
                    #print(team.get_text())
                    for score in scores:
                           print(team.get_text())
                           print(score.get_text())
                           break
             
             browser.close()
          
          
if __name__ == "__main__":
	scrape_scores()