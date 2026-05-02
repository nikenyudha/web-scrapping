import requests
from bs4 import BeautifulSoup

#url from network tab in inspect element and filter by XHR
BASE_URL = "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2014"
response = requests.get(BASE_URL)
items = response.json() #parse json response to python dictionary
print(items)

