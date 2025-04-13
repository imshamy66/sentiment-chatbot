# Wellness-Focused AI Chatbot

## Overview
A smart chatbot application that combines emotion analysis, natural language processing, and wellness recommendations to provide supportive conversations and mental wellness guidance.

## Approach Taken

### 1. Emotion Analysis
- Implemented emotion detection using the `emotion-english-distilroberta-base` model
- Identifies 7 primary emotions: anger, disgust, fear, joy, neutral, sadness, and surprise
- Provides confidence scores for emotion predictions
- Uses emotion data to tailor responses and suggestions

### 2. Advanced Language Model Integration
Integrated Ollama to access Llama 3.2, a cutting-edge large language model for contextual and high-quality text generation.
Enhances the chatbot's conversational abilities and provides more nuanced responses.
Complements other NLP and emotion analysis pipelines.

### 3. Conversation Management
- Session-based conversation tracking
- Maintains context of recent exchanges
- Stores:
  - User messages
  - Bot responses
  - Detected emotions
  - Timestamps
  - Wellness suggestions

### 4. Wellness Support System
- Provides contextual wellness suggestions based on:
  - Detected emotions
  - Extracted keywords
  - Conversation context
- Tracks suggestion history
- Offers personalized mental health tips
- Maintains a history of provided suggestions

## Technologies Used

### Backend
- **Flask**: Web framework for the application
- **Transformers**: Hugging Face transformers for emotion classification
- **Ollama**: Integration of Llama 3.2 for conversational intelligence.
- **Python**: Primary programming language

### Frontend
- **HTML/CSS**: Structure and styling
- **JavaScript**: Client-side interactions
- **Fetch API**: Asynchronous communication with backend

### Key Libraries
```plaintext
flask==2.2.2
Requests==2.32.3
Transformers==4.48.1
```

## Installation and Setup

### 1. Unzip the Files and Move to Directory
- Extract the provided .zip file to a location on your system.
```bash
cd wellness-chatbot
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Install Ollama
Follow the official Ollama documentation "https://ollama.com/download" to install and configure Ollama on your system.


## Running the Application

1. Start the Flask Server:
```bash
python app.py
```

2. Access the Application:
- Open your web browser
- Navigate to `http://localhost:5000`
- Start chatting!

## Features

### Core Functionality
- Real-time emotion analysis
- Natural language understanding
- Contextual conversation handling
- Wellness suggestion system
- Conversation history tracking

### User Interface
- Clean, responsive design
- Real-time message updates
- Wellness suggestion display
- History sidebar
