import csv
import requests
from bs4 import BeautifulSoup
#1. menentukan target website
response = requests.get("https://www.scrapethissite.com/pages/simple/")
#print(response.status_code)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
country_blocks = soup.find_all('div', class_='country')
print(f"Total countries found: {len(country_blocks)}")

result = []
for block in country_blocks:
    name_element = block.find('h3', class_='country-name')
    country_name = name_element.get_text(strip=True)
    
    capital_element = block.find('span', class_='country-capital')
    capital_name=capital_element.get_text(strip=True)

    population_element = block.find('span', class_='country-population')
    population_name = population_element.get_text(strip=True)
  
    result.append({ 'country': country_name, 'capital': capital_name, 'population': population_name })

#for item in result:
  #print(f"Country: {item['country']}, Capital: {item['capital']}, Population: {item['population']}, Area: {item['area']}")

with open('countries.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames=['country', 'capital', 'population']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in result:
        writer.writerow(item)

