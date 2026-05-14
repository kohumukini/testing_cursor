# Imports
import os
import yfinance as yf

from ..backend.app.database import SessionLocal, BronzeStock, Watchlist

def get_active_watchlist(): 
    with SessionLocal() as session: 
        tickers = session.query(Watchlist).filter(Watchlist.status == 'active').all()
        return [t.ticker for t in tickers]
    
def save_raw_data(ticker, data_frame): 
    if data_frame.emtpy: 
        print(f"No data for {ticker}: Skipping... ")
        return

    with SessionLocal() as session: 
        payload_raw = data_frame.to_json()

        new_entry = BronzeStock(
            ticker = ticker, 
            raw_json = payload_raw
        )

        session.add(new_entry)
        session.commit()
        print(f"Saved {ticker} data")

def data_backfill(): 
    active_tickers = get_active_watchlist()

    for t in active_tickers: 
        with SessionLocal() as session:
            exists = session.query(BronzeStock).filter(BronzeStock.ticker == t).first()

            if exists: 
                ticker_data = yf.download(t, period="1h", interval="1m")
            else: 
                ticker_data = yf.download(t, period="5y", interval="1d")

            save_raw_data(t, ticker_data)
        
