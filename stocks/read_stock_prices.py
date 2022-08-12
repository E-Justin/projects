class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.average_price = 0
        self.count = 0
        self.total_prices = 0

    def set_total_prices(self, line):
        if self.symbol in line:  # DIS
            prices = float(line.split('#')[4])
            self.count += 1
            self.total_prices += prices

    def set_avg_price(self):
        self.average_price = self.total_prices / self.count

    def display_average_price(self):
        print("%s average price: %f" %
              (self.symbol, self.average_price, 2))


stock_names = ['disney', 'apple', 'nvidia', 'ford', 'microsoft', 'levi']

stock_symbols = ['(DIS)', '(AAPL)', '(NVDA)', '(F)', '(MSFT)', '(LEVI)']


disney = Stock('(DIS)')
apple = Stock('(AAPL)')
nvidia = Stock('(NVDA)')
ford = Stock('(F)')
microsoft = Stock('(MSFT)')
levi = Stock('(LEVI)')


f = open("stock_prices.txt", 'r')

# get totals of each price
for line in f:
    disney.set_total_prices(line)
    apple.set_total_prices(line)
    nvidia.set_total_prices(line)
    ford.set_total_prices(line)
    microsoft.set_total_prices(line)
    levi.set_total_prices(line)


f.close()

# get average price of each stock
disney.set_avg_price()
apple.set_avg_price()
nvidia.set_avg_price()
ford.set_avg_price()
microsoft.set_avg_price()
levi.set_avg_price()

# display average prices
disney.display_average_price()
apple.display_average_price()
nvidia.display_average_price()
ford.display_average_price()
microsoft.display_average_price()
levi.display_average_price()


''' 
Todo:
1. get avg price change
2. get avg percent change
3. get low and high price for each stock in file
4. fix formatting '''
