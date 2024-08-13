import yfinance as yf


class Stock:
    def __init__(self, ticker:str) -> None:
        self.attributes = yf.Ticker(ticker)

    def validRanges(self) -> None:
        ranges = self.attributes.history_metadata['validRanges']
        print(ranges)


def calc_percentage(stock:yf): 
    history_periods = ['1d', '5d', '1mo', '3mo', '6mo', 
                     '1y', '2y', '5y', '10y', 'ytd', 'max'
                     ]
    for period in history_periods:
        timeframe = stock.history(period=period)
        first_price = timeframe['Open'].iloc[0]
        last_price = timeframe['Close'].iloc[-1]
        difference = last_price - first_price
        percent_change = round(difference / first_price * 100, 2)
        percent_change_string = "{:,}".format(percent_change) + '%'
        print(f'{percent_change_string} - {period}')


def main():
    #msft = yf.Ticker("MSFT") 
    #hist = msft.history()
    #value = msft.history_metadata
    #print(value)
    #sp500 = yf.Ticker("^GSPC")            
    #calc_percentage(msft)
    #calc_percentage(sp500)
    msft = Stock("msft")
    msft.validRanges()
    #print(msft.attributes.history())


if __name__ == "__main__":
    main()