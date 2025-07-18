from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load tokenizer and model
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Label mapping
id2label = {
    0: "NEGATIVE",
    1: "NEUTRAL",
    2: "POSITIVE"
}

def predict_sentiment(text: str) -> dict:
    # Preprocess input
    encoded_input = tokenizer(text, return_tensors='pt')
    
    # Run model
    with torch.no_grad():
        output = model(**encoded_input)
        scores = F.softmax(output.logits, dim=1)[0]

    # Get top prediction
    label_id = torch.argmax(scores).item()
    confidence = round(scores[label_id].item(), 4)
    label = id2label[label_id]

    return {
        "text": text,
        "sentiment": label,
        "confidence": confidence
    }


if __name__ == "__main__":
    examples = [
        "I absolutely love this product!",
        "This is the worst service I've ever had.",
        "Meh. It's okay, not great."
    ]
    for sentence in examples:
        print(predict_sentiment(sentence))
