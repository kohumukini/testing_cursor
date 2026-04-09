import streamlit as st
from data_ingest import get_google_data
from database import read_google_table
from model import predict_tomorrows_price

google_data = read_google_table()
chart_data = google_data.set_index('Date')[['Open', 'Close']]

st.title("Google Stock Price")
st.line_chart(chart_data)

prediction, mse, r2 = predict_tomorrows_price()
st.header("Tomorrow's Forecast")
st.metric(label = 'Predicted Close', value = f"${prediction[0]:.2f}")
st.write(f"MSE: {mse} \nR2 Value: {r2}")