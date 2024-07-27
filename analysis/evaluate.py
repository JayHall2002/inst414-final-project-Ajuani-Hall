from sklearn.metrics import classification_report
from .model import build_model

def evaluate_model():
    model, X_test, y_test = build_model()
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model()
