import requests
import os.path
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

import random
import string


def SavesScreenShot(url):
    if (url is None):
        return
    filename = url.split('/')[-1]
    try:
       r = requests.get(url, allow_redirects=True)
       open(os.path.join(os.getcwd(),"downloaded",filename), 'wb').write(r.content)
    except:
        pass


def SaveHtml(reg_url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    req = Request(url=reg_url, headers=headers)
    try:
      html = urlopen(req).read()
      return html
    except:
        pass
    
def ParseUrl(html):
    if (html is None):
        return
    soup = BeautifulSoup(html)
    images = soup.find('img')
    return images['src'] 

def GenerateUrl():
    return ''.join(random.sample(string.ascii_lowercase, 4))