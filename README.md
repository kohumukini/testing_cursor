# Stock Trend Predictor 📈

A modular Python application that fetches financial data, processes technical indicators, and uses Linear Regression to predict next-day closing prices.

## 🚀 Features
- **Data Ingest**: Automated fetching via `yfinance`.
- **Database**: Local SQLite storage using `SQLAlchemy`.
- **ML Model**: Scikit-Learn Linear Regression predicting price targets.
- **UI**: Interactive dashboard built with `Streamlit`.

## 🛠️ Installation
```bash
   git clone [https://github.com/kohumukini/yfinance-predictor.git](https://github.com/kohumukini/yfinance-predictor.git)

   pip install yfinance pandas sqlalchemy streamlit scikit-learn

   streamlit run app.py