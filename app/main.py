from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.sentiment import classify_sentiment
from app.insight import generate_insight

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StatementRequest(BaseModel):
    text: str

class AnalysisResponse(BaseModel):
    text: str
    sentiment: str
    confidence: float
    insight: str

@app.post("/analyze", response_model=AnalysisResponse)
def analyze_statement(request: StatementRequest):
    sentiment_result = classify_sentiment(request.text)
    sentiment = sentiment_result["sentiment"]
    confidence = sentiment_result["confidence"]
    
    insight = generate_insight(request.text, sentiment)

    return AnalysisResponse(
        text=request.text,
        sentiment=sentiment,
        confidence=confidence,
        insight=insight
    )
