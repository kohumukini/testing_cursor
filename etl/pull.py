
def sync_watchlist():
    tickers = db.query(Watchlist).filter(status = "active")

    for ticker in tickers: 