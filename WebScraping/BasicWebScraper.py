import requests
from bs4 import BeautifulSoup
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/Russell_Wilson"
downloaded_html = requests.get(start_url)

soup = BeautifulSoup(downloaded_html.text, features='lxml')

with open('download.html', "w", encoding="utf-8") as f:
    f.write(soup.prettify())

full_table = soup.select("table.wikitable")
print(full_table)
