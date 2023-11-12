from fastapi import FastAPI, UploadFile, File
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()

model_name = "blanchefort/rubert-base-cased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
sentiment_analyzer = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

@app.post("/analyze_sentiments/")
async def analyze_sentiments(file: UploadFile):
    text = await file.read()
    text = text.decode("utf-8")
    
    sentences = text.split('.')
    sentiments = [sentiment_analyzer(sentence)[0]['label'] for sentence in sentences if sentence]
    
    return {"sentiments": sentiments}


