control = {
    "id": "AC-2",
    "name": "Account Management",
    "family": "Access Control",
    "baseline_impact": ["Low", "Moderate", "High"],
    "status": "implemented",
    "evidence_location": "s3://audit-evidence/ac-2/"
}

print(control["id"])
print(control["name"])
print(control["family"])
print(control["baseline_impact"])
print(control["status"])
print(control["evidence_location"])

control["last_assessed"] = "2026-01-15"
control["status"] = "partially_implemented"
del control["evidence_location"]

print(control)
