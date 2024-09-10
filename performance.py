import yfinance as yf


class Stock:
    def __init__(self, ticker:str) -> None:
        self.attributes = yf.Ticker(ticker)


    def valid_periods(self) -> list:
        return self.attributes.history_metadata['validRanges']
    

    def print_color(self, percent:str, period:str) -> None:
        if percent == '0.0':
            print(f'{percent}% - {period}')
        elif percent[0] == '-':
            print(f'\033[31;1m{percent}% - {period}\033[0m')
        else:
            print(f'\033[32;1m{percent}% - {period}\033[0m')
        

    def calc_percentage(self) -> None: 
        for period in self.valid_periods():
            timeframe = self.attributes.history(period=period, actions=True)
            first_price = timeframe['Open'].iloc[0]
            last_price = timeframe['Close'].iloc[-1]
            if period == '1d':
                print(round(first_price, 2), round(last_price, 2))
            difference = last_price - first_price
            percent_change = '{:,}'.format(round(difference / first_price * 100, 2))
            self.print_color(percent_change, period)
            #print(f'{percent_change}% - {period}')
    

    def acqusition_timelines(self) -> None:
        time = self.attributes.history(start='2003-02-02')
        first_price = time['Open'].iloc[0]
        last_price = time['Close'].iloc[-1]
        difference = last_price - first_price
        percent_change = '{:,}'.format(round(difference / first_price * 100, 2))
        self.print_color(percent_change, 'yeet')
        


def main():
    msft = Stock("msft")
    sp = Stock("^GSPC")
    arm = Stock("arm")
    apple = Stock("AAPL")
    actu = Stock("actu")
    ambi = Stock("PBEV")
    msft.calc_percentage()
    apple.calc_percentage()
    #msft.acqusition_timelines()
    #sp.calc_percentage()
    
    sp.valid_periods()
    #msft.calc_percentage()


if __name__ == "__main__":
    main()