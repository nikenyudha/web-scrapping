import requests 
from bs4 import BeautifulSoup 

BASE_URL = "https://www.scrapethissite.com/pages/forms/"
page_num = 1
result = []

while True:
    url = f"{BASE_URL}?page_num={page_num}&per_page=100"
    print(f"fetching page {url}...")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}")      
        break
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table')  
    rows = table.find_all('tr', class_='team')

    if not rows:  
        print(f"No more data found on page {page_num}")
        break   

    for row in rows:
        team_name = row.find('td', class_='name').get_text(strip=True)
        years = row.find('td', class_='year').get_text(strip=True)
        win = row.find('td', class_='wins').get_text(strip=True)
        losses = row.find('td', class_='losses').get_text(strip=True)
        Goal_For = row.find('td', class_='gf').get_text(strip=True)
        Goal_Against = row.find('td', class_='ga').get_text(strip=True)
        pct = row.find('td', class_='pct').get_text(strip=True)

        result.append({
            'team': team_name, 
            'year': years, 
            'win': win,
            'losses': losses,
            'goal_for': Goal_For,
            'goal_against': Goal_Against,
            'win_percentage': pct
            })

    page_num += 1

print(result)
