class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.average_price = 0
        self.count = 0
        self.total_prices = 0
        self.total_price_change = 0
        self.total_percent_change = 0
        self.average_price_change = 0
        self.average_percent_change = 0

    def set_total_current_prices(self, line):
        if self.symbol in line:   # if symbol is in line
            prices = float(line.split('#')[4])  # get price for that line
            self.count += 1  # tally instances of specific stock
            self.total_prices += prices

    def set_total_price_change(self, line):
        if self.symbol in line:
            self.total_price_change += float(line.split('#')[6])

    def set_total_percent_change(self, line):
        if self.symbol in line:
            self.total_percent_change += float(line.split('#')[8][2:-3])

    def set_average_percent_change(self):
        self.average_percent_change = self.total_percent_change / self.count

    def set_average_price(self):
        self.average_price = self.total_prices / self.count

    def set_average_price_change(self):
        self.average_price_change = self.total_price_change / self.count

    def display_average_data(self):
        print("%s : Average Current Price = %f : Average Price change = %f : Average Percent change = %f" % (
            self.symbol, self.average_price, self.average_price_change, self.average_percent_change))


stock_symbols = ['(DIS)', '(AAPL)', '(NVDA)', '(F)', '(MSFT)', '(LEVI)']


disney = Stock('(DIS)')
apple = Stock('(AAPL)')
nvidia = Stock('(NVDA)')
ford = Stock('(F)')
microsoft = Stock('(MSFT)')
levi = Stock('(LEVI)')

stock_names = [disney, apple, nvidia, ford, microsoft, levi]

# open file for reading
f = open("Python\stock_prices.txt", 'r')

for line in f:

    # get totals of each price
    for stock in stock_names:
        stock.set_total_current_prices(line)
        stock.set_total_price_change(line)
        stock.set_total_percent_change(line)


# close file
f.close()

# set averages for: price change, percent change, and current price
for stock in stock_names:
    stock.set_average_price_change()
    stock.set_average_percent_change()
    stock.set_average_price()


# display average data
for stock in stock_names:
    stock.display_average_data()


''' 
Todo:
1. 
2. 
3. get low and high price for each stock in file
4. fix formatting 
5. start date of the data
6. end date of the data
7. make functions more efficient (work together instead of independently'''
