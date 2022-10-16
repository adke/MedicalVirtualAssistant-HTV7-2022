import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn import metrics
import pickle
# warnings.filterwarnings("ignore")

df = pd.read_csv("data.csv")

X = df[["symptoms"]]
y = df[["diagnoses"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

vectorizer = CountVectorizer(tokenizer = lambda x: x.split(','), binary="true")
symptom_train_data = vectorizer.fit_transform(X_train["symptoms"])
symptom_test_data = vectorizer.transform(X_test["symptoms"])
diagnosis_vectorizer = CountVectorizer(ngram_range=(1,1), stop_words="english")
diagnosis_train_data = diagnosis_vectorizer.fit_transform(y_train["diagnoses"])
diagnosis_test_data = diagnosis_vectorizer.fit_transform(y_test["diagnoses"])

rf_classifier = RandomForestClassifier()

rf_classifier = OneVsRestClassifier(rf_classifier)
rf_classifier.fit(symptom_train_data, diagnosis_train_data)

rf_predictions = rf_classifier.predict(symptom_test_data)
print(f"Accuracy: {metrics.accuracy_score(diagnosis_test_data, rf_predictions)}")

rf_hamming_loss = metrics.hamming_loss(diagnosis_test_data, rf_predictions)
print(f"Hamming loss: {rf_hamming_loss}")

