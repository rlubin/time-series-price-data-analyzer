'''
takes price data and converts it to a pandas dataframe
'''

import pandas as pd


class PriceData:

    # convert alphavantage api response into pandas dataframe=['datetime', 'open', 'high', 'low', 'close', 'volume']
    def __init__(self, price_data, name, period='250'):
        self.name = name
        self.price_data = price_data
        df = pd.DataFrame(
            columns=['open', 'high', 'low', 'close', 'volume', 'symbol'])
        i = 0
        for date in price_data:
            # currently limited data to period because constructing a pandas dataframe is sooooo fucking expensive
            if(i == period):
                break
            i += 1
            row = pd.DataFrame(
                {'datetime': pd.Timestamp(date), 'open': price_data[date]['1. open'], 'high': price_data[date]['2. high'],
                 'low': price_data[date]['3. low'], 'close': price_data[date]['4. close'], 'volume': price_data[date]['5. volume'], 'symbol': name}, index=[pd.Timestamp(date)])
            row.set_index('datetime')
            row = row.drop(columns='datetime')
            df = pd.concat([df, row])
        df['open'] = df['open'].astype(float)
        df['high'] = df['high'].astype(float)
        df['low'] = df['low'].astype(float)
        df['close'] = df['close'].astype(float)
        df['volume'] = df['volume'].astype(float)
        df['symbol'] = df['symbol'].astype(str)
        self.df = df
