import pandas as pd
import os

def transform_data():
    os.makedirs('data/processed', exist_ok=True)
    df = pd.read_csv('data/extracted/bank_account_fraud.csv')
    # Add data cleaning and transformation steps here
    df.to_csv('data/processed/bank_account_fraud_clean.csv', index=False)

if __name__ == "__main__":
    transform_data()
