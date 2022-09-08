from bs4 import BeautifulSoup
import requests
from datetime import datetime


# # gets date and time in this format : Mon Jun 13 11:09:53 2022
today = datetime.now().ctime()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
# list of stock symbols I want to get data for
stock_symbols = ['DIS', 'AAPL','F', 'MSFT', 'UBER', 'LAC', 'LEVI', 'NVDA', ]
stock_ids =     [5    ,   6   , 7,    9,      10,     11,    13,     14]


def get_stock_info_by_pk(id: int):
    # stock symbol index matches stock ids in lists above
    symbol = stock_symbols[stock_ids.index(id)]

    # url: insert symbol to get specific stock data
    url = f'https://finance.yahoo.com/quote/{symbol}'
    source = requests.get(url, headers=headers)
    soup = BeautifulSoup(source.text, 'lxml')  # creating soup object

    stock_price = soup.find('fin-streamer',
                            {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text  # gets stock price from site
    price_change = soup.find('div', {'class': 'D(ib) Va(m) Maw(65%) Ov(h)'}).find_all('span')[
        0].text  # gets price change from site
    percent_change = soup.find('div', {'class': 'D(ib) Va(m) Maw(65%) Ov(h)'}).find_all('span')[
        1].text  # gets percent change from site

    # [stock_price, price_change, percent_change]
    return ([stock_price, price_change, percent_change[1:6]])

def get_stock_info_by_symbol(symbol: str):
    
    # url: insert symbol to get specific stock data
    url = f'https://finance.yahoo.com/quote/{symbol}'
    source = requests.get(url, headers=headers)
    soup = BeautifulSoup(source.text, 'lxml')  # creating soup object

    # gets stock name  from site
    stock_name = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text

    # remove symbol (not needed)
    stock_name = stock_name.split(' ')  # string -> list
    stock_name = stock_name[0: -1]  # removes last element
    stock_name = ' '.join(stock_name)  # list -> string

    # gets stock price from site
    stock_price = soup.find('fin-streamer',
                            {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text  

    # gets price change from site
    price_change = soup.find('div', {'class': 'D(ib) Va(m) Maw(65%) Ov(h)'}).find_all('span')[
        0].text  

    # gets percent change from site
    percent_change = soup.find('div', {'class': 'D(ib) Va(m) Maw(65%) Ov(h)'}).find_all('span')[
        1].text  

    
    # ['The Walt Disney Company', '112.73', '+0.04', '+0.04']
    return ([stock_name, stock_price, price_change, percent_change[1:6]])







