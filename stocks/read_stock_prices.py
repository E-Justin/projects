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


stock_names = ['disney', 'apple', 'nvidia', 'ford', 'microsoft', 'levi']

stock_symbols = ['(DIS)', '(AAPL)', '(NVDA)', '(F)', '(MSFT)', '(LEVI)']


disney = Stock('(DIS)')
apple = Stock('(AAPL)')
nvidia = Stock('(NVDA)')
ford = Stock('(F)')
microsoft = Stock('(MSFT)')
levi = Stock('(LEVI)')

# open file for reading
f = open("Python\stock_prices.txt", 'r')

for line in f:
    # get totals of each price
    disney.set_total_current_prices(line)
    apple.set_total_current_prices(line)
    nvidia.set_total_current_prices(line)
    ford.set_total_current_prices(line)
    microsoft.set_total_current_prices(line)
    levi.set_total_current_prices(line)
    # set total price change
    disney.set_total_price_change(line)
    apple.set_total_price_change(line)
    nvidia.set_total_price_change(line)
    ford.set_total_price_change(line)
    microsoft.set_total_price_change(line)
    levi.set_total_price_change(line)
    # set total percent change
    disney.set_total_percent_change(line)
    apple.set_total_percent_change(line)
    nvidia.set_total_percent_change(line)
    ford.set_total_percent_change(line)
    microsoft.set_total_percent_change(line)
    levi.set_total_percent_change(line)

# close file
f.close()

# set average price change for each stock
disney.set_average_price_change()
apple.set_average_price_change()
nvidia.set_average_price_change()
ford.set_average_price_change()
microsoft.set_average_price_change()
levi.set_average_price_change()

# set average percent change of each stock
disney.set_average_percent_change()
apple.set_average_percent_change()
nvidia.set_average_percent_change()
ford.set_average_percent_change()
microsoft.set_average_percent_change()
levi.set_average_percent_change()

# set average price of each stock
disney.set_average_price()
apple.set_average_price()
nvidia.set_average_price()
ford.set_average_price()
microsoft.set_average_price()
levi.set_average_price()

# display average data
disney.display_average_data()
apple.display_average_data()
nvidia.display_average_data()
ford.display_average_data()
microsoft.display_average_data()
levi.display_average_data()

''' 
Todo:
1. 
2. 
3. get low and high price for each stock in file
4. fix formatting 
5. make reading/ math functions more efficient (work together instead of independently)'''
