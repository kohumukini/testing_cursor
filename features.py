import pandas as pd
from database import save_to_db, read_raw_data_table

def generate_features(ticker): 
    raw_data_df = read_raw_data_table(ticker)

    df = raw_data_df[['Date']].copy()

    df['7-Day MA'] = raw_data_df['Close'].rolling(window = 7).mean()
    df['Daily Raw Return'] = raw_data_df['Close'].pct_change()
    df['Daily Return %'] = (df['Daily Raw Return'] * 100).round(2)
    df['Target'] = raw_data_df['Close'].shift(-1)

    df.dropna(inplace = True)

    return df