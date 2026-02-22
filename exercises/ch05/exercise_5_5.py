controls = [
    {"id": "AC-2", "status": "implemented"},
    {"id": "IA-2", "status": "partially_implemented"},
    {"id": "AU-2", "status": "not_implemented"},
    {"id": "SC-28", "status": "implemented"},
    {"id": "CM-6", "status": "planned"},
    {"id": "AC-6", "status": "not_implemented"},
]

not_implemented_count = 0

print("Controls requiring attention:")
print("-" * 35)

for control in controls:
    if control["status"] != "implemented":
        print(f"  {control['id']:>5} - {control['status']}")

    if control["status"] == "not_implemented":
        not_implemented_count += 1

print("-" * 35)
print(f"{not_implemented_count} of {len(controls)} controls require remediation.")
