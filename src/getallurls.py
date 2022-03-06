# Import libraries
from bs4 import BeautifulSoup, SoupStrainer
import requests
import csv
import pandas as pd

url = requests.get("https://www.linkedin.com/learning/instructors/20514018")
soup = BeautifulSoup(url.text, 'html.parser')

##  Iterate over all links on the given URL with the response code next to it
for link in soup.find_all('a'):
    print(f"Url: {link.get('href')} ")
