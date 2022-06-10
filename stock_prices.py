from bs4 import BeautifulSoup
import requests
from datetime import datetime
# import pandas as pd

today = datetime.now()
today = today.ctime() # gets date in this format: Fri Jun 10 08:50:57 2022

stock_name = str

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

url = 'https://www.google.com/search?q=disney+stock+price+now&oq=disney+stock+price+now&aqs=chrome..69i57j0i22i30l9.7622j1j15&sourceid=chrome&ie=UTF-8'
source = requests.get(url, headers=headers) 
soup = BeautifulSoup(source.text, 'lxml') # creating soup object

#page_text = soup.get_text()

current_price = soup.find('span', {'class': 'IsqQVc NprOob wT3VGc'}) # the price is found in a <span with this class name
# print(current_price.get_text())












f = open("stock_prices.txt", "a+")
f.write("\n %s : $%s " % (today, current_price.get_text()))
f.close()

'''to do:
* add more stocks
* open and closing price
* how much it went up/ down from the previous day
* 
* put all of this in a table/ excel sheet
* probably more '''


