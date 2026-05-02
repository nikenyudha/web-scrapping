import requests
from bs4 import BeautifulSoup 

# user-agent header to mimic a real browser, and avoid being blocked by the server
#find the user-agent string from your browser's network tab in inspect element, request headers, and copy the user-agent value and Accept header value
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}
response = requests.get("https://www.scrapethissite.com/pages/advanced/?gotcha=headers", headers = headers)

if response.status_code == 200:
  print("Request successful!")
else:
  print(f"Request failed with status code: {response.status_code}")

print(response.text)

