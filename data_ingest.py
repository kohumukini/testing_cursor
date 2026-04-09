import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def get_stock_data(ticker): 
    stock_data = yf.download(ticker, start = "2024-01-01", end = "2026-01-01")

    if isinstance(stock_data.columns, pd.MultiIndex): 
        stock_data.columns = stock_data.columns.get_level_values(0)

    stock_df = stock_data.reset_index()
    stock_df = stock_df[['Date', 'Open', 'Close', 'Volume']]

    return stock_df        