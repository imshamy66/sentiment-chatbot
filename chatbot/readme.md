# Overview
A smart chatbot application that combines emotion analysis, natural language processing, and wellness recommendations to provide supportive conversations and mental guidance.

# 1. Emotion Analysis
- Implemented emotion detection using the `emotion-english-distilroberta-base` model
- Identifies 7 primary emotions: anger, disgust, fear, joy, neutral, sadness, and surprise
- Provides confidence scores for emotion predictions

# 2. Conversation Management
- Session-based conversation tracking
- Maintains context of recent exchanges
- Stores:
  - User messages
  - Bot responses
  - Detected emotions

# 3. Wellness Support System
- Provides contextual wellness suggestions based on:
  - Detected emotions
  - Extracted keywords
  - Conversation context

## Technologies Used

### Backend
- **Flask**: Web framework for the application
- **Python**: Primary programming language
- **Fetch API**: Asynchronous communication with backend

## Installation and Setup

#. Create Virtual Environment
python -m venv venv
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Running the Application

1. Start the Flask Server:
python app.py

2. Access the Application:
- Open your web browser
- Navigate to `http://localhost:5000`
- Start chatting!

Features
Core Functionality
- Real-time emotion analysis
- Contextual conversation handling

User Interface
- Clean, responsive design
- History sidebar
