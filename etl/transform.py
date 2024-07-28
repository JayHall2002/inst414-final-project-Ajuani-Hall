# etl/transform.py
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

def transform_data():
    os.makedirs('data/processed', exist_ok=True)
    
    # Load the CSV file
    df = pd.read_csv('data/extracted/fraudTest.csv')
    
    # Data cleaning steps
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    # EDA: Visualize the distribution of the fraud labels
    plt.figure(figsize=(10, 6))
    sns.countplot(x='is_fraud', data=df)
    plt.title('Fraud Label Distribution')
    plt.savefig('data/outputs/fraud_label_distribution.png')
    plt.show()

    # Save the cleaned data
    df.to_csv('data/processed/bank_account_fraud_clean.csv', index=False)
    print("Data transformation complete. Clean data saved to 'data/processed/bank_account_fraud_clean.csv'")

if __name__ == "__main__":
    transform_data()
