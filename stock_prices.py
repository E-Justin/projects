from bs4 import BeautifulSoup
import requests
from datetime import datetime
#import json
# import pandas as pd



today = datetime.now()
today = today.ctime() # gets date and time in user friendly format : Mon Jun 13 11:09:53 2022


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

url_dis = 'https://www.google.com/search?q=disney+stock+price+now&oq=disney+stock+price+now&aqs=chrome..69i57j0i22i30l9.7622j1j15&sourceid=chrome&ie=UTF-8'
url_appl = 'https://www.google.com/search?q=apple+stock+price+now&oq=apple+stock+price+now&aqs=chrome..69i57j0i22i30l9.2717j1j7&sourceid=chrome&ie=UTF-8'
url_nvida = 'https://www.google.com/search?q=nvida+stock+price+now&oq=nvida+stock+price+now&aqs=chrome..69i57.6212j1j7&sourceid=chrome&ie=UTF-8'
url_ford = 'https://www.google.com/search?q=ford+stock+price+now&oq=ford+stock+price+now&aqs=chrome..69i57j0i131i433i512l3j0i512l6.3353j1j7&sourceid=chrome&ie=UTF-8'
url_microsoft = 'https://www.google.com/search?q=microsoft+stock+price+now&oq=microsoft+stock+price+now&aqs=chrome..69i57j0i22i30l9.4354j1j7&sourceid=chrome&ie=UTF-8'

def get_stock_info(url:str):
    source = requests.get(url, headers=headers) 
    soup = BeautifulSoup(source.text, 'lxml') # creating soup object

    #page_text = soup.get_text()

    current_price = soup.find('span', {'class': 'IsqQVc NprOob wT3VGc'}).text
    change = soup.find('span', {'jsname': 'qRSVye'}).text
    stock_name = soup.find('span', {'role': 'heading'}).text

    print(today)
    print(stock_name)
    print(current_price)
    print(change)

    

    
    # write to file
    f.write("\n %s : %s : $%s : %s " % (today.rjust(26), stock_name.rjust(22), current_price.rjust(9), change.rjust(7)))
    


f = open("stock_prices.txt", "a+", encoding = "utf-8") # open file/ create if it does not already exist

get_stock_info(url_dis) #  get / write disney stock info
get_stock_info(url_appl) #  get / write apple stock info
get_stock_info(url_nvida) #  get / write nvida stock info
get_stock_info(url_ford) #  get / write ford stock info
get_stock_info(url_microsoft) #  get / write microsfot stock info

f.close() # close file when done'''


'''to do:
* 
* percent change
* function to average price for each stock in .txt file
* 
* put all of this in a table/ excel sheet
* probably more '''
