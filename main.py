import requests
from bs4 import BeautifulSoup
import re
import wget

URL = 'https://radio-podcast.fr/podcast/france-culture/1907/la-conversation-scientifique/etienne-klein'

page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

soup = str(soup)

url = re.findall("https://rf.proxycast.org+\/+[A-Za-z0-9_-]{1,100}\/[A-Za-z0-9_-]{1,}\.[A-Za-z0-9_-]{1,}\.[A-Za-z0-9_-]{1,}\.mp3", soup)

print(len(url))
