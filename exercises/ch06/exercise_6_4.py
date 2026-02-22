finding_controls = ["AC-2", "AC-6", "IA-2", "AC-2", "SC-28", "AU-6",
                    "AC-2", "IA-2", "SC-7", "AU-2", "AC-6", "IA-5"]

finding_count = {}

for finding_control in finding_controls:
    finding_count[finding_control] = finding_count.get(finding_control, 0) + 1

print(finding_count)

max_control = None
max_value = 0

for control in finding_count:
    if finding_count[control] > max_value:
        max_value = finding_count[control]
        max_control = control

print(f"\nMost findings: {max_control} ({max_value})")

# --- Manual sort (selection sort, descending) ---
sorted_controls = list(finding_count.keys())

for i in range(len(sorted_controls)):
    max_idx = i
    for j in range(i + 1, len(sorted_controls)):
        if finding_count[sorted_controls[j]] > finding_count[sorted_controls[max_idx]]:
            max_idx = j
    sorted_controls[i], sorted_controls[max_idx] = sorted_controls[max_idx], sorted_controls[i]

for control in sorted_controls:
    print(f"    {control}: {finding_count[control]}")
