import os
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import sys

# Add parent directory to path to import data modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.preprocess import load_and_preprocess_data
from neural_net import NeuroGuardDNN

def train_model():
    train_loader, test_loader, input_dim = load_and_preprocess_data(batch_size=64)
    if not train_loader:
        return
        
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = NeuroGuardDNN(input_dim).to(device)
    
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
    
    epochs = 30
    print("Starting training...")
    for epoch in range(epochs):
        model.train()
        train_loss = 0
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
            
        if (epoch + 1) % 5 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {train_loss/len(train_loader):.4f}")
            
    # Evaluation
    model.eval()
    all_preds = []
    all_targets = []
    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            X_batch = X_batch.to(device)
            outputs = model(X_batch)
            preds = (outputs >= 0.5).float().cpu().numpy()
            all_preds.extend(preds)
            all_targets.extend(y_batch.numpy())
            
    acc = accuracy_score(all_targets, all_preds)
    f1 = f1_score(all_targets, all_preds)
    cm = confusion_matrix(all_targets, all_preds)
    
    print("\n--- Evaluation Metrics ---")
    print(f"Accuracy: {acc:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"Confusion Matrix:\n{cm}")
    
    # Save model
    models_dir = os.path.dirname(os.path.abspath(__file__))
    torch.save(model.state_dict(), os.path.join(models_dir, 'neuroguard_model.pth'))
    print("Model saved successfully as 'neuroguard_model.pth'")

if __name__ == "__main__":
    train_model()
