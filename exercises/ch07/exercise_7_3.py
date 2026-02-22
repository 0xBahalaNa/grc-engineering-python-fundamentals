actions = {
    "1": "Running IAM audit...",
    "2": "Running S3 audit...",
    "3": "Running CloudTrail audit...",
    "4": "Displaying results... (no results yet)",
}

while True:
    print("\nAudit Tool Menu:")
    print("1. Run IAM Audit")
    print("2. Run S3 Audit")
    print("3. Run CloudTrail Audit")
    print("4. View Results")
    print("5. Exit")

    choice = input("\nSelect an option (1-5): ").strip()
    
    if choice =="5":
        print("Exiting. Goodbye!")
        break
    elif choice in actions:
        print(f"\n  {actions[choice]}")
    else:
        print("\n   Invalid choice. Please enter a number 1-5.")
