import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument("--headless") # Aktifkan jika ingin berjalan di belakang layar
driver = webdriver.Chrome(options=options)

driver.get("https://www.allrecipes.com/search?q=chicken")
wait = WebDriverWait(driver, 10)

all_results = [] # Tempat menyimpan hasil scraping

def scrape_page():
    """Fungsi khusus untuk mengambil judul resep di halaman yang sedang aktif"""
    # Mencari elemen kartu resep
    # AllRecipes menggunakan class 'mntl-card-list-items' untuk setiap item resep
    resep_elements = driver.find_elements(By.CSS_SELECTOR, ".mntl-card-list-items")
    
    for item in resep_elements:
        try:
            # Ambil judul dari span di dalam card
            title = item.find_element(By.CSS_SELECTOR, ".card__title-text").text
            # Ambil link resep
            link = item.get_attribute("href")
            
            if title:
                all_results.append({"title": title, "link": link})
        except:
            continue

# 1. Bypass Cookie
try:
    wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
    time.sleep(1)
except:
    pass

# 2. Mulai Scraping Multi-Halaman
jumlah_halaman = 3 # Tentukan mau berapa halaman

for i in range(jumlah_halaman):
    print(f"--- Men-scrape Halaman {i+1} ---")
    
    # Scroll ke bawah perlahan agar semua card ter-render (Lazy Loading)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    # Ambil data dari halaman saat ini
    scrape_page()
    print(f"Berhasil mengambil {len(all_results)} data sejauh ini.")

    # Klik Next jika belum di halaman terakhir
    if i < jumlah_halaman - 1:
        try:
            next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.mntl-pagination__next")))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", next_btn)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(3) # Tunggu loading halaman berikutnya
        except Exception as e:
            print("Tidak bisa menemukan tombol Next, mungkin sudah halaman terakhir.")
            break

# 3. Tampilkan Hasil Akhir
print("\n" + "="*30)
print("HASIL SCRAPING:")
print("="*30)
for idx, resep in enumerate(all_results, 1):
    print(f"{idx}. {resep['title']}")
    print(f"   Link: {resep['link']}")

driver.quit()