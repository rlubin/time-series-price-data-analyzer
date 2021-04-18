from AlphaVantageAPI import AlphaVantageAPI
from PriceData import PriceData
from tqdm import tqdm
from sp500 import SP500
import create_watchlist as cw
import os


def main():
    api = AlphaVantageAPI()
    # convert screener csv to list of tickers
    location = os.path.abspath(os.path.join(os.getcwd(), "tradingview_screen",
                                            "price_over_0.25_vol_over_100k_mktcap_50M_to_6B_CSE_TSX_TSVX.csv"))
    securities = cw.convert_tradingview_screener_to_ticker_list(
        location)
    # securities = SP500
    price_dfs = []
    # download whatever isn't downloaded
    # on_pc needs to be a list of name.csv strings

    on_pc = os.scandir(os.path.abspath(
        os.path.join(os.getcwd(), "price_data")))
    # on_pc = os.scandir('./price_data/')
    has = []
    for d in on_pc:
        name = os.path.splitext(d)[0]
        name = name[str(name).rfind('/')+1:]
        has.append(name)
    securities = [s for s in securities if s not in has]
    # download and save all data
    # create price_dfs from api
    for i in tqdm(range(len(securities))):
        df1 = PriceData(api.get_daily(
            securities[i]), securities[i]).df
        price_dfs.append(df1)
        df1.to_csv('./price_data/' + securities[i] + '.csv')


if __name__ == '__main__':
    main()
