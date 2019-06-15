from bs4 import BeautifulSoup
import csv
import json
import requests

url = "https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm"
r = requests.get(url)

soup = BeautifulSoup(r.content)
# print(soup.prettify())

lst = soup.find_all('td', {'class': 'titleColumn'})

str = ""
for item in lst:
    title = item.find('a')
    str = str+ title.text + "\n"

with open("output.txt", 'a') as file:
    file.write(str)