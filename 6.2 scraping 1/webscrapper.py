#import package requests dan BeautifulSoap
import requests
from bs4 import BeautifulSoup

#request ke website
page = requests.get("https://republika.co.id/");

#extract konten menjadi objek BeautifulSoap
obj = BeautifulSoup(page.text,'html.parser');

print ('Menampilkan objek html')
print ('======================')
print (obj)

print ('\nMenampilkan title browser dengan tag')
print ('====================================')
print (obj.title)

print ('\nMenampilkan title browser tanpa tag')
print ('=====================================')
print (obj.title.text)

print ('\nMenampilkan semua teks h2')
print ('===========================')
for headline in obj.find_all('h2'):
	print (headline.text)

print ('\nMenampilkan headline berdasarkan div class')
print ('============================================')
print (obj.find_all('div',class_='bungkus_txt_headline_center'))

print ('\nMenampilkan semua teks headline')
print ('=====================================')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	print (headline.find('h2').text)

print ('\nMenyimpan headline pada file text')
print ('===================================')
f=open('E:\\DATA DOKUMEN\\Program data\\XAMPP\\htdocs\\scraping\\latihan scraping\\headlineScraper.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	f.write(headline.find('h2').text)
	f.write('\n')
f.close()

#Menyimpan data dalam json

# Import package json
import json
# Deklarasi list kosong
data=[]
# Lokasi file json
f=open('E:\\DATA DOKUMEN\\Program data\\XAMPP\\htdocs\\scraping\\latihan scraping\\headlineScraper.json','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	# append headline ke variabel data
	data.append({"judul":headline.find('h2').text})
# dump list dictionary menjadi json
jdumps=json.dumps(data)
f.writelines(jdumps)
f.close()

# Deklarasi list kosong
dataterkini=[]
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")

# Lokasi file json
f=open('E:\\DATA DOKUMEN\\Program data\\XAMPP\\htdocs\\scraping\\contentTerkini.json','w')
for konten in obj.find_all('div',class_='conten1'):
	# append headline ke variabel data
	dataterkini.append({"judul":konten.find('h2').text,"kategori":konten.find('h1').text,"waktu_publish":konten.find('div',class_='date').text,"tgl_scrap":dt_string})
# dump list dictionary menjadi json
jdumps=json.dumps(dataterkini)
f.writelines(jdumps)
f.close()