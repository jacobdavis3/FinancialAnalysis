import yfinance as yf



class Stock:
    ...

history_periods = ['1d', '5d', '1mo', '3mo', '6mo', 
                     '1y', '2y', '5y', '10y', 'ytd', 'max'
                     ]
arm = yf.Ticker("ARM")
#his = arm.history(period='5y')


def calc_percentage(stock):  # figure out how to do type annotation
    history_periods = ['1d', '5d', '1mo', '3mo', '6mo', 
                     '1y', '2y', '5y', '10y', 'ytd', 'max'
                     ]
    for period in history_periods:
        timeframe = stock.history(period=period)
        
             

calc_percentage(arm)
########## What happens if I call 10y on a stock w/o that longevity, like ARM ####
## ARM: Period '5y' is invalid, must be one of ['1d', '5d', '1mo', '3mo', '6mo', '1y', 'ytd', 'max']
## Empty DataFrame

#arm = yf.Ticker("ARM")
#his = arm.history(period='5y')
#print(arm.history(period='5y'))

msft = yf.Ticker("MSFT")

msft_info = msft.info
#print(msft.history(period='5y'))



sp500 = yf.Ticker("^GSPC")
#print(sp500.info)