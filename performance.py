import yfinance as yf



class Stock:
    ...


def calc_percentage(stock):  # figure out how to do type annotation
    history_periods = ['1d', '5d', '1mo', '3mo', '6mo', 
                     '1y', '2y', '5y', '10y', 'ytd', 'max'
                     ]
    for period in history_periods:
        timeframe = stock.history(period=period)
        first_price = timeframe['Open'].iloc[0]
        last_price = timeframe['Close'].iloc[-1]
        difference = last_price - first_price
        percent_change = difference / first_price * 100
        print(f'{percent_change}% - {period}')


def main():
    msft = yf.Ticker("MSFT") 
    sp500 = yf.Ticker("^GSPC")            
    calc_percentage(msft)
    calc_percentage(sp500)


if __name__ == "__main__":
    main()