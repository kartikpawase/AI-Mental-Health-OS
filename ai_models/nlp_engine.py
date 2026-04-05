def analyze_journal_sentiment(text):
    """
    Heuristic-based NLP simulator. 
    In the final system, you would plug in HuggingFace Pipeline("sentiment-analysis").
    """
    text_lower = text.lower()
    negative_keywords = ['sad', 'depressed', 'empty', 'hopeless', 'tired', 'anxious', 'alone', 'crying', 'stress']
    positive_keywords = ['happy', 'good', 'great', 'excited', 'better', 'improving', 'sleep', 'energy']
    
    neg_count = sum(1 for word in negative_keywords if word in text_lower)
    pos_count = sum(1 for word in positive_keywords if word in text_lower)
    
    if neg_count > pos_count:
        sentiment = "Negative / Distressed"
        risk_modifier = 0.15 # increases predicted risk
    elif pos_count > neg_count:
        sentiment = "Positive / Stable"
        risk_modifier = -0.10 # decreases predicted risk
    else:
        sentiment = "Neutral"
        risk_modifier = 0.0
        
    return {
        "sentiment": sentiment,
        "risk_modifier": risk_modifier,
        "analysis": f"Detected {neg_count} distress markers."
    }

def get_therapist_response(user_text):
    """
    Simulated LLM CBT Therapist Agent.
    """
    sub_text = user_text.lower()
    if 'sleep' in sub_text or 'tired' in sub_text:
         return "It sounds like you're struggling with rest. Have you considered setting a strict wind-down routine 30 minutes before bed without screens?"
    elif 'sad' in sub_text or 'empty' in sub_text or 'depressed' in sub_text:
         return "I hear your pain. It takes courage to admit feeling empty. I suggest we try a grounding technique: Name 5 things you can see around you."
    elif 'stress' in sub_text or 'anxious' in sub_text:
         return "Stress can be deeply overwhelming. Let's take a deep breath together. Inhale to the count of 4, hold for 4, and exhale for 6. How does that feel?"
    
    responses = [
        "It sounds like you're going through a lot. Can you tell me a bit more about what's occupying your mind?",
        "Thank you for sharing that. Acknowledging your feelings is a massive step forward.",
        "That makes complete sense. When we feel overwhelmed, it helps to focus on one small, controllable thing right now."
    ]
    import random
    return random.choice(responses)
