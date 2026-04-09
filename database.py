import sqlalchemy as sa
from data_ingest import get_google_data
import pandas as pd

engine = sa.create_engine('sqlite:///stocks.db')

def create_table(df, df_name): 
    df.to_sql(f'{df_name}_data', engine, if_exists = 'replace', index = False)

def read_table(df_name):
    return pd.read_sql_table(df_name, engine)

def create_google_table():
    google_df = get_google_data()
    google_df.to_sql('google_data', engine, if_exists = 'replace', index = False)

def read_google_table(): 
    return pd.read_sql_table('google_data', engine)