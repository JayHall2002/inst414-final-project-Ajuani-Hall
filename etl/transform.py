# etl/transform.py
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

def transform_data():
    os.makedirs('data/processed', exist_ok=True)
    
    # Load the CSV files
    base_df = pd.read_csv('data/extracted/Base.csv')
    variant_i_df = pd.read_csv('data/extracted/Variant I.csv')
    variant_ii_df = pd.read_csv('data/extracted/Variant II.csv')
    variant_iii_df = pd.read_csv('data/extracted/Variant III.csv')
    variant_iv_df = pd.read_csv('data/extracted/Variant IV.csv')
    variant_v_df = pd.read_csv('data/extracted/Variant V.csv')
    
    # Combine the dataframes if necessary
    df = pd.concat([base_df, variant_i_df, variant_ii_df, variant_iii_df, variant_iv_df, variant_v_df])
    
    # Data cleaning steps
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    # EDA: Visualize the distribution of the fraud labels
    plt.figure(figsize=(10, 6))
    sns.countplot(x='fraud_bool', data=df)  # Update 'fraud_label' to 'fraud_bool'
    plt.title('Fraud Label Distribution')
    plt.savefig('data/outputs/fraud_label_distribution.png')
    plt.show()

    # Save the cleaned data
    df.to_csv('data/processed/bank_account_fraud_clean.csv', index=False)
    print("Data transformation complete. Clean data saved to 'data/processed/bank_account_fraud_clean.csv'")

if __name__ == "__main__":
    transform_data()
