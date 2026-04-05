import streamlit as st

def set_premium_ui():
    st.set_page_config(page_title="AI Mental Health Operating System", page_icon="🧬", layout="wide", initial_sidebar_state="expanded")
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        
        .stApp {
            background-color: #0b0f19;
            background-image: radial-gradient(circle at 10% 20%, rgba(31, 38, 59, 1) 0%, rgba(11, 15, 25, 1) 90%);
            color: #ffffff;
        }
        
        /* Modern Gradient Buttons */
        .stButton>button {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
            color: white !important;
            border-radius: 8px;
            border: none;
            font-weight: 600;
            padding: 0.6rem 1.2rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 242, 254, 0.2);
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 242, 254, 0.4);
            border: none;
        }
        
        /* Glassmorphism Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 24px;
            margin: 16px 0;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        }
        
        /* Cool Metrics */
        div[data-testid="stMetricValue"] {
            font-size: 3rem !important;
            font-weight: 800 !important;
            background: -webkit-linear-gradient(#00f2fe, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
    """, unsafe_allow_html=True)
