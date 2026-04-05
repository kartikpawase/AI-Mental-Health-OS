import numpy as np

def predict_future_trends(historical_risk_scores, days_ahead=14):
    """
    Simulated time-series forecasting.
    Takes last 30 days of risk scores and linearly projects the next 'days_ahead'.
    """
    if len(historical_risk_scores) < 2:
        base = historical_risk_scores[-1] if historical_risk_scores else 0.5
        return [max(0, min(1, base + np.random.normal(0, 0.05))) for _ in range(days_ahead)]
        
    x = np.arange(len(historical_risk_scores))
    y = np.array(historical_risk_scores)
    
    # Simple linear regression
    slope, intercept = np.polyfit(x, y, 1)
    
    future_x = np.arange(len(historical_risk_scores), len(historical_risk_scores) + days_ahead)
    future_y = slope * future_x + intercept
    
    # Add noise
    future_y += np.random.normal(0, 0.02, size=days_ahead)
    
    # Clip between 0 and 1
    return np.clip(future_y, 0, 1).tolist()
