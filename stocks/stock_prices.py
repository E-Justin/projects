from bs4 import BeautifulSoup
import requests
from datetime import datetime


# # gets date and time in this format : Mon Jun 13 11:09:53 2022
today = datetime.now().ctime()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
# list of stock symbols I want to get data for
stock_symbols = ['DIS', 'AAPL', 'NVDA', 'F', 'MSFT', 'LEVI']


def get_stock_info(symbol: str):
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
    f.write('\n%s : Name: %s, Price: %s, Price Change: %s, Percent Change: %s' %
            (today, stock_name, stock_price, price_change, percent_change))


# open file for appending/ creating if one does not already exist
f = open('stock_prices.txt', 'a+')
f.write(today)  # time/ date stamp
for symbol in stock_symbols:
    get_stock_info(symbol)
f.close()  # close file when done

'''to do:
* 
* alerts if a stock changes by more than a certain percent
* function to average price for each stock in .txt file
* 
* put all of this in a table/ excel sheet
* probably more '''
