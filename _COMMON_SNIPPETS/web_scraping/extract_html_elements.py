# pip install beautifulsoup4

from bs4 import BeautifulSoup

with open('LOCAL_HTML_FILEPATH') as file:
    soup = BeautifulSoup(file, "html.parser")

    # make list of all 'a' element urls

    a.elems = soup.find_all('a')
    urls = [tag['href'] for tag in a_elems]
    print(urls) #observe output



# Option 2
from bs4 import BeautifulSoup
import requests

url = "http://google.com"
r = requests.get(url, verify=False)

soup = BeautifulSoup(r.text, "html.parser")
a_elems = soup.find_all('a')
urls = [tags['href'] for tag in a_elems if 'href' in tag]
print(urls)

