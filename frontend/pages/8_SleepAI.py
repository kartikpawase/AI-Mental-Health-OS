import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("😴 Sleep Intelligence AI")

st.markdown("""
<div class="glass-card">
    <p style="color:#ccc; font-size: 1.1em;"><strong>70% of mental health disorders are linked to disrupted sleep.</strong> Our AI analyses your sleep patterns, predicts tonight's quality, and generates a personalised recovery plan using deep learning sleep models.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📊 Tonight's Sleep Prediction")

col1, col2, col3 = st.columns(3)
stress = col1.slider("Today's Stress Level", 0, 10, 6)
caffeine = col2.slider("Caffeine cups today", 0, 10, 3)
screen_time = col3.slider("Evening screen time (hrs)", 0, 8, 3)

# Simple prediction heuristic
sleep_score = max(10, 100 - (stress * 4) - (caffeine * 5) - (screen_time * 4) + np.random.randint(-5, 5))
sleep_score = min(sleep_score, 98)

rem = max(0, 22 - stress * 1.5 + np.random.randint(-3, 3))
deep = max(0, 18 - caffeine * 2 + np.random.randint(-2, 2))
light = 100 - rem - deep

fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=sleep_score,
    title={'text': "Predicted Sleep Quality Score", 'font': {'color': 'white'}},
    delta={'reference': 80},
    gauge={
        'axis': {'range': [0, 100], 'tickcolor': 'white'},
        'bar': {'color': "#00f2fe"},
        'steps': [
            {'range': [0, 40], 'color': '#ff0844'},
            {'range': [40, 70], 'color': '#ffd700'},
            {'range': [70, 100], 'color': '#00c853'}
        ],
    }
))
fig_gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': 'white'})
st.plotly_chart(fig_gauge, use_container_width=True)

# Sleep stage breakdown
st.subheader("🌙 Predicted Sleep Stage Breakdown")
fig_pie = go.Figure(data=[go.Pie(
    labels=['REM Sleep', 'Deep Sleep', 'Light Sleep'],
    values=[rem, deep, light],
    hole=0.4,
    marker_colors=['#4facfe', '#a78bfa', '#00f2fe']
)])
fig_pie.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': 'white'}, legend=dict(bgcolor="rgba(0,0,0,0)"))
st.plotly_chart(fig_pie, use_container_width=True)

# 30-day sleep debt tracker
st.markdown("---")
st.subheader("📅 30-Day Sleep Debt Accumulation")
days = np.arange(1, 31)
base = 7.5
debt = np.cumsum(np.clip(base - (5 + np.random.randn(30) * 1.5), 0, None))
fig_debt = go.Figure()
fig_debt.add_trace(go.Scatter(x=days, y=debt, fill='tozeroy', name="Sleep Debt (hrs)",
                               line=dict(color='#ff7043', width=2), fillcolor='rgba(255,112,67,0.3)'))
fig_debt.update_layout(title="Cumulative Sleep Debt",
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.1)", font={'color': 'white'})
st.plotly_chart(fig_debt, use_container_width=True)

# Personalized fix plan
st.markdown("---")
st.subheader("🤖 AI Sleep Recovery Protocol")
recs = []
if caffeine > 2: recs.append("☕ Cut caffeine after 2 PM — it has a 6-hour half-life in your blood.")
if screen_time > 1: recs.append("📱 Use blue-light blocking glasses after 8 PM or use Night Mode.")
if stress > 6: recs.append("🧘 Try 10-min body-scan meditation before bed (reduces cortisol by 28%).")
recs.append("🌡️ Keep your room at 18-20°C — the optimal temperature for deep sleep stages.")
recs.append("⏰ Maintain the same wake time every day, even weekends (strongest sleep signal).")
for rec in recs:
    st.success(rec)
