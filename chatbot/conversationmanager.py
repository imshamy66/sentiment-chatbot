from flask import session
from datetime import datetime

class ConversationManager:
    def __init__(self):
        self.max_context_length = 5

    def initialize_context(self, session_id):
        if 'context' not in session:
            session['context'] = []
        if 'wellness_history' not in session:
            session['wellness_history'] = []

    def add_to_context(self, user_message, bot_response, emotion):
        context = session.get('context', [])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        context.append({
            'timestamp': timestamp,
            'user_message': user_message,
            'bot_response': bot_response,
            'emotion': emotion
        })

        if len(context) > self.max_context_length:
            context = context[-self.max_context_length:]
        
        session['context'] = context

    def get_context(self):
        return session.get('context', [])
