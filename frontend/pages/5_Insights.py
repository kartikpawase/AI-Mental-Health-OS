import streamlit as st
import plotly.express as px
import pandas as pd
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("🧠 Advanced XAI & Fairness Insights")

st.markdown("""
<div class="glass-card">
    <p style="color:#ccc; font-size: 1.1em;">Explore the model's inner workings via <strong>Explainable AI (SHAP)</strong> and verify that our algorithms adhere to strict ethical and demographic fairness standards.</p>
</div>
""", unsafe_allow_html=True)

st.header("1. Explainable AI (Why you got this score)")
st.info("SHAP values indicate how each feature pushed your risk score higher (red) or lower (blue). Never trust a black box in healthcare.")

# Mock SHAP Data
df_shap = pd.DataFrame({
    'Feature': ['Lack of Sleep', 'High Stress', 'Age Factor', 'Physical Activity', 'Social Interactions'],
    'Impact': [0.18, 0.22, 0.05, -0.12, -0.09]
})
df_shap = df_shap.sort_values(by='Impact')

fig_shap = px.bar(df_shap, x='Impact', y='Feature', orientation='h', color='Impact', 
                  color_continuous_scale='RdBu_r', title="SHAP Feature Importance (Waterfall Mock)")
fig_shap.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.1)", font={'color': "white"})
st.plotly_chart(fig_shap, use_container_width=True)

st.markdown("---")

st.header("2. Bias & Fairness Mitigation Center")
st.warning("Ensuring AI works equally and accurately for everyone, regardless of gender or age demographics.")

df_fairness = pd.DataFrame({
    'Demographic Group': ['Male', 'Female', 'Non-Binary', 'Age 18-35', 'Age 35-50', 'Age 50+'],
    'Accuracy': [0.93, 0.94, 0.92, 0.95, 0.93, 0.91]
})
fig_fairness = px.line_polar(df_fairness, r='Accuracy', theta='Demographic Group', line_close=True, 
                             title="Model Accuracy Radar Map")
fig_fairness.update_traces(fill='toself', fillcolor="rgba(0, 242, 254, 0.3)", line_color="#00f2fe")
fig_fairness.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font={'color': "white"})
st.plotly_chart(fig_fairness, use_container_width=True)
