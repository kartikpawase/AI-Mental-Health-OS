def check_demographic_fairness(df, demographic_column, target_column, prediction_column):
    """
    Evaluates model accuracy across different groups of a demographic to spot bias.
    """
    if df.empty:
        return {}
        
    groups = df[demographic_column].unique()
    fairness_metrics = {}
    
    for group in groups:
        group_df = df[df[demographic_column] == group]
        if group_df.empty:
            continue
            
        correct = (group_df[target_column] == group_df[prediction_column]).sum()
        total = len(group_df)
        acc = correct / total
        
        fairness_metrics[group] = {
            "accuracy": round(acc, 4),
            "sample_size": total
        }
        
    return fairness_metrics
