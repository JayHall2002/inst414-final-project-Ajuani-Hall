# etl/extract.py
import os
from kaggle.api.kaggle_api_extended import KaggleApi

def extract_data():
    api = KaggleApi()
    api.authenticate()
    
    dataset = 'sgpjesus/bank-account-fraud-dataset-neurips-2022'
    path = 'data/extracted'
    os.makedirs(path, exist_ok=True)
    
    api.dataset_download_files(dataset, path=path, unzip=True)
    
    print("Data extraction complete. Files saved to 'data/extracted/'")

if __name__ == "__main__":
    extract_data()
