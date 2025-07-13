from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import joblib
from pathlib import Path



def prepare(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size = 0.2, random_state=101, stratify=y)
    return X_train, X_test, y_train, y_test

def train(X_train, y_train):
    logit = LogisticRegression()
    return logit.fit(X_train, y_train)

def predict(model, data):
    return model.predict(data)

def report(y_true, y_cap):
    print(confusion_matrix(y_true, y_cap))
    print()
    print(classification_report(y_true, y_cap))
    print()
    print(accuracy_score(y_true, y_cap))
    print()

def save_model(model, path, name):
    Path(path[:-1]).mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path+name+'.pkl')





