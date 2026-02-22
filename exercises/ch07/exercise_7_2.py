evidence_log = []  # list to store each entry as a dictionary

print("=== Evidence Collection Tool ===")
print("Type 'done' as the Control ID when finished.\n")

while True:
    control_id = input("Control ID (or 'done'): ").strip()

    if control_id.lower() == "done":
        break

    # keep asking until user enters 'pass' or 'fail'
    result = ""
    while result not in ("pass", "fail"):
        result = input("Result (pass/fail): ").strip().lower()

    notes = input("Notes: ").strip()

    # store entry and add to log
    evidence_log.append({"control_id": control_id, "result": result, "notes": notes})
    print(f"  [OK] {control_id} recorded.\n")

# print summary
print(f"\n{'=' * 40}")
print(f"  SUMMARY - {len(evidence_log)} entries")
print(f"{'=' * 40}")

i = 1
for e in evidence_log:
    print(f"\n  {i}. [{e['result'].upper()}] {e['control_id']} - {e['notes']}")
    i += 1

# pass/fail totals
passed = 0
for e in evidence_log:
    if e["result"] == "pass":
        passed += 1
print(f"\n  Passed: {passed} | Failed: {len(evidence_log) - passed}")
