import yfinance as yf
from datetime_util import convertDatetoMinutes

class RefData:
    def __init__(self, tickers, interval, period):
        '''
        Get quotes from yahoo finance
        :param tickers: List of tickers seperated by space
        :param start: start date
        :param end: end date
        :param period: Frequency of quotes
        :return: DF of prices
        '''
        self.quotes = yf.download(tickers=tickers, interval=interval, period=period)
        self.vix = self.quotes['Close']
        self.vix.index = convertDatetoMinutes(self.vix.index)

