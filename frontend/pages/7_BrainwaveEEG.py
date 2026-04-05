import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("🧠 Live Brainwave EEG Monitor")

st.markdown("""
<div class="glass-card">
    <p style="color:#ccc; font-size: 1.1em;">Using simulated <strong>EEG (Electroencephalogram)</strong> data, this module classifies your real-time brainwave activity into mental states. By 2050, wearable EEG headbands will be as common as smartwatches.</p>
</div>
""", unsafe_allow_html=True)

# Mental state detection
states = {
    "🟢 Deep Focus": {"alpha": 0.3, "beta": 0.8, "theta": 0.2, "delta": 0.1},
    "🔴 Anxious / Stressed": {"alpha": 0.2, "beta": 0.95, "theta": 0.4, "delta": 0.15},
    "🟡 Meditative / Calm": {"alpha": 0.85, "beta": 0.2, "theta": 0.6, "delta": 0.3},
    "🔵 Drowsy / Fatigued": {"alpha": 0.5, "beta": 0.15, "theta": 0.7, "delta": 0.8},
    "🟠 Creative Flow": {"alpha": 0.7, "beta": 0.55, "theta": 0.5, "delta": 0.2},
}

state_name = st.selectbox("Simulate Mental State (will be auto-detected via headband in 2050):", list(states.keys()))
chosen = states[state_name]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Alpha Waves (8-12 Hz)", f"{chosen['alpha']*100:.0f}%", help="Relaxation & creativity")
col2.metric("Beta Waves (12-30 Hz)", f"{chosen['beta']*100:.0f}%", help="Active thinking & focus")
col3.metric("Theta Waves (4-8 Hz)", f"{chosen['theta']*100:.0f}%", help="Dreaming & meditation")
col4.metric("Delta Waves (0.5-4 Hz)", f"{chosen['delta']*100:.0f}%", help="Deep sleep")

st.markdown("---")

# Generate live-looking EEG signal
t = np.linspace(0, 4 * np.pi, 300)
alpha_amp = chosen['alpha']
beta_amp = chosen['beta']
theta_amp = chosen['theta']

signal = (alpha_amp * np.sin(10 * t) +
          beta_amp * np.sin(20 * t + 0.5) +
          theta_amp * np.sin(6 * t + 1.2) +
          0.1 * np.random.randn(300))

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=np.linspace(0, 4, 300), y=signal,
    mode='lines', name='EEG Signal',
    line=dict(color='#00f2fe', width=2)
))
fig.add_trace(go.Scatter(
    x=np.linspace(0, 4, 300),
    y=alpha_amp * np.sin(10 * t),
    mode='lines', name='Alpha Component',
    line=dict(color='#a78bfa', width=1, dash='dot')
))
fig.update_layout(
    title=f"Live EEG Signal — Detected State: {state_name}",
    xaxis_title="Time (seconds)",
    yaxis_title="Amplitude (μV)",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0.1)",
    font={'color': "white"},
    legend=dict(bgcolor="rgba(0,0,0,0.3)")
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Insight panel
insight_map = {
    "🟢 Deep Focus": ("Low risk. You are in a productive state. Optimal time for problem-solving.", "success"),
    "🔴 Anxious / Stressed": ("High Beta activity detected. Your brain is overloaded. Take a 5-min break and try breathing exercises.", "error"),
    "🟡 Meditative / Calm": ("Excellent Alpha activity. Your nervous system is balanced. Great state for therapy sessions.", "success"),
    "🔵 Drowsy / Fatigued": ("High Delta/Theta while awake = sleep pressure. Mental processing is impaired. Prioritize rest tonight.", "warning"),
    "🟠 Creative Flow": ("Balanced Alpha-Beta profile. Ideal state for creative healing, journaling, or artistic expression.", "info"),
}
msg, kind = insight_map[state_name]
getattr(st, kind)(f"🧠 AI EEG Insight: {msg}")
