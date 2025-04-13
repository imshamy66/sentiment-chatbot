# app.py
from flask import Flask, request, jsonify, render_template, session
from transformers import pipeline
from conversationmanager import ConversationManager
from generator import OllamaGenerator

app = Flask(__name__)
app.secret_key = 'your-secret-key'

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

conversation_manager = ConversationManager()
ollama_generator = OllamaGenerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    conversation_manager.initialize_context(session.get('id'))
    
    try:
        emotion_result = classifier(user_message)[0]
        emotion = emotion_result['label'].lower()
        confidence = emotion_result['score']
        
        context = conversation_manager.get_context()
        
        main_response = ollama_generator.generate_response(user_message, context)
        
        wellness_suggestion = ollama_generator.generate_wellness_suggestion(emotion, user_message)
        
        full_response = f"{main_response} {wellness_suggestion}"
        
        conversation_manager.add_to_context(
            user_message,
            full_response,
            emotion
        )
        
        return jsonify({
            'response': main_response,
            'emotion': emotion,
            'confidence': f"{confidence:.2%}",
            'wellness_suggestion': wellness_suggestion
        })
        
    except Exception as e:
        print(f"Error processing message: {str(e)}")
        return jsonify({
            'response': "I'm having trouble processing that right now. Could you try rephrasing?",
            'emotion': 'unknown',
            'confidence': '0%'
        })

if __name__ == '__main__':
    app.run(debug=True)