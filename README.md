# AICTE_AI-ML_internship_Mental-Health-Companion-Chatbot-

MindBuddy – Mental Health Companion Chatbot

MindBuddy is an AI-powered mental health companion chatbot designed to support students dealing with stress, anxiety, loneliness, and emotional challenges. It uses sentiment and emotion analysis to understand user mood and responds with empathetic, motivational messages along with simple coping and relaxation techniques.

⚠️ Disclaimer: MindBuddy is not a replacement for professional mental health care. It is intended as a supportive tool only.

✨ Features

💬 Emotion Detection

Uses a pre-trained transformer model to detect emotions such as sadness, fear, anger, joy, and neutral states.

🤝 Empathetic Responses

Generates emotionally appropriate, supportive, and motivational replies.

🌱 Coping & Relaxation Tips

Provides breathing exercises, grounding techniques, and journaling prompts.

🚨 Crisis Detection

Identifies high-risk keywords and displays emergency support resources.

🔐 Privacy-Aware

Automatically masks emails and phone numbers from user input.

🌐 Web-Based Interface

Clean, responsive UI built with HTML, CSS, and JavaScript.

⚡ Real-Time Interaction

Fast chatbot responses using Flask backend.

🛠️ Tech Stack

Frontend

HTML5

CSS3

JavaScript

Backend

Python (Flask)

AI / NLP

Hugging Face Transformers

DistilRoBERTa Emotion Classification Model

PyTorch

📁 Project Structure
Mental-Health-Companion-Chatbot/
│
├── app.py               # Flask backend and AI logic
├── requirements.txt     # Python dependencies
│
├── templates/
│   └── index.html       # Chatbot UI
│
├── static/
│   └── style.css        # Styling for UI
│
└── README.md            # Project documentation

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/Mental-Health-Companion-Chatbot.git
cd Mental-Health-Companion-Chatbot

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser
http://localhost:5000

🧪 How It Works

User enters a message describing their feelings.

The chatbot analyzes the text using an emotion classification model.

An empathetic response is generated based on detected emotion.

If emotional distress is detected, coping tips are suggested.

If crisis-related language is found, emergency resources are shown.

🚨 Crisis Support Notice

If a user expresses thoughts related to self-harm or suicide, MindBuddy immediately displays crisis resources such as:

National Suicide & Crisis Lifeline (USA): Call/Text 988

Crisis Text Line: Text HOME to 741741

Local campus counseling services

🔮 Future Enhancements

User authentication and chat history

Multilingual support

Voice-based interaction

Personalized mental health tracking

Integration with campus counseling systems

🤝 Contributing

Contributions are welcome!

Fork this repository

Create a new branch (feature/your-feature-name)

Commit your changes

Open a Pull Request

📜 License

This project is licensed under the MIT License.

🙌 Acknowledgements

Hugging Face Transformers

PyTorch

Open-source mental health AI research community
