# etl/extract.py
import requests
import os

def extract_data():
    url = "https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022/download"
    os.makedirs('data/extracted', exist_ok=True)
    
    # Adjust the following lines based on actual download steps if necessary
    response = requests.get(url, stream=True)
    with open('data/extracted/bank_account_fraud.zip', 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    
    print("Data extraction complete. Data saved to 'data/extracted/bank_account_fraud.zip'")

if __name__ == "__main__":
    extract_data()
