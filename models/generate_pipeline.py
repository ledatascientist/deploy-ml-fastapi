from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline
from joblib import dump


tokenizer = AutoTokenizer.from_pretrained("tblard/tf-allocine", use_fast=True)
model = TFAutoModelForSequenceClassification.from_pretrained("tblard/tf-allocine")


nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
#Dump 
dump(nlp, 'models/dumps/sentiment_classifier.joblib')