# etl/load.py
import pandas as pd

def load_data():
    df = pd.read_csv('data/processed/bank_account_fraud_clean.csv')
    # Load data into a database or further processing
    # Here, we will just print the first few rows as a placeholder
    print(df.head())

if __name__ == "__main__":
    load_data()
