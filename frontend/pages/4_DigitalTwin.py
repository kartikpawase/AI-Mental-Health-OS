import streamlit as st
import plotly.graph_objects as go
import numpy as np
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("🧬 Digital Twin & Future Forecasting")

st.markdown("""
<div class="glass-card">
    <p style="color:#ccc; font-size: 1.1em;">Your <strong>Digital Twin</strong> integrates real-time wearable data (smartwatch, fitness bands) and uses time-series forecasting to predict your mental health trajectory <strong>2 weeks into the future</strong>.</p>
</div>
""", unsafe_allow_html=True)

# Generate fake historical and future data
np.random.seed(42)
days = np.arange(1, 31)
risk_history = 0.4 + 0.15 * np.sin(days/4) + np.random.normal(0, 0.05, 30)

future_days = np.arange(31, 46)
slope, intercept = np.polyfit(days[-10:], risk_history[-10:], 1)
future_risk = slope * future_days + intercept + np.random.normal(0, 0.03, 15)

fig = go.Figure()

# Plot History
fig.add_trace(go.Scatter(
    x=days, y=risk_history, 
    mode='lines+markers', name='Past 30 Days (Actual)',
    line=dict(color='#00f2fe', width=3)
))

# Plot Future Forecast
fig.add_trace(go.Scatter(
    x=future_days, y=future_risk,
    mode='lines+markers', name='15-Day Forecast (AI Predicted)',
    line=dict(color='#ff0844', width=3, dash='dash')
))

fig.update_layout(
    title="Comprehensive Depression Risk Trajectory",
    xaxis_title="Timeline (Days)",
    yaxis_title="Risk Probability Score",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0.1)",
    font={'color': "white"}
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")

st.markdown("### ⌚ Live Wearable Data Stream (Simulated)")
w1, w2, w3 = st.columns(3)
with w1:
    st.metric("Resting Heart Rate", f"{np.random.randint(60, 85)} BPM", delta=f"{np.random.randint(-5, 5)}")
with w2:
    st.metric("Sleep Deep Cycle", f"{np.random.randint(40, 90)} mins", delta="-15 mins")
with w3:
    st.metric("Activity Rings", f"{np.random.randint(60, 99)}%", delta="Trending Up")
