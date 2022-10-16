import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ml_model import diagnosis_vectorizer, rf_classifier, vectorizer

api = FastAPI()

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
origins = ["http://localhost:3000",
            "localhost:3000"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
class request_body(BaseModel):
    symptoms: list

@api.post('/predict')
def predict(data: request_body):
    return {'class' : convert(filter_words(data.symptoms))}

def filter_words(data):
    words = word_tokenize(data[0])
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.casefold() not in stop_words]
    return filtered_words

def convert(data):
    elements = diagnosis_vectorizer.inverse_transform(rf_classifier.predict(vectorizer.transform(data)))[0]
    return ', '.join(element.title() for element in elements)
 