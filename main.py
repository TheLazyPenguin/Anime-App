# Anime App
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QImage,QPixmap
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as BS
import asyncio
import cfscrape
import urllib.request
url_1="https://kissanime.ru"
url_2="https://kissanime.ru/AnimeList/NewAndHot"
url_3="https://kissanime.ru/AnimeList/Newest"
urls= []
new_IMG= []
def fetch(url): #url_1
    try:
        scraper = cfscrape.create_scraper()
        with closing(scraper.get(url, stream=True)) as resp:
            if response(resp):
                print("Fetched!")
                return(resp.content)
            else:
                print(response(resp))
                print(resp.status_code)

    except RequestException as err:
        log_error("Error during request to {0} : {1}".format(url,str(err)))

def response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200)

def log_error(err):
    print(err)

def parse(url):
    raw = fetch(url)
    html = BS(raw, 'html.parser')
    for i in html.find_all("span", class_='title'):
        print(i.get_text())
def NEWHOT(url): #url_2
    raw = fetch(url)
    html = BS(raw, 'html.parser')
    for i in html.find_all("tr", class_='odd'):
        i = i.get_text()
        i = " ".join(i.split())
        print(i)
        print("---------------------------------\n")

def NEWEST(url): #url_3
    raw = fetch(url)
    html = BS(raw, 'html.parser')
    for i in html.find_all("tr", class_='odd'):
        for a in i.find_all("a",href=True):
            urls.append(a['href'])
    for i in range(len(urls)):
        urls[i]= "https://kissanime.ru" + urls[i]
        for i in range(len(urls)):
            new_IMG.append(GETIMG(urls[i]))
    print(new_IMG)
def GETIMG(url):
    raw= fetch(url)
    html= BS(raw, 'html.parser')
    foo = html.find_all("div",class_="barContent")
    a = foo.find_all("img")
    print(a)
    print(foo['src'])
    return(foo['src'])
def GUI(url):
    app = QApplication([])
    urls = NEWEST(url)

    data = urllib.request.urlopen(url).read()
    label = QLabel('Hello World!')
    pixmap= QImage()
    pixmap.loadFromData(data)
    label.setPixmap(QPixmap(pixmap))
    label.show()
    app.exec_()

GUI(url_3)