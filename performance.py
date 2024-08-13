import yfinance as yf


class Stock:
    def __init__(self, ticker:str) -> None:
        self.attributes = yf.Ticker(ticker)


    def valid_periods(self) -> list:
        return self.attributes.history_metadata['validRanges']
        

    def calc_percentage(self) -> None: 
        for period in self.valid_periods():
            timeframe = self.attributes.history(period=period)
            first_price = timeframe['Open'].iloc[0]
            last_price = timeframe['Close'].iloc[-1]
            difference = last_price - first_price
            percent_change = '{:,}'.format(round(difference / first_price * 100, 2))
            print(f'{percent_change}% - {period}')


def main():
    msft = Stock("msft")
    sp = Stock("^GSPC")
    arm = Stock("arm")
    actu = Stock("actu")
    
    sp.valid_periods()
    msft.calc_percentage()


if __name__ == "__main__":
    main()