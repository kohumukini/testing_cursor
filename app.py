import streamlit as st
from data_ingest import get_google_data
from database import read_google_table

google_data = read_google_table()
chart_data = google_data.set_index('Date')[['Open', 'Close']]

st.title("Google Stock Price")
st.line_chart(chart_data)
