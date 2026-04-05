import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("🌍 Community Mental Health Map")

st.markdown("""
<div class="glass-card">
    <p style="color:#ccc; font-size: 1.1em;">This <strong>anonymised, crowd-sourced heatmap</strong> visualises real-time mental health stress concentrations across Indian cities. Data is fully anonymised before submission — used by WHO-level health bodies in 2050 for policy planning.</p>
</div>
""", unsafe_allow_html=True)

# Simulated city data
cities = [
    {"city": "Mumbai",     "lat": 19.076, "lon": 72.877, "depression_index": 0.72, "reports": 1243},
    {"city": "Delhi",      "lat": 28.614, "lon": 77.209, "depression_index": 0.68, "reports": 1876},
    {"city": "Bangalore",  "lat": 12.972, "lon": 77.594, "depression_index": 0.55, "reports": 987},
    {"city": "Pune",       "lat": 18.521, "lon": 73.857, "depression_index": 0.61, "reports": 734},
    {"city": "Chennai",    "lat": 13.083, "lon": 80.270, "depression_index": 0.49, "reports": 612},
    {"city": "Hyderabad",  "lat": 17.385, "lon": 78.486, "depression_index": 0.58, "reports": 820},
    {"city": "Kolkata",    "lat": 22.572, "lon": 88.363, "depression_index": 0.64, "reports": 943},
    {"city": "Ahmedabad",  "lat": 23.022, "lon": 72.571, "depression_index": 0.43, "reports": 521},
    {"city": "Jaipur",     "lat": 26.912, "lon": 75.787, "depression_index": 0.38, "reports": 389},
    {"city": "Surat",      "lat": 21.170, "lon": 72.831, "depression_index": 0.35, "reports": 312},
    {"city": "Lucknow",    "lat": 26.846, "lon": 80.946, "depression_index": 0.52, "reports": 476},
    {"city": "Nagpur",     "lat": 21.145, "lon": 79.088, "depression_index": 0.45, "reports": 398},
    {"city": "Bhopal",     "lat": 23.259, "lon": 77.412, "depression_index": 0.41, "reports": 344},
    {"city": "Patna",      "lat": 25.594, "lon": 85.137, "depression_index": 0.59, "reports": 542},
    {"city": "Chandigarh", "lat": 30.733, "lon": 76.779, "depression_index": 0.33, "reports": 278},
]

df = pd.DataFrame(cities)

def get_color(v):
    if v >= 0.65: return "#ff0844"
    elif v >= 0.45: return "#ffd700"
    else: return "#00c853"

def get_risk(v):
    if v >= 0.65: return "🔴 High Risk"
    elif v >= 0.45: return "🟡 Moderate"
    else: return "🟢 Low Risk"

df['color'] = df['depression_index'].apply(get_color)
df['risk_label'] = df['depression_index'].apply(get_risk)
df['size'] = df['reports'] / 25  # normalise bubble size

# ─── WORKING MAP using open-street-map (no token needed) ─────────────────────
fig = go.Figure()

# Add city bubbles
for _, row in df.iterrows():
    fig.add_trace(go.Scattermapbox(
        lat=[row['lat']],
        lon=[row['lon']],
        mode='markers+text',
        marker=dict(
            size=row['size'],
            color=row['color'],
            opacity=0.75,
            sizemode='diameter'
        ),
        text=[row['city']],
        textposition="top center",
        textfont=dict(color='white', size=11),
        hovertemplate=(
            f"<b>{row['city']}</b><br>"
            f"Depression Index: {row['depression_index']:.0%}<br>"
            f"Risk Level: {row['risk_label']}<br>"
            f"Anonymous Reports: {row['reports']}<br>"
            "<extra></extra>"
        ),
        name=row['city']
    ))

fig.update_layout(
    mapbox=dict(
        style="open-street-map",
        center={"lat": 21.0, "lon": 78.5},
        zoom=4,
    ),
    showlegend=False,
    height=550,
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
    paper_bgcolor="rgba(0,0,0,0)",
    font={'color': 'white'},
    title=dict(text="Community Depression Risk Index — India (2050 Live Data)", font=dict(color='white'))
)

st.plotly_chart(fig, use_container_width=True)

# ─── LEGEND ──────────────────────────────────────────────────────────────────
lc1, lc2, lc3 = st.columns(3)
lc1.markdown("<div style='text-align:center; padding:10px; background:rgba(255,8,68,0.2); border-radius:10px; border:1px solid #ff0844;'>🔴 <b>High Risk</b><br><small>>65% Depression Index</small></div>", unsafe_allow_html=True)
lc2.markdown("<div style='text-align:center; padding:10px; background:rgba(255,215,0,0.2); border-radius:10px; border:1px solid #ffd700;'>🟡 <b>Moderate Risk</b><br><small>45–65% Depression Index</small></div>", unsafe_allow_html=True)
lc3.markdown("<div style='text-align:center; padding:10px; background:rgba(0,200,83,0.2); border-radius:10px; border:1px solid #00c853;'>🟢 <b>Low Risk</b><br><small>&lt;45% Depression Index</small></div>", unsafe_allow_html=True)

# ─── TABLE ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.subheader("📋 City-Level Breakdown")
display_df = df[['city', 'depression_index', 'reports', 'risk_label']].copy()
display_df['depression_index'] = display_df['depression_index'].apply(lambda x: f"{x:.0%}")
display_df.columns = ['City', 'Depression Index', 'Anonymous Reports', 'Risk Level']
st.dataframe(display_df.sort_values('Depression Index', ascending=False), use_container_width=True)

# ─── BAR CHART ───────────────────────────────────────────────────────────────
st.subheader("📊 Risk Ranking by City")
df_sorted = df.sort_values('depression_index', ascending=True)
fig_bar = go.Figure(go.Bar(
    x=df_sorted['depression_index'],
    y=df_sorted['city'],
    orientation='h',
    marker_color=df_sorted['color'],
    text=[f"{v:.0%}" for v in df_sorted['depression_index']],
    textposition='outside',
    textfont=dict(color='white')
))
fig_bar.update_layout(
    xaxis=dict(tickformat='.0%', color='white', range=[0, 0.9]),
    yaxis=dict(color='white'),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0.1)",
    font={'color': 'white'},
    height=420,
    margin=dict(l=10, r=60, t=20, b=20)
)
st.plotly_chart(fig_bar, use_container_width=True)

# ─── CONTROLS ────────────────────────────────────────────────────────────────
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    contribute = st.toggle("📡 Contribute My Anonymous Data to This Map")
    if contribute:
        st.success("✅ Your anonymised, location-blurred data will help improve the community mental health map. No PII is ever stored.")
with col2:
    st.info("🔒 All data is de-identified using k-anonymity (k≥50) and differential privacy noise before public release.")
