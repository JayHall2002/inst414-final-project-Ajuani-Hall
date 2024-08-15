from sklearn.metrics import classification_report
from .model import build_model
import logging

logging.basicConfig(level=logging.INFO)

def evaluate_model():
    logging.info("Building and training model...")
    model, X_test, y_test = build_model()
    
    logging.info("Predicting...")
    y_pred = model.predict(X_test)
    
    logging.info("Evaluating model...")
    report = classification_report(y_test, y_pred)
    print(report)
    logging.info("Evaluation complete.")

if __name__ == "__main__":
    evaluate_model()
