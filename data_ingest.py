import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def get_google_data(): 
    google_data = yf.download("GOOG", start = "2024-01-01", end = "2026-01-01")
    google_df = google_data.reset_index()
    google_df = google_df[['Date', 'Open', 'Close', 'Volume']]
    return google_df
