# Imports
import os
import yfinance

from ..backend.app.database import SessionLocal, BronzeStock, Watchlist

def get_active_watchlist(): 
    with SessionLocal() as session: 
        tickers = session.query(Watchlist).filter(Watchlist.status == 'active').all()
        return [t.ticker for t in tickers]
    
def save_raw_data(ticker, data_frame): 
    with SessionLocal() as session: 
        payload_raw = data_frame.to_json()

        new_entry = BronzeStock(
            ticker = ticker, 
            raw_json = payload_raw
        )

        session.add(new_entry)
        session.commit()