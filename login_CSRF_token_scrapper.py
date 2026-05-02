import requests
from bs4 import BeautifulSoup

#session object to persist cookies across requests
#when use session, it will automatically handle cookies for you, so you don't have to manually manage them. This is especially useful when dealing with login forms that require CSRF tokens, as the token is often stored in a cookie and needs to be included in subsequent requests.
#and when use session, make sure to change response = requests.get(...) to response = session.get(...) and response = requests.post(...) to response = session.post(...) to ensure that the session is used for all requests, allowing you to maintain the state of the login and handle CSRF tokens properly.

session = requests.Session()
response = session.get("https://www.scrapingcourse.com/login/csrf")
soup = BeautifulSoup(response.text, "html.parser")
csrf_token = soup.find("input", {"name": "_token"})["value"]
print("CSRF Token:", csrf_token)  

payload = {
    "email": "admin@example.com",
   "password": "password",
    "_token": csrf_token}

response = session.post("https://www.scrapingcourse.com/login/csrf", data=payload)

if response.status_code == 200:
  print("Successfully retrieved the page!")
else:  
  print("Failed to retrieve the page.", response.status_code)

print(response.text)

