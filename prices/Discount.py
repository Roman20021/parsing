import re
from bs4 import BeautifulSoup 
import requests
class Discount():
    def __init__(self, link):
        self.link = link
    def parse(self):      
        l = 0
        r = requests.get(self.link).text
        html = BeautifulSoup(r, 'lxml')
        for el in html.select('.buy-zone'):
            if l == 0:
                l = l + 1
                title = el.select('.old-price')
                title0 = el.select('.price')
        prise = title[0].text
        title = re.findall(r'\d+', prise)
        prise = title0[0].text
        title0 = re.findall(r'\d+', prise)
        return title0[0]
    def parse_discount(self):
        l = 0
        r = requests.get(self.link).content
        html = BeautifulSoup(r, 'lxml')
        for el in html.select('.buy-zone'):
            if l == 0:
                l = l + 1
                title_discount = el.select('.discount')
        prise_discount = title_discount[0].text
        title_discount = re.search(r'-(\d*)%', prise_discount)
        return title_discount.group(1)
    def parse_free(self):
        l = 0
        r = requests.get(self.link).content
        html = BeautifulSoup(r, 'lxml')
        for el in html.select('.buy-zone'):
            if l == 0:
                l = l + 1
                title_free = el.select('.notavailable-notice')
        prise_free = title_free[0].text
        title_free = re.findall(r'\w+\s+\w+', prise_free)
        title_free = title_free[0]
        return title_free  