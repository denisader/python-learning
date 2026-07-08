import threading
import requests
from lxml import html
import time
import random

class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super().__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
    
    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break

            yahooFinanacePriceWorke = YahooFinanacePriceWorker(symbol=val)
            price = yahooFinanacePriceWorke.get_price()
            print(price)
            time.sleep(random.random())

class YahooFinanacePriceWorker():
    def __init__(self, symbol, **kwargs):
        self._symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{base_url}{self._symbol}'

    def get_price(self):
        r = requests.get(self._url, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code != 200:
            print(f'{self._symbol}: failed with status {r.status_code}')
            return
        page_contents = html.fromstring(r.text)
        page_text = page_contents.xpath('//*[@id="main-content-wrapper"]/section[1]/div[2]/div[1]/section/div/section[1]/div[1]/span[1]')[0].text
        price = float(page_text.replace(',', ''))
        return price
