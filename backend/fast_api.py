from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
 
class request_body(BaseModel):
    symptoms: list

@api.post('/predict')
def predict(data: request_body):
    return {'class' : convert(data.symptoms)}

def convert(data):
    elements = diagnosis_vectorizer.inverse_transform(rf_classifier.predict(vectorizer.transform(data)))[0]
    return ','.join(element for element in elements)
 