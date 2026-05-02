import requests
from bs4 import BeautifulSoup

# Define the payload with the login credentials 
#get payload from the inspect element of the login form on the website
payload = {
    "email": "admin@example.com",
    "password": "password"
}
#change from get to post as we are sending data to the server
response = requests.post("https://www.scrapingcourse.com/login", data=payload)

if response.status_code == 200:
  print("Successfully retrieved the page!")
else:
  print("Failed to retrieve the page.", response.status_code) 

print(response.text)