import streamlit as st
import pandas as pd
from data_ingest import get_stock_data
from database import save_to_db
from model import predict_tomorrows_price

ticker = st.selectbox("Choose a Stock", ['GOOG', 'AAPL', 'MSFT', 'TSLA'])

if st.button(f"Update and Predict {ticker}"): 
    raw_df = get_stock_data(ticker) 
    save_to_db(raw_df, ticker)
    prediction, mse, r2 = predict_tomorrows_price(ticker)
    st.title(f"{ticker} Stock Price")


try: 
    chart_data = raw_df.set_index('Date')[['Open', 'Close']]
    st.line_chart(chart_data)

    col1, col2, col3 = st.columns(3)
    col1.metric("Predicted Price", f"${prediction[0]:.2f}")
    col2.metric("R2 Score", f"{r2:.4f}")
    col3.metric("MSE", f"{mse:.2f}")
except NameError: 
    st.title("Please select and update a stock")


# google_data = read_google_table()
# chart_data = google_data.set_index('Date')[['Open', 'Close']]

# st.title("Google Stock Price")
# st.line_chart(chart_data)

# prediction, mse, r2 = predict_tomorrows_price()
# st.header("Tomorrow's Forecast")
# st.metric(label = 'Predicted Close', value = f"${prediction[0]:.2f}")
# st.write(f"MSE: {mse} \nR2 Value: {r2}")