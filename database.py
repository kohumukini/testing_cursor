import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine('sqlite:///stocks.db')

def read_raw_data_table(ticker): 
    return pd.read_sql_table(f"{ticker}_raw_data", engine)

def save_to_db(raw_df, ticker): 
    raw_df.to_sql(f'{ticker}_raw_data', engine, if_exists = 'replace', index = False)    