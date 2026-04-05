import pandas as pd
import numpy as np
import os
import joblib
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from torch.utils.data import Dataset, DataLoader

class MentalHealthDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32).unsqueeze(1)
        
    def __len__(self):
        return len(self.X)
        
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

def load_and_preprocess_data(batch_size=32):
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dummy_data.csv')
    if not os.path.exists(filepath):
        print("Data not found. Please run generate_synthetic.py first.")
        return None, None
        
    df = pd.read_csv(filepath)
    
    X = df.drop('Depression_Risk', axis=1)
    y = df['Depression_Risk'].values
    
    numerical_cols = ['Age', 'Sleep_Hours', 'Physical_Activity', 'Social_Interactions', 'Stress_Level']
    categorical_cols = ['Gender', 'History_Mental_Illness']
    
    # Create preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_cols)
        ])
        
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Fit and transform
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    
    # Save the preprocessor for later inference
    models_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ai_models')
    os.makedirs(models_dir, exist_ok=True)
    joblib.dump(preprocessor, os.path.join(models_dir, 'preprocessor.pkl'))
    
    # Create PyTorch Datasets
    train_dataset = MentalHealthDataset(X_train_processed, y_train)
    test_dataset = MentalHealthDataset(X_test_processed, y_test)
    
    # Create DataLoaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    print(f"Data preprocessed successfully. Input features: {X_train_processed.shape[1]}")
    return train_loader, test_loader, X_train_processed.shape[1]
