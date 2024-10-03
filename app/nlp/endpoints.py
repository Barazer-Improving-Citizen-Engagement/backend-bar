from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google.cloud import language_v1
from google.oauth2 import service_account
import os

nlp_router = APIRouter()

# Configure Google Cloud credentials
credentials = service_account.Credentials.from_service_account_file(
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
)
client = language_v1.LanguageServiceClient(credentials=credentials)

class Feedback(BaseModel):
    text: str

@nlp_router.post("/analyze")
def analyze_feedback(feedback: Feedback):
    try:
        document = language_v1.Document(content=feedback.text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        return {
            "text": feedback.text,
            "sentiment_score": sentiment.score,
            "sentiment
