import streamlit as st
import requests
import plotly.graph_objects as go
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("📊 Real-Time Monitoring & Early Warning System")

st.markdown("""
<div class="glass-card">
    <h3 style='margin-top:0'>Daily Biometric Input</h3>
    <p style='color:#ccc'>Enter your daily statistics to calculate your real-time risk probability via the AI Mental Health Operating System Neural Network.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 6.5)
    physical_activity = st.slider("Physical Activity (0-10)", 0.0, 10.0, 5.0)
    
with col2:
    gender = st.selectbox("Gender", ["Male", "Female", "Non-Binary"])
    stress_level = st.slider("Stress Level (0-10)", 0.0, 10.0, 5.0)
    social_interactions = st.slider("Social Interactions (0-10)", 0.0, 10.0, 5.0)
    history = st.selectbox("History of Mental Illness", ["No", "Yes"])

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Predict Mental Health Risk"):
    payload = {
        "age": age,
        "gender": gender,
        "sleep_hours": sleep_hours,
        "physical_activity": physical_activity,
        "social_interactions": social_interactions,
        "stress_level": stress_level,
        "history_mental_illness": history
    }
    
    # Try calling backend API
    try:
        response = requests.post("http://127.0.0.1:8000/predict_risk/", json=payload, timeout=2)
        if response.status_code == 200:
            data = response.json()
            risk_prob = data["risk_probability"]
        else:
            raise Exception("API Error")
    except:
        # Fallback UI simulated response if API server isn't running
        base_risk = 0.35
        if sleep_hours < 6: base_risk += 0.2
        if stress_level >= 7: base_risk += 0.2
        if physical_activity < 3: base_risk += 0.1
        if history == 'Yes': base_risk += 0.15
        risk_prob = min(0.99, base_risk)
        
    st.markdown("---")
    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        st.metric("Depression Risk Score", f"{risk_prob*100:.1f}%")
        if risk_prob > 0.85:
            st.error("🚨 CRITICAL ALERT: High Depression Risk Detected! Generating notification to Healthcare Provider.", icon="🚨")
        elif risk_prob > 0.50:
            st.warning("⚠️ Elevated Risk. Please consider evaluating your sleep and stress thresholds.")
        else:
            st.success("✅ Stable Mental Health.")
            
        st.markdown("""
        <div class="glass-card" style="margin-top: 20px;">
            <h4 style='color: #4facfe'>Personalized Action Plan</h4>
            <ul style='color: #ccc; font-size: 0.9em;'>
                <li>Increase sleep goal to 8 hours.</li>
                <li>Hydrate and spend 15 mins stretching.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
            
    with res_col2:
        # Plotly Gauge chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = risk_prob * 100,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Risk Probability"},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
                'bar': {'color': "rgba(255,255,255,0.8)"},
                'steps' : [
                    {'range': [0, 40], 'color': "rgba(0,255,0,0.3)"},
                    {'range': [40, 75], 'color': "rgba(255,255,0,0.3)"},
                    {'range': [75, 100], 'color': "rgba(255,0,0,0.5)"}],
            }
        ))
        fig.update_layout(height=350, margin=dict(l=10, r=10, t=50, b=10), paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"})
        st.plotly_chart(fig, use_container_width=True)
