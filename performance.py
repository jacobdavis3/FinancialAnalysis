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
            timeframe = self.attributes.history(period=period)
            first_price = timeframe['Open'].iloc[0]
            last_price = timeframe['Close'].iloc[-1]
            difference = last_price - first_price
            percent_change = '{:,}'.format(round(difference / first_price * 100, 2))
            self.print_color(percent_change, period)
            #print(f'{percent_change}% - {period}')


def main():
    msft = Stock("msft")
    sp = Stock("^GSPC")
    arm = Stock("arm")
    actu = Stock("actu")
    ambi = Stock("PBEV")
    ambi.calc_percentage()
    
    sp.valid_periods()
    #msft.calc_percentage()


if __name__ == "__main__":
    main()