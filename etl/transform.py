# etl/transform.py
import pandas as pd
import os

def transform_data():
    os.makedirs('data/processed', exist_ok=True)
    
    # Load the first CSV file
    base_df = pd.read_csv('data/extracted/Base.csv')
    
    # Print the column names to identify the correct column for the fraud label
    print(base_df.columns)
    
    # Combine the dataframes if necessary (assuming the column structure is similar)
    df = pd.concat([
        base_df,
        pd.read_csv('data/extracted/Variant I.csv'),
        pd.read_csv('data/extracted/Variant II.csv'),
        pd.read_csv('data/extracted/Variant III.csv'),
        pd.read_csv('data/extracted/Variant IV.csv'),
        pd.read_csv('data/extracted/Variant V.csv')
    ])
    
    # Data cleaning steps
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    # Save the cleaned data
    df.to_csv('data/processed/bank_account_fraud_clean.csv', index=False)
    print("Data transformation complete. Clean data saved to 'data/processed/bank_account_fraud_clean.csv'")

if __name__ == "__main__":
    transform_data()
