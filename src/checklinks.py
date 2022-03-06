# Import libraries
from bs4 import BeautifulSoup, SoupStrainer
import requests
import csv
import pandas as pd

data = [
"https://www.linkedin.com/learning/strategic-planning-foundations",
"https://www.linkedin.com/learning/managerial-economics",
"https://www.linkedin.com/learning/project-management-foundations-4",
"https://www.linkedin.com/learning/creating-and-giving-business-presentations",
"https://www.linkedin.com/learning/excel-data-analysis-forecasting",
"https://www.linkedin.com/learning/forecasting-using-financial-statements"
]

for row in data:
    
    # Prompt user to enter the URL
    url = row

    # Make a request to get the URL
    page = requests.get(url)

    # Get the response code of given URL
    response_code = str(page.status_code)

    # Display the text of the URL in str
    # data = page.text

    # Use BeautifulSoup to use the built-in methods
    # soup = BeautifulSoup(data)

    print("Url: " + url + f" | Status Code: {response_code}")

# Iterate over all links on the given URL with the response code next to it
# for link in soup.find_all('a'):
#    print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")
