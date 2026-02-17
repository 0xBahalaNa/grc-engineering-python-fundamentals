test_levels = ["Critical", "High", "Medium", "Low", "Banana"]

for severity in test_levels:
    print(f"{severity:>10} -> ", end="")
    if severity == "Critical":
        print("Escalate to CISO immediately.")
    elif severity == "High":
        print("Assign to remediation team. 30-day SLA.")
    elif severity == "Medium":
        print("Add to quarterly remediation plan.")
    elif severity == "Low":
        print("Accept risk or add to backlog.")
    else:
        print("Unknown severity. Review finding.")
