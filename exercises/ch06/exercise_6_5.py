evidence_log = [
    {
        "timestamp": "2026-02-01T09:00:00Z",
        "control": "AC-2",
        "source": "iam_audit",
        "result": "pass",
    },
    {
        "timestamp": "2026-02-01T09:01:00Z",
        "control": "SC-28",
        "source": "s3_audit",
        "result": "fail",
    },
    {
        "timestamp": "2026-02-01T09:05:00Z",
        "control": "AU-6",
        "source": "cloudtrail_review",
        "result": "pass",
    },
    {
        "timestamp": "2026-02-01T09:12:00Z",
        "control": "IA-2",
        "source": "mfa_check",
        "result": "fail",
    },
    {
        "timestamp": "2026-02-01T09:20:00Z",
        "control": "SC-7",
        "source": "vpc_scan",
        "result": "pass",
    },
]

# One-line summary of each record
for e in evidence_log:
    print(f"{e['timestamp']} | {e['control']} | {e['source']} | {e['result']}")

# Only the failed checks
failed_checks = [e for e in evidence_log if e["result"] == "fail"]
print(f"\nFailed checks ({len(failed_checks)}):")
for e in failed_checks:
    print(f"  {e['control']} - {e['source']}")

# Count passes vs. failures
results = [e["result"] for e in evidence_log]
print(f"\nPasses: {results.count('pass')}")
print(f"Failures: {results.count('fail')}")