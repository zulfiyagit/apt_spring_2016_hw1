from bottle import route, run, template
import requests
from bs4 import BeautifulSoup
import os 


@route('/')
def index():
    URL = "http://public.mig.kz/"
    resp = requests.get(URL)
    bs4 = BeautifulSoup(resp.content, "html.parser")
    sell = []
    i=0
    table = bs4.find('table')
    for tr in table.find_all('tr'):
        for tag in tr.find_all('td', {'class': 'sell delta-neutral'}):
            
            sell.append(tag.string)
            i+=1
        
    return {"USD": sell[0], "EUR": sell[1], "RUB": sell[2], "KGS": sell[3], "GBP": sell[4], "CNY": sell[5], "CHF": sell[6]}
        
        
    

URL = "https://github.com/giAtSDU/apt_spring_2016_hw1"

@route('/forks')
def forks():
    resp = requests.get(URL)
    bs4 = BeautifulSoup(resp.content, "html.parser")
    res = None
    for tag in bs4.find_all('a'):
        if tag.has_attr('class') and 'social-count' in tag.attrs['class']:
            res = int(tag.string)
    return {"forks": res}

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

