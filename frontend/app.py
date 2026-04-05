import streamlit as st
import sys, os

# Add parent path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils_ui import set_premium_ui

set_premium_ui()

st.markdown("<h1 style='text-align: center; color: #4facfe; font-size: 4rem; font-weight: 800;'>AI Mental Health Operating System</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #a1a1aa; margin-bottom: 40px;'>Intelligent Mental Health Prediction & Monitoring System</h3>", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card" style="text-align: center;">
    <h2 style="color: white; margin-bottom: 20px;">Welcome to the Future of Healthcare (2050 Vision) 🚀</h2>
    <p style="font-size: 1.1rem; color: #cccccc; line-height: 1.6;">
        AI Mental Health Operating System is a state-of-the-art, multi-modal AI system designed to predict, track, and improve mental wellbeing.
        By analyzing advanced biometric data and utilizing cutting-edge deep learning, it serves as your personal 
        Digital Twin and always-available AI Therapist.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="glass-card" style="text-align: center; height: 180px;">
        <h1 style="font-size: 3rem; margin: 0;">📊</h1>
        <h4 style="margin-top: 10px; color: #00f2fe;">Real-time Tracking</h4>
        <p style="font-size: 0.9rem; color: #aaa;">Continuous monitoring & Early Warning System.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="text-align: center; height: 180px;">
        <h1 style="font-size: 3rem; margin: 0;">🤖</h1>
        <h4 style="margin-top: 10px; color: #4facfe;">AI Therapist</h4>
        <p style="font-size: 0.9rem; color: #aaa;">NLP-driven conversations and CBT strategies.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-card" style="text-align: center; height: 180px;">
        <h1 style="font-size: 3rem; margin: 0;">🧬</h1>
        <h4 style="margin-top: 10px; color: #764ba2;">Digital Twin</h4>
        <p style="font-size: 0.9rem; color: #aaa;">Wearable integration & Time-Series prediction.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: #333;'>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>👈 Please navigate using the sidebar to explore the advanced modules.</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-size: 0.9rem; margin-top: 40px;'>👨‍💻 Admin: Kartik Pawase</p>", unsafe_allow_html=True)
