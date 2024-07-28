# analysis/model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def build_model():
    df = pd.read_csv('data/processed/bank_account_fraud_clean.csv')
    X = df.drop('fraud_bool', axis=1)
    y = df['fraud_bool']
    
    # Ensure all features are numeric
    X = pd.get_dummies(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    print("Model training complete.")
    return model, X_test, y_test

if __name__ == "__main__":
    build_model()
