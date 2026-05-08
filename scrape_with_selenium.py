import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

driver = webdriver.Chrome(options=options)  # Make sure to have the appropriate WebDriver installed
driver.get("https://sandbox.oxylabs.io/products")

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".product-card"))
)

results = []
cards = driver.find_elements(By.CSS_SELECTOR, ".product-card")
for card in cards:  
    title = card.find_element(By.CSS_SELECTOR, ".title").text.strip()
    price = card.find_element(By.CSS_SELECTOR, ".price-wrapper").text.strip()
    
    results.append(
        {
            "title": title, 
         "price": price
         }
    )
print(results)

#time.sleep(2)  # Wait for the page to load

driver.quit() 
