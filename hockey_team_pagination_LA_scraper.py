import sqlite3
import requests 
from bs4 import BeautifulSoup 

BASE_URL = "https://www.scrapethissite.com/pages/forms/"
page_num = 1
result = []

while True:
    url = f"{BASE_URL}?q=los&page_num={page_num}&per_page=100"
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

print(f"\nBerhasil mengambil {len(result)} tim dengan kata kunci 'los'.")
print(result)

#save to SQLite database
conn = sqlite3.connect('hockey_teams_LA.db')
cursor = conn.cursor()

#create table 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team TEXT,
        year TEXT,
        win TEXT,
        losses TEXT,
        goal_for TEXT,
        goal_against TEXT,
        win_percentage TEXT
    )
''')

#delete existing data   (avoid duplicates)
cursor.execute('DELETE FROM teams')

# 3. Insert data sekaligus (Lebih rapi dan cepat)
# Kita ubah list of dictionary menjadi list of tuple
data_to_insert = [
    (t['team'], t['year'], t['win'], t['losses'], t['goal_for'], t['goal_against'], t['win_percentage']) 
    for t in result
]

cursor.executemany('''
    INSERT INTO teams (team, year, win, losses, goal_for, goal_against, win_percentage)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', data_to_insert)


#save changes and close connection
conn.commit()
conn.close()

print(f"Data berhasil disimpan ke database 'hockey_teams_LA.db'")