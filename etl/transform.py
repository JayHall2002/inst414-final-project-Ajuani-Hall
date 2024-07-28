# etl/transform.py
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

def transform_data():
    """
    Transform the extracted data by cleaning, processing, and visualizing it.

    This function performs the following steps:
    - Load the CSV files.
    - Combine the dataframes.
    - Clean the data by removing missing values and duplicates.
    - One-hot encode categorical variables.
    - Visualize the distribution of the fraud labels.
    - Save the cleaned and processed data.
    """
    # Ensure the necessary directories exist
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('data/outputs', exist_ok=True)
    
    # Load the CSV files
    base_df = pd.read_csv('data/extracted/Base.csv')
    variant_i_df = pd.read_csv('data/extracted/Variant I.csv')
    variant_ii_df = pd.read_csv('data/extracted/Variant II.csv')
    variant_iii_df = pd.read_csv('data/extracted/Variant III.csv')
    variant_iv_df = pd.read_csv('data/extracted/Variant IV.csv')
    variant_v_df = pd.read_csv('data/extracted/Variant V.csv')
    
    # Combine the dataframes
    df = pd.concat([base_df, variant_i_df, variant_ii_df, variant_iii_df, variant_iv_df, variant_v_df])
    
    # Data cleaning steps
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    # One-hot encode categorical variables
    categorical_features = ['employment_status', 'payment_type', 'housing_status', 'source', 'device_os']
    df = pd.get_dummies(df, columns=categorical_features, drop_first=True)
    
    # EDA: Visualize the distribution of the fraud labels
    plt.figure(figsize=(10, 6))
    sns.countplot(x='fraud_bool', data=df)
    plt.title('Fraud Label Distribution')
    plt.savefig('data/outputs/fraud_label_distribution.png')
    plt.show()

    # Save the cleaned and processed data
    df.to_csv('data/processed/bank_account_fraud_clean.csv', index=False)
    print("Data transformation complete. Clean data saved to 'data/processed/bank_account_fraud_clean.csv'")

if __name__ == "__main__":
    transform_data()
