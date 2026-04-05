import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_ui import set_premium_ui

set_premium_ui()

st.title("🧬 Genomic Mental Health Risk Mapper")

st.markdown("""
<div class="glass-card">
    <p style="color:#ccc; font-size: 1.1em;">By 2050, DNA sequencing costs will fall to <strong>under $10</strong>. This module simulates a quantum-genomic analysis of your inherited predispositions toward various mental health conditions — enabling true <em>preventive</em> psychiatry.</p>
</div>
""", unsafe_allow_html=True)

st.info("🔬 Simulating genomic scan of SNPs (Single Nucleotide Polymorphisms) linked to neuropsychiatric disorders...")

# Simulate genomic risk
np.random.seed(int(st.number_input("Enter your birth year (for personalised simulation):", 1970, 2010, 1995)))

conditions = ['Major Depression', 'Anxiety Disorder', 'Bipolar Disorder', 'ADHD', 'PTSD', 'OCD', 'Schizophrenia']
base_risk = np.random.uniform(0.05, 0.45, len(conditions))
genetic_risk = np.round(base_risk, 3)

df = pd.DataFrame({'Condition': conditions, 'Genetic Risk Score': genetic_risk})
df['Risk Level'] = pd.cut(df['Genetic Risk Score'], bins=[0, 0.15, 0.30, 1.0],
                          labels=['Low 🟢', 'Moderate 🟡', 'High 🔴'])

# Radar chart
fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
    r=genetic_risk.tolist() + [genetic_risk[0]],
    theta=conditions + [conditions[0]],
    fill='toself',
    fillcolor='rgba(167, 139, 250, 0.3)',
    line=dict(color='#a78bfa', width=2),
    name='Your Genetic Risk Profile'
))
fig_radar.add_trace(go.Scatterpolar(
    r=[0.15] * (len(conditions) + 1),
    theta=conditions + [conditions[0]],
    line=dict(color='#00c853', width=1, dash='dot'),
    name='Low Risk Baseline'
))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 0.5], color='white'),
               angularaxis=dict(color='white')),
    paper_bgcolor="rgba(0,0,0,0)",
    font={'color': 'white'},
    legend=dict(bgcolor='rgba(0,0,0,0.3)')
)
st.plotly_chart(fig_radar, use_container_width=True)

# Table
st.subheader("📋 Detailed Risk Breakdown")
st.dataframe(df.sort_values('Genetic Risk Score', ascending=False).reset_index(drop=True), use_container_width=True)

st.markdown("---")
highest = df.loc[df['Genetic Risk Score'].idxmax()]
st.warning(f"⚠️ **Highest genetic predisposition detected:** {highest['Condition']} (Score: {highest['Genetic Risk Score']:.2%}). This does NOT mean you will develop this condition — genetics are only ~40% of the story. Lifestyle, environment, and early intervention make the critical difference.")
st.success("🧬 **Protective Factor Tip**: Regular exercise (30 min/day) has been shown to reduce genetic depression risk expression by up to 35% by modifying epigenetic methylation patterns.")
