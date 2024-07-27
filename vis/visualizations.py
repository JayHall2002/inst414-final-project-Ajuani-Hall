import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_visualizations():
    df = pd.read_csv('data/processed/bank_account_fraud_clean.csv')
    plt.figure(figsize=(10, 6))
    sns.countplot(x='fraud_label', data=df)
    plt.title('Fraud Label Distribution')
    plt.savefig('data/outputs/fraud_label_distribution.png')

if __name__ == "__main__":
    create_visualizations()
