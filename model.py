import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from database import read_table

def predict_tomorrows_price():
    df = read_table("google_features_data")

    features = df[['7-Day MA', 'Daily Return Raw']]
    target = df['Target']

    reg_model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.2, random_state = 23)

    reg_model.fit(X_train, y_train)

    predictions = reg_model.predict(X_test)
    # print(df.corr(numeric_only = True)) Checking correlation
    r_squared = r2_score(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)

    print(f"R2 Value: {r_squared}")
    print(f"Mean Squared Error: {mse}")

    new_df_data = features.tail(1)
    new_true_data = target.iloc[-1]

    new_pred = reg_model.predict(new_df_data)
    print(f"Predicted Values: {new_pred} \nActual: {new_true_data}")

    return new_pred, mse, r_squared