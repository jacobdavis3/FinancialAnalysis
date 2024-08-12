import yfinance as yf



class Stock:
    ...

history_periods = ['1d', '5d', '1mo', '3mo', '6mo', 
                     '1y', '2y', '5y', '10y', 'ytd', 'max'
                     ]

########## What happens if I call 10y on a stock w/o that longevity, like ARM ####

msft = yf.Ticker("MSFT")

msft_info = msft.info
print(msft.history(period='1mo'))



sp500 = yf.Ticker("^GSPC")
#print(sp500.info)