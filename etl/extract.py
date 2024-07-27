import requests
import os

def extract_data():
    url = "https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022"
    os.makedirs('data/extracted', exist_ok=True)
    response = requests.get(url)
    with open('data/extracted/bank_account_fraud.csv', 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    extract_data()
