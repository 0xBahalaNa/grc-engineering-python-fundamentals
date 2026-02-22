finding = {
    "id": "F-2026-042",
    "title": "S3 Bucket Lacks FIPS 140-3 Validated Encryption",
    "control_ids": ["SC-28", "SC-13"],
    "frameworks": {
        "nist": "SC-28",
        "fedramp": "SC-28",
        "cjis": "SC-28 (CJI at rest)"
    },
    "severity": "High",
    "status": "Open",
    "remediation": {
        "owner": "Cloud Engineering",
        "sla_days": 30,
        "plan": "Enable AWS KMS with FIPS 140-3 validated CMK"
    }
}

print(finding["title"])
print(finding["frameworks"]["cjis"])
print(finding["remediation"]["sla_days"])
print(finding["control_ids"])
