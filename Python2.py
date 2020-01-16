from iexfinance.stocks import Stock

aapl = Stock('WM')
x = aapl.get_quote()
print(x)
'why isn\'t this working'
