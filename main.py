# Anime App
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QImage,QPixmap
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as BS
import asyncio
import cfscrape
import requests
import re
import urllib
url_1="https://kissanime.ru"
url_2="https://kissanime.ru/AnimeList/NewAndHot"
url_3="https://kissanime.ru/AnimeList/Newest"
urls= []
new_IMG= []
links = []
head= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                'Cookie': 'PHPSESSID=ldc1bp9mj7n4ocffvftm25te62'}
class HTML:

    def fetch(self,url): #url_1
        try:
            scraper = cfscrape.create_scraper()
            with closing(scraper.get(url, stream=True)) as resp:
                if self.response(resp):
                    print("Fetched!")
                    raw = resp.content
                    html = BS(raw, 'html.parser')
                    return html
                else:
                    print(self.response(resp))
                    print(resp.status_code)
        except RequestException as err:
                self.log_error("Error during request to {0} : {1}".format(url,str(err)))

    def response(self,resp):
        content_type = resp.headers['Content-Type'].lower()
        print(resp.status_code)
        return(resp.status_code == 200)

    def log_error(self,err):
        print(err)

def newhot(url): #url_2
    for i in html.find_all("tr"):
        i = i.get_text()
        i = " ".join(i.split())
        print(i)
        print("---------------------------------\n")
def getimg(url):
    wb = HTML()
    html = wb.fetch(url)
    foo = html.find_all("img")
    foo=str(foo)
    foo = "".join(foo)
    foo = foo.split('img height="100px"')
    n_h = foo[1:11]
    rec = foo[11:21]
    m_pop = foo[21:31]
    for i in range(len(n_h)):
        n_h[i] = (re.search('src="(.+?)"',n_h[i])).group(1)
        rec[i] = (re.search('src="(.+?)"',rec[i])).group(1)
        m_pop[i] = (re.search('src="(.+?)"',m_pop[i])).group(1)
    return n_h,rec,m_pop

def gui(url):
    urlgg= "https://kissanime.ru/Uploads/Etc/8-31-2018/543776545221170.jpg"
    scraper = cfscrape.create_scraper()
    data = scraper.get(urlgg, stream=True)
    print(data.status_code)
    data = data.raw.read()
    app = QApplication([])
    label = QLabel('Hello World!')
    pixmap= QImage()
    pixmap.loadFromData(data)
    label.setPixmap(QPixmap(pixmap))
    label.show()
    app.exec_()

gui(url_1)