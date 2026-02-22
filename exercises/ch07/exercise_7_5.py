sla_map = {
    "Critical": 7,
    "High": 30,
    "Medium": 90,
    "Low": 180,
}

while True:
    severity = input("Enter a severity level (Critical, High, Medium, Low): ")
    severity = severity.title()  # Normalize: "critical" -> "Critical"

    if severity in sla_map:
        print(f"SLA for {severity}: {sla_map[severity]} days")
        break
    else:
        print(f"'{severity}' is not valid. Please try again.")
