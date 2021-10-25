import bs4
from bs4 import BeautifulSoup as soup
import urllib3


http = urllib3.PoolManager()
r = http.request('GET', 'https://www.billboard.com/charts/billboard-200')
htmlSource = r.data


page_soup = soup(htmlSource, "html.parser")

containers = page_soup.findAll("span",{"class":"chart-element__information"})


container = containers[0]

filename = "data.csv"
f = open(filename, "w")
headers = "Artist, Titlu\n"
f.write(headers)
i=1
for container in containers:
    song_title = container.findAll("span", {"class":"chart-element__information__song"})
    song_artist = container.findAll("span", {"class":"chart-element__information__artist"})
    peak_rank = container.findAll("span",{"class":"chart-element__information__week"})
    weeks_chart = container.findAll("span",{"class":"chart-element__information__top"})
    last_week = container.findAll("span",{"class":"chart-element__information__lasting"})

    print(i)
    i=i+1
    print(container.text)
    f.write(song_artist + "," + song_artist +'\n')

f.close()
