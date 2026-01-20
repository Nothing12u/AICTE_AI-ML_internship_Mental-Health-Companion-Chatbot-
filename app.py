from flask import Flask, render_template, request, jsonify
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import re
import logging
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False,
    top_k=1
)

CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end it all", "no reason to live",
    "hurt myself", "cutting", "overdose", "die", "can't go on"
]

RESPONSE_TEMPLATES = {
    "anger": [
        "I hear your frustration. It’s okay to feel angry—would you like to talk about what’s bothering you?",
        "That sounds really unfair. Want to vent a bit more?"
    ],
    "fear": [
        "It sounds like you're feeling overwhelmed. You're not alone—I'm here with you.",
        "Anxiety can feel so heavy. Would a quick breathing exercise help right now?"
    ],
    "joy": [
        "I'm so glad you're feeling good!  What made today special?",
        "Your positivity is contagious! Keep holding onto that."
    ],
    "sadness": [
        "I'm really sorry you're feeling this way. Your feelings are valid.",
        "It’s okay to not be okay. Would you like a gentle mindfulness tip?"
    ],
    "surprise": [
        "Wow! That sounds unexpected. How are you feeling about it?",
        "Life can be full of surprises—good or tough. Want to unpack this together?"
    ],
    "neutral": [
        "Thanks for sharing. How are you feeling overall today?",
        "I'm here whenever you need to talk—no judgment, just support."
    ]
}

COPING_TIPS = {
    "breathing": "Try box breathing: Inhale 4 sec → Hold 4 sec → Exhale 4 sec → Hold 4 sec. Repeat 3x.",
    "grounding": "5-4-3-2-1 technique: Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste.",
    "journaling": "Write down: 1 thing you’re grateful for, 1 emotion you feel, 1 small win today."
}

def detect_crisis(text):
    text_lower = text.lower()
    for keyword in CRISIS_KEYWORDS:
        if keyword in text_lower:
            return True
    return False

def get_emotion(text):
    try:
        result = emotion_classifier(text)[0]
        label = result['label'].lower()
        score = result['score']
        emotion_map = {
            'anger': 'anger',
            'disgust': 'anger',
            'fear': 'fear',
            'joy': 'joy',
            'sadness': 'sadness',
            'surprise': 'surprise'
        }
        return emotion_map.get(label, 'neutral'), score
    except:
        return 'neutral', 0.0

def generate_response(user_input, emotion):
    if detect_crisis(user_input):
        return {
            "text": (
                "I'm really concerned about you right now. \n\n"
                "Please reach out to someone who can help:\n"
                "• National Suicide & Crisis Lifeline: Call/text **988**\n"
                "• Crisis Text Line: Text **HOME** to **741741**\n"
                "• Your campus counseling center: [Link to local resources]\n\n"
                "You matter. Please don’t go through this alone."
            ),
            "type": "crisis"
        }

    responses = RESPONSE_TEMPLATES.get(emotion, RESPONSE_TEMPLATES['neutral'])
    base_response = random.choice(responses)

    if emotion in ['fear', 'sadness', 'anger'] and random.random() < 0.4:
        tip_key = random.choice(list(COPING_TIPS.keys()))
        tip = COPING_TIPS[tip_key]
        base_response += f"\n\n🌱 *Here’s a small tool:* {tip}"

    return {"text": base_response, "type": "support"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    user_message = re.sub(r'\b\d{10}\b', '[PHONE]', user_message)
    user_message = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        '[EMAIL]',
        user_message
    )

    emotion, confidence = get_emotion(user_message)
    bot_response = generate_response(user_message, emotion)

    return jsonify({
        "user_message": user_message,
        "bot_response": bot_response["text"],
        "emotion": emotion,
        "confidence": round(confidence, 2),
        "response_type": bot_response["type"]
    })

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True, host='0.0.0.0', port=5000)
