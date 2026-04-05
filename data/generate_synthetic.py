import pandas as pd
import numpy as np
import os

def generate_synthetic_data(num_samples=5000):
    np.random.seed(42)
    
    # Generate features
    age = np.random.randint(18, 70, size=num_samples)
    gender = np.random.choice(['Male', 'Female', 'Non-Binary'], size=num_samples, p=[0.48, 0.48, 0.04])
    
    # Lifestyle factors
    sleep_hours = np.random.normal(6.5, 1.5, size=num_samples).clip(2, 12)
    physical_activity = np.random.uniform(0, 10, size=num_samples) # Score 0-10
    social_interactions = np.random.uniform(0, 10, size=num_samples) # Score 0-10
    
    # Current state
    stress_level = np.random.uniform(0, 10, size=num_samples) # Score 0-10
    history_mental_illness = np.random.choice(['Yes', 'No'], size=num_samples, p=[0.2, 0.8])
    
    # Create logic for depression risk
    # Higher stress, lower sleep, lower physical activity, lower social interactions, and history increase risk
    risk_score = (stress_level * 0.3) + ((10 - sleep_hours) * 0.25) + \
                 ((10 - physical_activity) * 0.15) + ((10 - social_interactions) * 0.1) + \
                 (np.where(history_mental_illness == 'Yes', 3, 0)) + \
                 np.random.normal(0, 1, size=num_samples) # add some noise
                 
    # Normalize risk score to probability
    risk_prob = 1 / (1 + np.exp(-(risk_score - 4))) # Sigmoid shifting center
    
    # Binary classification target (Threshold at 0.5)
    depression_risk = (risk_prob > 0.5).astype(int)
    
    # Create dataframe
    df = pd.DataFrame({
        'Age': age,
        'Gender': gender,
        'Sleep_Hours': sleep_hours,
        'Physical_Activity': physical_activity,
        'Social_Interactions': social_interactions,
        'Stress_Level': stress_level,
        'History_Mental_Illness': history_mental_illness,
        'Depression_Risk': depression_risk
    })
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dummy_data.csv')
    df.to_csv(filepath, index=False)
    print(f"✅ Synthetic data generated successfully at {filepath}")
    
    print(df['Depression_Risk'].value_counts())

if __name__ == "__main__":
    generate_synthetic_data()
