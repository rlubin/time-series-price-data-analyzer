import pandas as pd


def convert_tradingview_screener_to_ticker_list(location):
    # print(location)
    data = pd.read_csv(location)
    # print(data["Ticker"])
    return data["Ticker"].tolist()
