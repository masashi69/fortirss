#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import time

url = 'https://fortiguard.com/rss/ir.xml'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'xml') 

items = soup.find_all('item')

n = 1
for content in items:

    time.sleep(3)
    detail = requests.get(content.link.text)
    
    soup = BeautifulSoup(detail.text, 'html.parser')
    
    for affected_ver in soup.find_all('div', class_='detail-item'):
        if 'Affected Products' in affected_ver.text:
        
            print(""" 
    --- No. {} ---
    Titile: {}
    Date: {}
    Link: {}
    Affected Ver: {}
    """.format(n, content.title.text, content.pubDate.text, content.link.text, 
        affected_ver.text.replace("\n", "\n\t")))
        
    time.sleep(3)
    n += 1
