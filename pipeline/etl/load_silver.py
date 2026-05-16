from .transform import transform
from ...backend.app.database import SilverStock
from sqlalchemy.dialetcts.postgresql import insert

def load_silver(ticker, df): 
    if dataframe.empty: 
        print(f"No data for {ticker}: Skipping...")
        return

    with SessionLocal() as session: 
        statement = 
