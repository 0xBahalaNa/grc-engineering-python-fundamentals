open_findings = ["AC-1", "IR-4", "CM-6", "SC-7", "RA-5"]
closed_findings = []

print("=== Remediation Tracker ===")
print(f"You have {len(open_findings)} open findings to remediate.\n")

# loop runs as long as there are open findings left
while open_findings:
    print(f"  Open: {', '.join(open_findings)}")
    control_id = input("\nWhich control did you remediate? ").strip().upper()

    if control_id in open_findings:
        open_findings.remove(control_id)   # remove from open
        closed_findings.append(control_id)  # add to closed
        print(f"  [OK] {control_id} closed. {len(open_findings)} remaining.\n")
    else:
        print(f"  [FAIL] '{control_id}' is not in the open findings list.\n")

# all findings closed
print("=" * 40)
print("  All findings remediated!")
print(f"  Closed: {', '.join(closed_findings)}")
print("=" * 40)
