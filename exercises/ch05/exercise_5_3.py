test_levels = ["high", "moderate", "low"]

for data_sensitivity in test_levels:
    if data_sensitivity == "high":
        baseline = "FedRAMP High (421 controls)"
    elif data_sensitivity == "moderate":
        baseline = "FedRAMP Moderate (325 controls)"
    elif data_sensitivity == "low":
        baseline = "FedRAMP Low (156 controls)"
    else:
        baseline = "Unknown sensitivity level"
        
    print(f"{data_sensitivity:>10} -> {baseline}")
    
    