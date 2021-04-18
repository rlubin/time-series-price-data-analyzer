'''
this wrapper class will be used to call alphavantage API
dox link
https://www.alphavantage.co/documentation/
only allows 5 api calls per minute with 500 calls per day
'''
import requests
import json
import time

thang = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=5ZC0WWZ6635PJYOT'


class AlphaVantageAPI:

    def __init__(self):
        self.key = '5ZC0WWZ6635PJYOT'
        # 5 calls per minute means 1 api call every 12 seconds + 1 second to be safe
        self.timer = (60/5)+1
        self.counter = 0

    # return price by the day data as json
    def get_daily(self, symbol, outputsize='full'):
        if self.counter >= 500:
            print('maximum queries reached')
            return {}
        time.sleep(self.timer)
        response = requests.get(
            f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize={outputsize}&apikey={self.key}')
        # print(response.json().keys())
        if('Time Series (Daily)' not in list(response.json().keys())):
            print('error')
            return {}
        # print(type(response.json()))
        self.counter += 1
        return (response.json()['Time Series (Daily)'])
