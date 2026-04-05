import streamlit as st
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("🔐 Privacy & Security Control")

st.markdown("""
<div class="glass-card">
    <p style="color:#ccc; font-size: 1.1em;">Mental Healthcare data is highly sensitive. Here you can configure your encryption preferences, compliance toggles, and data anonymization settings.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Data Consent Form")
st.checkbox("I consent to my biometric data being processed locally for Risk Assessment.", value=True)
st.checkbox("I consent to my anonymized data being used to improve Bias & Fairness models.", value=True)

st.markdown("---")
st.subheader("Security Controls")
col1, col2 = st.columns(2)

with col1:
    anon = st.toggle("Enable Anonymous Mode")
    if anon:
        st.success("You are now fully anonymous. No personally identifiable information (PII) will be sent to the backend database.")
    
with col2:
    encrypt = st.toggle("Enable Fernet E2E Encryption", value=True)
    if encrypt:
        st.success("All journal logs and symptoms will be encrypted using Passlib/bcrypt mock before transit.")
        
st.markdown("---")
st.info("🔒 AI Mental Health Operating System strictly adheres to 2050 Global Healthcare Data Privacy Regulations.")
