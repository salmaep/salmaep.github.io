from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import urllib.request
import json

s = Service("E:\DATA DOKUMEN\POLBAN\semester 2\Proyek 1  Pengembangan Perangkat Lunak Desktop\Tugas\P-Minggu 6\Tugas 6.3 web scraping\msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get("https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/")

i = 1
movieslist = []
now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")

for movies in driver.find_elements(By.CLASS_NAME, "row.countdown-item"):
    print(movies.text.split("\n"))
    for img in movies.find_elements(By.TAG_NAME,"img"):
        print(img.get_attribute("src"))
        urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
        i = i+1
        movieslist.append(
            {"Ranking":movies.text.split("\n")[2].split("#",1)[1],
             "Title":movies.text.split("\n")[0].split(" (",1)[0],
             "ReleaseDate":movies.text.split("\n")[0].split(" (", 1)[1].split(")")[0],
             "PercentRate":movies.text.split("\n")[1],
             "Director":movies.text.split("\n")[6].split("Directed By: ",1)[1],
             "ScrapingDate":dt_string,
             "Image":img.get_attribute("src")
             }
            )
        
hasil_scraping = open("hasilscraping.json", "w")
json.dump(movieslist, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.quit()
