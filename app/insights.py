import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def generate_insight(text: str, sentiment: str) -> str:
    prompt = (
        f"You are a marketing assistant. Based on the influencer's statement and sentiment, "
        f"write a short insight summary in professional tone.\n\n"
        f"Statement: {text}\n"
        f"Sentiment: {sentiment.upper()}\n"
        f"Insight:"
    )

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"Groq API error: {response.text}")

if __name__ == "__main__":
    print(generate_insight("This is the worst service I've ever had.", "NEGATIVE"))
