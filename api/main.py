import joblib
import re
#ml import
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline
#Api import
from fastapi import FastAPI
from pydantic import BaseModel


# On crée notre instance FastApi puis on définit l'objet enstiment
app = FastAPI()
class Sentiment(BaseModel):
    sentiment: str
    sentiment_probability: float


# On crée notre pipeline
tokenizer = AutoTokenizer.from_pretrained("tblard/tf-allocine", use_fast=True)
model = TFAutoModelForSequenceClassification.from_pretrained("tblard/tf-allocine")

nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Nos différents endpoints

@app.get('/')
def get_root():
    return {'message': 'Welcome to the sentiment analysis API'}

@app.get('/predict/{message}',response_model=Sentiment)
async def predict(message: str):
   prediction_result = nlp(message)[0]
   return Sentiment(sentiment=prediction_result['label'], sentiment_probability=float(prediction_result['score']))