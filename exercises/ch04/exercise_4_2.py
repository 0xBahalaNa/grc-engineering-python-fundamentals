findings = [
    {"id": "F-001", "control": "AC-2", "severity": "High"},
    {"id": "F-002", "control": "IA-2", "severity": "Critical"},
    {"id": "F-003", "control": "AU-6", "severity": "Medium"},
    {"id": "F-004", "control": "SC-28", "severity": "High"},
    {"id": "F-005", "control": "CM-6", "severity": "Low"},
  ]

for finding in findings:
    print(f'Finding {finding["id"]}: {finding["control"]} — Severity: {finding["severity"]}')
