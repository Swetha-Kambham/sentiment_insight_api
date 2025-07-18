# Sentiment Insight API 🔍🧠

A FastAPI-based backend that performs sentiment analysis on influencer statements and generates AI-powered insight summaries using LLaMA 3 (Groq) and CardiffNLP.

---

## 🚀 Features

- 🔎 Sentiment classification using `cardiffnlp/twitter-roberta-base-sentiment`
- 🧠 Insight generation using `Groq` + `LLaMA 3`
- 📦 FastAPI backend with Swagger Docs (`/docs`)

---

## 📦 Tech Stack

- Python 3.11
- FastAPI
- Hugging Face Transformers
- CardiffNLP (sentiment)
- Groq API (insight generation via LLaMA 3)
- Uvicorn

---

## 📂 Project Structure

```
sentiment_insight_api/
├── app/
│   ├── main.py
│   ├── sentiment.py
│   └── insight.py
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

```bash
# 1. Clone repo
git clone https://github.com/YOUR_USERNAME/sentiment_insight_api.git
cd sentiment_insight_api

# 2. Create virtual env
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run API
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` to test or you can use Postman

---

## 🧪 Example Request

```json
POST /analyze
{
  "text": "This is the worst service I've ever had."
}
```

### ✅ Response:

```json
{
  "text": "This is the worst service I've ever had.",
  "sentiment": "NEGATIVE",
  "confidence": 0.9829,
  "insight": "The influencer's negative sentiment toward a particular service suggests..."
}
```