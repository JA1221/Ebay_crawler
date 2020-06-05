import requests
from bs4 import BeautifulSoup
import re
import time

url = 'https://www.ebay.com/itm/114035436630'

while True:
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    data = sp.find("span", {"id":"qtySubTxt"})
    data = data.get_text().lstrip()
    data = re.sub('[a-zA-Z \n]','',data)
    if data == '0':
        print(data,end = '')
    else:
        print(data)
    time.sleep(10)
