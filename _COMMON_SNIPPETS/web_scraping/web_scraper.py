# Simple Web Scraper
# Prev: Automation Scripts
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.txt, 'html.parser')

headlines = [h2.text for h2 in soup.find_all('h2')]
print(headlines)