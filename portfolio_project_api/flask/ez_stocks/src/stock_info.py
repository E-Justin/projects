from bs4 import BeautifulSoup
import requests
from datetime import datetime


# # gets date and time in this format : Mon Jun 13 11:09:53 2022
today = datetime.now().ctime()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
# list of stock symbols I want to get data for
stock_symbols = ['DIS', 'AAPL','F', 'MSFT', 'UBER',  'LEVI', 'NVDA', ]
stock_ids =     [5    ,   6   , 7,  9, 10]


def get_stock_info(id: int):
    symbol = stock_symbols[stock_ids.index(id)]
    # url: insert symbol to get specific stock data
    url = f'https://finance.yahoo.com/quote/{symbol}'
    source = requests.get(url, headers=headers)
    soup = BeautifulSoup(source.text, 'lxml')  # creating soup object

    # gets stock name from site
    stock_name = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
    stock_price = soup.find('fin-streamer',
                            {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text  # gets stock price from site
    price_change = soup.find('div', {'class': 'D(ib) Va(m) Maw(65%) Ov(h)'}).find_all('span')[
        0].text  # gets price change from site
    percent_change = soup.find('div', {'class': 'D(ib) Va(m) Maw(65%) Ov(h)'}).find_all('span')[
        1].text  # gets percent change from site

    print('Getting data for %s...' % (stock_name))
    
    return ([stock_price, price_change, percent_change[1:6]])





