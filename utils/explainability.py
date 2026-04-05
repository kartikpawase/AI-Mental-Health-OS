import numpy as np

def generate_shap_explanation(input_features, feature_names):
    """
    Generate Feature Importance (Mocking SHAP for system stability without model file).
    Outputs a dictionary mapping features to their contribution impact.
    """
    impacts = {}
    total_impact = 0
    for name, val in zip(feature_names, input_features):
        try:
            val_float = float(val)
        except:
            val_float = 1.0 # default for string categoricals
            
        # Mock logic
        if name == 'Sleep_Hours':
             impact = - (val_float - 6.5) * 0.05
        elif name == 'Stress_Level':
             impact = (val_float - 5.0) * 0.04
        else:
             impact = val_float * np.random.uniform(-0.02, 0.03)
             
        impacts[name] = round(impact, 4)
        total_impact += impact
        
    return {
        "feature_impacts": impacts,
        "base_value": 0.50,
        "prediction_value": round(0.50 + total_impact, 4)
    }
