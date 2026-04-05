import streamlit as st
import sys, os
import time
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("🤖 AI Therapist (Powered by Gemini AI)")

st.markdown("""
<div class="glass-card">
    <p style="color:#ccc">This is your real AI Therapist powered by <strong>Google Gemini</strong>. It understands full context, emotional tone, and provides clinically-aligned Cognitive Behavioral Therapy (CBT) responses in real-time.</p>
</div>
""", unsafe_allow_html=True)

# ─── API KEY SETUP ────────────────────────────────────────────────────────────
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))

if not GEMINI_API_KEY:
    st.warning("⚠️ **Gemini API key not set.** To enable real AI responses, create a file `.streamlit/secrets.toml` with:\n```\nGEMINI_API_KEY = 'your-key-here'\n```\nGet a FREE key at: https://aistudio.google.com/app/apikey\n\n*Running in smart fallback mode for now.*")

# ─── SYSTEM PROMPT ───────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are an empathetic, professional AI Mental Health Therapist built into the AI Mental Health Operating System (2050 vision). 
Your role:
- Provide evidence-based Cognitive Behavioral Therapy (CBT) responses
- Detect emotional tone in the user's message
- Be warm, supportive, non-judgmental, and calm
- Suggest specific coping strategies (breathing, grounding, journaling, etc.)
- If user expresses crisis/suicidal thoughts, immediately recommend professional help and crisis lines
- Keep responses concise (3-5 sentences max) but empathetic
- Never diagnose. Always remind user you supplement, not replace, professional care.
"""

# ─── GEMINI API CALL ─────────────────────────────────────────────────────────
def call_gemini(messages: list) -> str:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
        # Build history for context
        history = []
        for msg in messages[:-1]:  # all except last user msg
            role = "user" if msg["role"] == "user" else "model"
            history.append({"role": role, "parts": [msg["content"]]})
        
        chat = model.start_chat(history=history)
        response = chat.send_message(messages[-1]["content"])
        return response.text
    except Exception as e:
        return smart_fallback(messages[-1]["content"])

# ─── SMART FALLBACK ──────────────────────────────────────────────────────────
def smart_fallback(text: str) -> str:
    t = text.lower()
    if any(w in t for w in ["suicide", "kill myself", "end my life", "want to die"]):
        return "🚨 I'm deeply concerned about what you've shared. Please reach out immediately to a crisis helpline — **iCall India: 9152987821** or **Vandrevala Foundation: 1860-2662-345** (24/7). You matter, and help is available right now."
    elif any(w in t for w in ["sad", "empty", "hopeless", "depressed", "worthless"]):
        return "I hear you, and I want you to know that feeling this way is valid. Emptiness can feel overwhelming, but it does lift. Let's try a grounding technique right now — look around and name **5 things you can see**. I'm right here with you."
    elif any(w in t for w in ["anxious", "anxiety", "panic", "nervous", "scared", "fear"]):
        return "Anxiety can feel all-consuming, but your body is safe. Let's do **box breathing**: Breathe in for 4 counts, hold 4, exhale 4, hold 4. Repeat 3 times. This activates your parasympathetic nervous system and calms the panic response."
    elif any(w in t for w in ["stress", "overwhelmed", "too much", "can't cope"]):
        return "When everything piles up, your brain goes into survival mode. The most powerful thing you can do right now? Write down **one small task** you can complete in the next 10 minutes. Small wins rebuild a sense of control."
    elif any(w in t for w in ["sleep", "tired", "exhausted", "insomnia", "can't sleep"]):
        return "Poor sleep and mental health are deeply interlinked. I recommend the **4-7-8 sleep technique**: Inhale 4 sec, hold 7 sec, exhale 8 sec. Also, try removing all screens 30 mins before bed — blue light disrupts melatonin production significantly."
    elif any(w in t for w in ["happy", "good", "great", "better", "excited"]):
        return "That's wonderful to hear! 🌟 Positive emotions are powerful medicine. Take a moment to **acknowledge this feeling** — what specifically made today a good day? Recording this in a journal helps your brain create a 'positive memory bank' to draw on in harder times."
    elif any(w in t for w in ["lonely", "alone", "isolated", "no one"]):
        return "Loneliness is one of the most painful human experiences — you are not alone in feeling alone. Even small social interactions help. Could you send a text to someone you care about today? Research shows even a 2-minute connection can lift mood significantly."
    else:
        responses = [
            "Thank you for sharing that with me. Could you tell me a bit more about what's been on your mind lately? I want to make sure I understand what you're going through.",
            "I appreciate you opening up. Sometimes just putting feelings into words is the first step to understanding them. What do you think triggered this feeling?",
            "That makes a lot of sense. Our feelings are valid signals. What's one thing that usually helps you feel even slightly better when you're in this headspace?",
        ]
        return random.choice(responses)

# ─── CHAT UI ─────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi there 👋 I'm your AI Mental Health Therapist. This is a safe space — no judgment, only support. How are you feeling today?"}]

# Render all past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new input
if prompt := st.chat_input("Talk to me... (e.g. 'I've been feeling really anxious lately')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if GEMINI_API_KEY:
                bot_reply = call_gemini(st.session_state.messages)
            else:
                time.sleep(0.8)
                bot_reply = smart_fallback(prompt)
            st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Clear chat button
if len(st.session_state.messages) > 1:
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = [{"role": "assistant", "content": "Fresh start! 🌱 I'm here whenever you need to talk. How are you feeling right now?"}]
        st.rerun()
