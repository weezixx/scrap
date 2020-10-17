import requests
from bs4 import BeautifulSoup
import re
import wget

URL = 'https://radio-podcast.fr/podcast/france-culture/1907/la-conversation-scientifique/etienne-klein'

page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

soup = str(soup)

url = re.findall("http://rf.proxycast.org+\/+[A-Za-z0-9_-]{1,100}\/[A-Za-z0-9_-]{1,}\.[A-Za-z0-9_-]{1,}\.[A-Za-z0-9_-]{1,}\.mp3", soup)

#http://rf.proxycast.org/5dda516c-eb56-4632-832b-9221d203b030/13957-17.10.2020-ITEMA_22457933-2020C22785E0031.mp3

#<div class="h4 titre-0">Louis Lachenal ou la résurrection d’un alpiniste</div>

titre = re.findall("h4 titre-[0-9]{1,}\"+\>+[A-Za-z0-9'’\-\ \-\'\"\ê\é\è\à\&\ù\ç,()«»]{1,}",soup)


print(titre)
