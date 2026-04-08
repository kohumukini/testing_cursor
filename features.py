import pandas as pd
from database import read_google_table, create_table

def google_features(): 
    name = "google_features"
    google_df = read_google_table()

    # Create a copy
    df = google_df[['Date']].copy()

    # Moving Average
    df['7-Day MA'] = google_df['Close'].rolling(window = 7).mean()

    # Daily Returns
    df['Daily Return Raw'] = google_df['Close'].pct_change()

    # Human Daily Return Readability
    df['Daily Return %'] = (df['Daily Return Raw'] * 100).round(2)

    # Target - What happened next?
    df['Target'] = google_df['Close'].shift(-1)
    df.dropna(inplace = True)

    return df, name

def upload_features(df, df_name): 
    create_table(df, df_name)

df, name = google_features()
upload_features(df, name)