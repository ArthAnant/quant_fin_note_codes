import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as sco

#Stocks
stocks = ['AAPL', 'GS', 'TGT', 'NFLX', 'NVDA', 'GM']

#start and end dates
start_date = '2020-01-01'
end_date = '2025-01-01'

#download stock data
def download_data():
    stock_data = {}
    for stock in stocks:
        ticker = yf.Ticker(stock)
        stock_data[stock] = ticker.history(start=start_date, end=end_date)['Close']
    return pd.DataFrame(stock_data)

def plot_data(data):
    data.plot(figsize=(10, 5))
    plt.show()

if __name__ == "__main__":
    dataset = download_data()
    plot_data(dataset)