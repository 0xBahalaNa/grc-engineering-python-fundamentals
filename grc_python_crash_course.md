# Python Crash Course: GRC Engineering Edition

**A parallel exercise set for Python Crash Course (3rd Edition) by Eric Matthes**

Every exercise below maps to the chapter structure of the original book. The concepts are identical — the context is GRC Engineering. Work through these alongside (or instead of) the book exercises. By the end, you'll have Python fundamentals wired to compliance patterns you'll use in your portfolio tools.

> **★ Beyond PCC3e** marks a step that uses a tool or technique the book does not teach in the corresponding chapter (or at all). These are intentional, portfolio-relevant extensions — the note tells you where (if anywhere) the book covers them, so you can tell core fundamentals from added scope.

---

## Chapter 1: Getting Started

The book has you print "Hello World." You're going to print compliance output.

### Exercise 1-1: Compliance Greeting
Write a Python script that prints the following:
```
GRC Engineering Environment Initialized
Framework: NIST 800-53 Rev 5
Baseline: FedRAMP High
```

### Exercise 1-2: First Finding
Write a script that prints a formatted compliance finding:
```
FINDING: AC-2 — Account Management
SEVERITY: High
STATUS: Open
SYSTEM: Evidence Management Platform
```

### Exercise 1-3: Your Environment
Write a script that prints:
- Your Python version (just hardcode it as a string for now)
- The frameworks you're studying (NIST 800-53, FedRAMP, CJIS)
- Today's date (hardcoded string)

Run it from the command line to confirm your environment works.

---

## Chapter 2: Variables and Simple Data Types

### Exercise 2-1: Control Variables
Create variables for a NIST 800-53 control and print a formatted message:
```python
control_id = "AC-2"
control_name = "Account Management"
control_family = "Access Control"
```
Print: `"AC-2 (Account Management) belongs to the Access Control family."`

### Exercise 2-2: Framework Names
Assign `framework = "nist 800-53 rev 5"` and use string methods to print:
- The framework name in title case
- The framework name in all caps
- The framework name with leading/trailing whitespace stripped (add whitespace first)

### Exercise 2-3: Severity Arithmetic
Assign numeric severity values: Critical = 4, High = 3, Medium = 2, Low = 1.
- Calculate the average severity of three findings: Critical, High, Medium
- Print the result as a float
- Print it rounded to one decimal place using `round()`

### Exercise 2-4: Control ID Anatomy
Practice the Chapter 2 string methods (case, whitespace, prefix/suffix removal) to clean and normalize control identifiers:
```python
raw_family = "  access control  "
prefixed_id = "NIST-AC-2"
control_id = "AC-2(3)"
```
- Strip the whitespace from `raw_family` and print it in title case
- Use `removeprefix("NIST-")` on `prefixed_id` to recover `"AC-2"`
- Use `removesuffix("(3)")` on `control_id` to recover the base control `"AC-2"`, then print a label for it
- Print the family abbreviation in upper case

Splitting a control like `"AC-2(3)"` into its separate prefix / base / enhancement parts needs `split()` and indexing — you'll have those after Chapters 3–4. For now, stay with the Chapter 2 string methods above.

### Exercise 2-5: Compliance Quote
Assign a quote about compliance to a variable. Include the speaker's name in a separate variable. Print a message like:
```
NIST states: "Security is not a product, but a process."
```
Use an f-string to combine them.

### Exercise 2-6: FedRAMP Baseline Count
FedRAMP High has 421 controls. FedRAMP Moderate has 325. FedRAMP Low has 156.
- Store each in a variable
- Calculate the difference between High and Moderate
- Print: `"FedRAMP High requires {X} more controls than Moderate."`

---

## Chapter 3: Introducing Lists

### Exercise 3-1: Control Families
Create a list of the 20 NIST 800-53 Rev 5 control families using their two-letter abbreviations:
```python
families = ["AC", "AT", "AU", "CA", "CM", "CP", "IA", "IR", "MA", "MP",
            "PE", "PL", "PM", "PS", "PT", "RA", "SA", "SC", "SI", "SR"]
```
- Print the first family, the last family, and the 8th family
- Print a message for the 7th family: `"IA is critical for CJIS compliance."`

### Exercise 3-2: Finding Severities
Create a list: `severities = ["Critical", "High", "Medium", "Low", "Informational"]`
- Print each severity individually using its index
- Change `"Informational"` to `"Info"` using index assignment
- Print the modified list

### Exercise 3-3: Adding Controls to Scope
Start with an empty list called `audit_scope`. Using `append()`, add these controls one at a time: `"AC-2"`, `"IA-2"`, `"AU-2"`, `"SC-28"`.
- Print the list after each addition
- Insert `"AC-1"` at the beginning using `insert()`
- Print the final list

### Exercise 3-4: Removing Controls from Scope
Starting from your `audit_scope` list:
- Remove the last control using `pop()` and print what was removed
- Remove `"AU-2"` by value using `remove()`
- Delete the first item using `del`
- Print what remains

### Exercise 3-5: Framework List
Create a list of 5 compliance frameworks you encounter in public safety technology. Sort them:
- Print the list in alphabetical order using `sorted()` (don't modify the original)
- Print the original list to show it's unchanged
- Now permanently sort it with `.sort()`
- Reverse the order with `.reverse()`
- Print the length of the list

---

## Chapter 4: Working with Lists

### Exercise 4-1: Control Family Report
Using your `families` list from 3-1, loop through it and print:
```
Control Family: AC
Control Family: AT
Control Family: AU
...
```

### Exercise 4-2: Finding Summary
Store five findings as three parallel lists (dictionaries come in Chapter 6 — for now use lists you already know):
```python
finding_ids        = ["F-001", "F-002", "F-003", "F-004", "F-005"]
finding_controls   = ["AC-2",  "IA-2",  "AU-6",  "SC-28", "CM-6"]
finding_severities = ["High",  "Critical", "Medium", "High", "Low"]
```
- Loop with `for i in range(len(finding_ids)):` and use the index to reach the matching item in each list
- Print each finding as:
```
Finding F-001: AC-2 — Severity: High
```
(This index-pairing is exactly what dictionaries will make cleaner in Chapter 6.)

### Exercise 4-3: Control Number Generator
Use `range()` to generate control numbers for the AC (Access Control) family:
- Print `AC-1` through `AC-25`
- Create a list of these control IDs using a for loop and `append()`
- Print the total number of controls generated using `len()`

### Exercise 4-4: Severity Scores
Create a list of severity scores for 10 findings: `[4, 3, 3, 2, 4, 1, 2, 3, 4, 2]`
- Print the minimum, maximum, and sum
- Calculate and print the average severity
- Print how many findings you have

### Exercise 4-5: FedRAMP Baselines with Slicing
Create a list of 10 controls in priority order (highest priority first). Use slicing to:
- Print the top 3 priority controls (label them "Immediate Remediation")
- Print controls 4-7 (label them "30-Day Remediation")
- Print the remaining controls (label them "90-Day Remediation")

### Exercise 4-6: List Comprehension — Control IDs
Use a list comprehension to generate control IDs:
```python
ac_controls = [f"AC-{i}" for i in range(1, 26)]
```
- Create a similar list for the AU (Audit) family, AU-1 through AU-16
- Create a combined list of both families
- Print the combined list and its length

### Exercise 4-7: Tuple — Immutable Baseline
Define a tuple representing the FedRAMP High baseline version:
```python
baseline = ("FedRAMP", "High", "Rev 5", 421)
```
- Print each element
- Try to modify an element and observe the error
- Reassign the entire tuple to a new version:
  ```python
  baseline = ("FedRAMP", "High", "Rev 5.1", 425)
  ```
- Print the updated tuple

---

## Chapter 5: if Statements

### Exercise 5-1: Compliance Check
```python
control_status = "implemented"
```
Write `if` statements to test:
- Is the status `"implemented"`? Print "Control passes."
- Is the status `"not implemented"`? Print "Finding generated."
- Use `!=` to check if the status is NOT `"planned"`.

### Exercise 5-2: Severity Router
Given a severity variable, write an `if-elif-else` chain:
- `"Critical"` → print `"Escalate to CISO immediately."`
- `"High"` → print `"Assign to remediation team. 30-day SLA."`
- `"Medium"` → print `"Add to quarterly remediation plan."`
- `"Low"` → print `"Accept risk or add to backlog."`
- Anything else → print `"Unknown severity. Review finding."`

Test it with each severity level.

### Exercise 5-3: FedRAMP Baseline Selector
Given `data_sensitivity = "high"`, use `if-elif-else` to determine the FedRAMP baseline:
- `"high"` → `"FedRAMP High (421 controls)"`
- `"moderate"` → `"FedRAMP Moderate (325 controls)"`
- `"low"` → `"FedRAMP Low (156 controls)"`

Test with each value.

### Exercise 5-4: CJIS MFA Check
Write a function-like block (just inline code for now) that checks whether a system meets CJIS AAL2 MFA requirements:
```python
mfa_enabled = True
mfa_type = "phishing_resistant"  # options: "phishing_resistant", "sms", "email", "none"
cji_access = True
```
- If `cji_access` is True and `mfa_enabled` is False → "CRITICAL: CJI access without MFA violates CJIS IA-2"
- If `mfa_enabled` is True but `mfa_type` is `"sms"` or `"email"` → "WARNING: MFA type does not meet AAL2 requirements"
- If `mfa_enabled` is True and `mfa_type` is `"phishing_resistant"` → "PASS: AAL2 MFA requirement satisfied"
- If `cji_access` is False → "N/A: No CJI access, MFA check not required"

### Exercise 5-5: Control List Filtering
Given control IDs and their statuses as two parallel lists (dictionaries are Chapter 6 — stick with lists for now):
```python
control_ids      = ["AC-2", "IA-2", "AU-2", "SC-28", "CM-6", "AC-6"]
control_statuses = ["implemented", "partially_implemented", "not_implemented",
                    "implemented", "planned", "not_implemented"]
```
Loop through by index and:
- Print all controls whose status is NOT `"implemented"`
- Count how many are `"not_implemented"`
- Print a summary: `"X of Y controls require remediation."`

### Exercise 5-6: Boolean Compliance Logic
A system is compliant if ALL of the following are True:
```python
encryption_at_rest = True
encryption_in_transit = True
fips_validated = False
key_management = True
```
- Use `and` to check if all four are True. Print the result.
- Identify which requirement failed and print it.
- Bonus (★ Beyond PCC3e — `all()` is a built-in the book never introduces): use `all()` with a list of booleans to do the same check in one line.

---

## Chapter 6: Dictionaries

### Exercise 6-1: Control Record
Create a dictionary representing a NIST 800-53 control:
```python
control = {
    "id": "AC-2",
    "name": "Account Management",
    "family": "Access Control",
    "baseline_impact": ["Low", "Moderate", "High"],
    "status": "implemented",
    "evidence_location": "s3://audit-evidence/ac-2/"
}
```
- Print each value using its key
- Add a new key: `"last_assessed": "2026-01-15"`
- Modify the status to `"partially_implemented"`
- Remove the `evidence_location` key using `del`

### Exercise 6-2: Framework Crosswalk
Create a dictionary mapping NIST controls to their CJIS v6.0 equivalents:
```python
nist_to_cjis = {
    "AC-2": "AC-2 (Account Management)",
    "IA-2": "IA-2 (AAL2 MFA required for CJI)",
    "AU-2": "AU-2 (CJI access audit logging)",
    "SC-28": "SC-28 (FIPS 140-3 encryption at rest for CJI)",
    "SC-7": "SC-7 (CJI enclave boundary protection)",
}
```
- Loop through and print each mapping:
  ```
  NIST AC-2 → CJIS: AC-2 (Account Management)
  ```
- Loop through only the keys
- Loop through only the values
- Check if `"CM-6"` is in the dictionary. If not, print a message and add it.

### Exercise 6-3: Finding Record
Create a dictionary for a compliance finding. Include nested data:
```python
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
```
- Print the finding title
- Print the CJIS framework mapping
- Print the remediation SLA
- Print all control IDs the finding maps to

### Exercise 6-4: Control Family Counter
Given a list of finding control IDs:
```python
finding_controls = ["AC-2", "AC-6", "IA-2", "AC-2", "SC-28", "AU-6",
                    "AC-2", "IA-2", "SC-7", "AU-2", "AC-6", "IA-5"]
```
Build a dictionary that counts how many findings exist per control:
```
{"AC-2": 3, "AC-6": 2, "IA-2": 2, ...}
```
- Loop through and build the count manually (don't use `Counter` yet)
- Print the control with the most findings
- Print the controls sorted by control ID (use `sorted()` over the dictionary's keys — the Chapter 6 way)
- Bonus (★ Beyond PCC3e): print them sorted by count, highest first — this needs `sorted(..., key=...)`, which the book doesn't cover until Chapter 17

### Exercise 6-5: List of Dictionaries — Audit Evidence Log
Create a list of 5 evidence records:
```python
evidence_log = [
    {"timestamp": "2026-02-01T09:00:00Z", "control": "AC-2", "source": "iam_audit", "result": "pass"},
    {"timestamp": "2026-02-01T09:01:00Z", "control": "SC-28", "source": "s3_audit", "result": "fail"},
    # ... add 3 more
]
```
- Loop through and print a one-line summary of each
- Create a new list containing only the failed checks
- Print the count of passes vs. failures

### Exercise 6-6: Building a Severity Map
Build a dictionary mapping severity names to numeric scores from two parallel lists:
```python
severity_names = ["Critical", "High", "Medium", "Low", "Info"]
severity_scores = [4, 3, 2, 1, 0]
```
- Start with an empty dict and fill it with a `for` loop over `range(len(severity_names))` to produce:
  `{"Critical": 4, "High": 3, "Medium": 2, "Low": 1, "Info": 0}`
- Then build the reverse mapping with another loop: `{4: "Critical", 3: "High", ...}`

(PCC3e teaches *list* comprehensions in Chapter 4 but never *dictionary* comprehensions, so we build these dicts with an explicit loop. If you already know the `{k: v for ...}` syntax, that's a ★ Beyond-PCC3e shortcut you're free to use.)

---

## Chapter 7: User Input and while Loops

### Exercise 7-1: Interactive Control Lookup
Write a program that asks the user to input a control family abbreviation (e.g., `"AC"`) and prints the full family name. Use a dictionary for the lookup. If the family isn't found, print an error message.

Handle at least 5 families.

### Exercise 7-2: Evidence Collection Loop
Write a `while` loop that collects evidence entries from the user:
- Prompt for: control ID, result (pass/fail), and notes
- Store each entry as a dictionary in a list
- Continue until the user types `"done"` as the control ID
- When done, print a summary of all collected evidence

### Exercise 7-3: Audit Menu
Create an interactive menu:
```
Audit Tool Menu:
1. Run IAM Audit
2. Run S3 Audit
3. Run CloudTrail Audit
4. View Results
5. Exit
```
Use a `while` loop. For each selection, print a placeholder message (e.g., `"Running IAM audit..."`). Exit the loop when the user selects 5. Handle invalid inputs gracefully.

### Exercise 7-4: Remediation Tracker
Write a program that:
- Starts with a list of 5 open findings (just control IDs)
- In a loop, asks the user which control they've remediated
- Removes it from the open list and adds it to a closed list
- Prints remaining open findings after each remediation
- Exits when all findings are closed (the open list is empty)

### Exercise 7-5: Input Validation — Severity Selector
Write a loop that asks the user to input a severity level. Keep asking until they provide a valid option (`Critical`, `High`, `Medium`, `Low`). Use `.lower()` or `.title()` to normalize input. Once valid, print the corresponding SLA:
- Critical: 7 days
- High: 30 days
- Medium: 90 days
- Low: 180 days

---

## Chapter 8: Functions

### Exercise 8-1: Format Control ID
Write a function `format_control_id(family, number, enhancement=None)` that returns a properly formatted control ID:
- `format_control_id("AC", 2)` → `"AC-2"`
- `format_control_id("AC", 2, 3)` → `"AC-2(3)"`
- `format_control_id("ac", 2)` → `"AC-2"` (normalize to uppercase)

### Exercise 8-2: Severity Calculator
Write a function `calculate_risk_score(likelihood, impact)` where both are integers 1-5. Return the product as the risk score. Add a second function `categorize_risk(score)` that returns:
- 20-25: `"Critical"`
- 12-19: `"High"`
- 6-11: `"Medium"`
- 1-5: `"Low"`

Chain them: `categorize_risk(calculate_risk_score(4, 5))` → `"Critical"`

### Exercise 8-3: Control Mapper
Write a function `map_control(control_id, framework="nist")` that takes a control ID and returns the mapping for the specified framework. Use a dictionary inside the function (or passed as a parameter) for lookups. Support at least `"nist"`, `"fedramp"`, and `"cjis"` as framework options.

Return `"No mapping found"` if the control or framework is unknown.

### Exercise 8-4: Evidence Formatter
Write a function `format_evidence(control_id, result, timestamp, source, **details)` that:
- Takes required positional arguments for control, result, timestamp, and source
- Accepts arbitrary keyword arguments for additional metadata
- Returns a formatted dictionary ready for logging

Example call:
```python
format_evidence("AC-2", "pass", "2026-02-12T10:00:00Z", "iam_audit",
                assessor="automated", region="us-gov-west-1")
```

### Exercise 8-5: Batch Compliance Checker
Write a function `check_compliance(controls_list, required_status="implemented")` that:
- Takes a list of control dictionaries (each with `"id"` and `"status"` keys)
- Returns a tuple: `(compliant_list, non_compliant_list)`
- Use this to process a list of 10 controls and print a summary

### Exercise 8-6: Framework Report Generator
Write a function `generate_report(findings, *frameworks, include_remediation=False)` that:
- Takes a list of findings and one or more framework names as positional args
- Filters findings to only those relevant to the specified frameworks
- If `include_remediation` is True, includes remediation details
- Returns a formatted string report

This exercises `*args` and keyword arguments together.

### Exercise 8-7: Module Organization
Create two files:
- `compliance_utils.py` — containing your `format_control_id`, `calculate_risk_score`, and `categorize_risk` functions
- `main.py` — imports from `compliance_utils` and uses the functions

Practice both `import compliance_utils` and `from compliance_utils import format_control_id`.

---

## Chapter 9: Classes

### Exercise 9-1: The Control Class
Create a class `Control` with:
- `__init__` taking: `control_id`, `name`, `family`, `status="not_assessed"`
- A method `assess(result)` that updates the status to `"pass"` or `"fail"`
- A method `describe()` that prints a formatted summary
- A `__str__` method returning `"AC-2: Account Management [not_assessed]"` (★ Beyond PCC3e — the book's Chapter 9 stops at `__init__` and named methods; it doesn't introduce `__str__` until the Django chapter. It's a natural fit for classes, so we include it here.)

Create 3 instances, assess them, and print each.

### Exercise 9-2: The Finding Class
Create a class `Finding` with:
- Attributes: `finding_id`, `title`, `severity`, `control_ids` (list), `status="open"`
- A method `remediate()` that changes status to `"closed"` and prints a confirmation
- A method `escalate()` that upgrades severity by one level (Medium → High → Critical)
- A method `age(days)` that checks if the finding exceeds its SLA and prints a warning

### Exercise 9-3: Inheritance — Framework Control
Create a base class `BaseControl` and subclasses:
```python
class BaseControl:
    """Generic compliance control."""

class NISTControl(BaseControl):
    """Adds NIST-specific attributes: family, baseline_impact, enhancements."""

class CJISControl(NISTControl):
    """Adds CJIS-specific attributes: cji_relevant (bool), fips_required (bool)."""
```
- `CJISControl` should inherit from `NISTControl`
- Override `describe()` in each subclass to add framework-specific details
- Demonstrate that a `CJISControl` instance has attributes from all three classes

### Exercise 9-4: The AuditTool Class
Create a class `AuditTool` with:
- Attributes: `name`, `controls_assessed` (list), `results` (empty list)
- A method `run_check(control_id)` that simulates a check (randomly pass/fail) and appends to results
- A method `summary()` that prints pass/fail counts and percentages
- A method `export(format="dict")` that returns results as a list of dicts

Use `import random` for simulated results.

### Exercise 9-5: Composition — Audit Session
Create an `AuditSession` class that CONTAINS (not inherits from) multiple `AuditTool` instances:
```python
class AuditSession:
    def __init__(self, session_name, tools=None):
        self.session_name = session_name
        self.tools = tools or []
        self.start_time = None
        self.findings = []
```
- A method `add_tool(tool)` to register an AuditTool
- A method `run_all()` that executes every registered tool
- A method `generate_report()` that aggregates results from all tools

This demonstrates composition vs. inheritance, which matters for how your portfolio tools fit together.

### Exercise 9-6: Evidence Package
Create an `EvidencePackage` class that:
- Takes a `package_id` and `framework` on init
- Has an `add_evidence(control_id, evidence_dict)` method
- Has a `validate()` method that checks each evidence record has required fields: `timestamp`, `source`, `result`
- Has an `export_json()` method that returns the package as a JSON string (use `import json`) — ★ a one-chapter forward reference: the `json` module is formally taught in Chapter 10
- Handles invalid evidence gracefully with error messages, not crashes

---

## Chapter 10: Files and Exceptions

### Exercise 10-1: Read a Controls File
Create a text file `controls.txt` with one control ID per line:
```
AC-2
IA-2
AU-2
SC-28
CM-6
```
Write a program that reads the file and prints each control. Then modify it to store them in a list.

### Exercise 10-2: Write Audit Results
Write a program that creates a file `audit_results.txt` containing:
```
Audit Results — 2026-02-12
========================
AC-2: PASS
IA-2: PASS
AU-2: FAIL
SC-28: FAIL
CM-6: PASS
========================
Summary: 3 PASS, 2 FAIL
```
Use `write()` or `writelines()`.

### Exercise 10-3: JSON Evidence Files
Write a program that:
- Creates a list of evidence dictionaries (5+ entries)
- Writes them to `evidence.json` using `json.dump()` with `indent=2`
- Reads them back with `json.load()`
- Prints the data to confirm round-trip integrity

### Exercise 10-4: CSV Compliance Report
Write a program that:
- Creates compliance data (control ID, status, last assessed date, assessor)
- Writes it to `compliance_report.csv` as plain text — one record per line, fields joined with commas (`",".join(...)`) — using the file-writing and `.split(",")` techniques from this chapter
- Reads it back, splits each line on commas, and prints a formatted summary
- Handles the case where the file doesn't exist (use `try/except FileNotFoundError`)
- Bonus (★ Beyond PCC3e): redo it with the `csv` module (`csv.writer` / `csv.DictReader`). The book introduces the `csv` module in Chapter 16, so you'll use it for real in Project 2.

### Exercise 10-5: Exception Handling — Robust Input
Write a program that reads a JSON config file for an audit:
```json
{
    "framework": "fedramp_high",
    "target_account": "123456789012",
    "regions": ["us-gov-west-1", "us-gov-east-1"],
    "controls": ["AC-2", "IA-2", "SC-28"]
}
```
Handle these exceptions:
- `FileNotFoundError` — print a helpful message about creating the config
- `json.JSONDecodeError` — print a message about invalid JSON format
- `KeyError` — if a required key is missing, print which key and continue with defaults

### Exercise 10-6: Log File Analyzer
Write a program that reads a simulated CloudTrail-style log file (create it first as JSON lines):
```json
{"timestamp": "2026-02-12T10:00:00Z", "event": "ConsoleLogin", "user": "admin", "source_ip": "10.0.1.5", "success": true}
{"timestamp": "2026-02-12T10:01:00Z", "event": "ConsoleLogin", "user": "unknown", "source_ip": "203.0.113.50", "success": false}
```
- Read each line, parse the JSON
- Flag failed login attempts
- Flag logins from external IPs (anything not starting with `10.`)
- Write a summary report to `log_analysis.txt`
- Handle malformed lines gracefully

### Exercise 10-7: YAML Controls File ★ Beyond PCC3e
PCC3e never covers YAML or third-party parsing libraries — this is an intentional extension because Project 1 loads its controls from a YAML config file. Install PyYAML (`pip install pyyaml`). Write a program that:
- Reads a YAML file containing control definitions:
```yaml
controls:
  - id: AC-2
    name: Account Management
    family: Access Control
    status: implemented
  - id: IA-2
    name: Identification and Authentication
    family: Identification and Authentication
    status: partially_implemented
```
- Loads it into Python data structures
- Modifies a control's status
- Writes it back to a new YAML file
- This directly applies to your Project 1 YAML workflow.

---

## Chapter 11: Testing Your Code

### Exercise 11-1: Test format_control_id
Using `pytest`, write tests for your `format_control_id` function from Chapter 8:
```python
def test_basic_control_id():
    assert format_control_id("AC", 2) == "AC-2"

def test_with_enhancement():
    assert format_control_id("AC", 2, 3) == "AC-2(3)"

def test_lowercase_normalization():
    assert format_control_id("ac", 2) == "AC-2"
```
Add at least 2 more test cases including edge cases.

### Exercise 11-2: Test Severity Calculator
Write tests for `calculate_risk_score` and `categorize_risk`:
- Test boundary values (score of 5, 6, 11, 12, 19, 20)
- Test that invalid inputs raise appropriate errors (add error handling to the function if you haven't) — ★ Beyond PCC3e: asserting that code raises an exception uses `pytest.raises`, which the book's Chapter 11 doesn't cover (it shows only `==`/`in`-style asserts)
- Test the chained call: `categorize_risk(calculate_risk_score(5, 5))` == `"Critical"`

### Exercise 11-3: Test the Control Class
Write a test class `TestControl` using pytest:
```python
class TestControl:
    def test_initial_status(self):
        """New controls should have 'not_assessed' status."""

    def test_assess_pass(self):
        """Assessing a control as pass updates status."""

    def test_assess_fail(self):
        """Assessing a control as fail updates status."""

    def test_str_representation(self):
        """String representation follows expected format."""
```

### Exercise 11-4: Test Evidence Validation
Write tests for your `EvidencePackage.validate()` method:
- Test that valid evidence passes validation
- Test that evidence missing `timestamp` fails
- Test that evidence missing `source` fails
- Test that an empty package handles gracefully
- Use fixtures to create reusable test data

### Exercise 11-5: Test File Operations
Write tests for your JSON evidence file functions:
- Use `tmp_path` (pytest's built-in fixture) for temporary files — ★ Beyond PCC3e: the book teaches writing your *own* `@pytest.fixture` but not the built-in `tmp_path`
- Test writing and reading back produces identical data
- Test that reading a nonexistent file handles gracefully
- Test that malformed JSON raises the expected error

### Exercise 11-6: Parametrized Compliance Tests ★ Beyond PCC3e
`@pytest.mark.parametrize` isn't taught in PCC3e (Chapter 11 covers `@pytest.fixture` only) — it's included because it's the standard way to run one test body over many input cases. Use it to test multiple controls through the same test logic:
```python
@pytest.mark.parametrize("control_id,expected_family", [
    ("AC-2", "Access Control"),
    ("IA-2", "Identification and Authentication"),
    ("AU-2", "Audit and Accountability"),
    ("SC-28", "System and Communications Protection"),
    ("CM-6", "Configuration Management"),
])
def test_control_family_mapping(control_id, expected_family):
    assert get_family(control_id) == expected_family
```
Write the `get_family` function and add at least 5 more parametrized cases.

---

## Chapters 12-14: Project 1 — GRC Audit CLI Tool

**The book builds an Alien Invasion game. You're building a command-line audit tool.**

Build a CLI tool called `grc-audit` that ties together everything from Chapters 1-11:

### Milestone 1: Core Structure
- Use classes for `Control`, `Finding`, `AuditTool`, and `AuditSession`
- Load controls from a YAML configuration file
- Accept command-line arguments using `argparse`:
  ```
  python grc_audit.py --framework fedramp_high --controls AC-2 IA-2 SC-28
  ```

### Milestone 2: Simulated Checks
- Each "check" reads a JSON file simulating AWS resource state
- Compare resource state against expected control requirements
- Generate `Finding` objects for any failures

### Milestone 3: Reporting
- Generate output in three formats: text summary, JSON, and CSV
- Include: timestamp, framework, controls assessed, pass/fail counts, individual findings
- Write reports to an `output/` directory

### Milestone 4: Testing
- Write pytest tests for all core functions
- Achieve >80% coverage (use `pytest-cov`)
- Include both unit tests and integration tests

> **★ Beyond PCC3e (by design):** this capstone uses real CLI tooling the book doesn't teach — `argparse` (command-line parsing), `PyYAML` (config files), the `csv` module and `datetime` (both formally introduced in the book's Chapter 16), and `pytest-cov` (coverage). They're here because a portfolio-grade audit tool needs them; just know they're added scope, not Chapter 1–11 fundamentals.

**This project is a simplified version of your portfolio evidence collector tools. The patterns you learn here apply directly to Projects 4, 5, and 2B.**

---

## Chapters 15-17: Project 2 — Compliance Data Analysis

**The book covers data visualization. You're analyzing compliance data.**

### Milestone 1: Generate Sample Data
Write a script that generates realistic compliance assessment data:
- 100+ controls across 5 frameworks
- Random but weighted statuses (most should be "implemented")
- Timestamps spanning 12 months
- Save as CSV and JSON

### Milestone 2: Analysis with Standard Library
Using only Python standard library (`csv`, `json`, `statistics`):
- Calculate compliance percentage per framework
- Identify the most common failing controls
- Calculate average time to remediate (generate remediation timestamps)
- Identify trends over the 12-month period

### Milestone 3: Enrich from a Live API (Chapter 17)
Mirror the book's Chapter 17 "Working with APIs" using the `requests` package:
- Fetch live data from a public API — e.g., pull recent CVEs from the NVD API (`https://services.nvd.nist.gov/rest/json/cves/2.0`) or repo metadata from the GitHub API
- Check `response.status_code` before processing, and handle a non-200 response
- Parse the JSON response and join it to your generated compliance data (e.g., map CVEs to affected controls)
- Write a short test (Chapter 11) asserting `status_code == 200` and that you got the expected number of items

### Milestone 4: Visualization (Chapters 15–16)
Visualization is the through-line of the book's Chapters 15–17, so build at least one chart with matplotlib or plotly:
- Compliance percentage over time (line chart) — **required**
- Optional: findings by severity (bar chart), framework comparison (grouped bar chart), control family heatmap

**This builds the analysis skills you'll use in Project 9 (Continuous Monitoring Dashboard).**

---

## Chapters 18-20: Project 3 — Compliance API

**The book builds a Django web app. You're building a lightweight API.**

Using Flask (simpler than Django for this purpose):

### Milestone 1: Basic API
- `GET /controls` — list all controls
- `GET /controls/<id>` — get a specific control
- `POST /findings` — create a new finding
- `GET /findings` — list findings with optional severity filter

### Milestone 2: Data Persistence
- Store data in JSON files (keep it simple, no database needed)
- Load data on startup, save on changes

### Milestone 3: Compliance Endpoints
- `GET /compliance/status` — overall compliance percentage
- `GET /compliance/framework/<name>` — framework-specific status
- `GET /compliance/gaps` — list controls that are not fully implemented

### Milestone 4: User Accounts & Access Control (Chapter 19)
The book's Chapter 19 is entirely a user-authentication system (register, log in, log out, restrict data to its owner). Recreate that concept on the API side:
- Add simple authentication — an API key or token sent in a request header — and reject unauthenticated requests with `401`
- Tie findings to the user who created them (an `owner` field), and filter `GET /findings` so a user sees only their own
- Add a registration/login concept (even a minimal user store in JSON) so there is more than one identity to own data

### Milestone 5: Documentation
- Write API documentation in markdown
- Include example `curl` commands for each endpoint (including the auth header)
- Add basic input validation and error responses
- Optional (★ Chapter 20): containerize or deploy the API and run it with the debugger/reloader off, mirroring the book's deployment chapter

**This project is lower priority than Projects 1 and 2 above. Only tackle it if you want web API experience. The patterns are useful if you ever build a compliance dashboard backend.**

> **Note on the Flask-vs-Django swap:** a JSON API has no HTML templates or Bootstrap styling, so the book's Chapter 18 templates and Chapter 20 CSS work are intentionally out of scope here. The conceptual cores that *do* carry over — request routing/views (M1), data persistence (M2), and user accounts + per-user data ownership (M4) — are all represented.

---

## Appendix: GRC Data Patterns Reference

Use these patterns throughout your exercises. They're the building blocks you'll use in every portfolio project.

### Common Data Structures

```python
# A compliance control
control = {
    "id": "AC-2",
    "name": "Account Management",
    "family": "Access Control",
    "frameworks": ["NIST 800-53", "FedRAMP High", "CJIS v6.0"],
    "status": "implemented",
    "last_assessed": "2026-01-15",
    "evidence_artifacts": ["iam_audit_2026-01-15.json"]
}

# A compliance finding
finding = {
    "id": "F-2026-042",
    "title": "MFA Not Enforced for CJI Access",
    "control_ids": ["IA-2"],
    "severity": "Critical",
    "status": "open",
    "created": "2026-02-01",
    "sla_days": 7,
    "remediation_owner": "Identity Team"
}

# An evidence record
evidence = {
    "timestamp": "2026-02-12T10:30:00Z",
    "control_id": "SC-28",
    "source_tool": "s3_audit",
    "result": "fail",
    "resource_id": "arn:aws:s3:::evidence-bucket",
    "details": {
        "encryption_enabled": True,
        "fips_validated": False,
        "kms_key_id": "alias/default-key"
    }
}

# A framework crosswalk entry
crosswalk = {
    "nist_control": "SC-28",
    "fedramp_control": "SC-28",
    "cjis_requirement": "SC-28: FIPS 140-3 encryption required for CJI at rest",
    "cjis_exceeds_fedramp": True,
    "notes": "CJIS requires agency-managed keys; FedRAMP does not"
}
```

### Common Operations You'll Repeat
- Reading/writing JSON and YAML files
- Filtering lists of dictionaries by key values
- Counting occurrences (severity distribution, status distribution)
- Mapping control IDs across frameworks
- Generating formatted reports from structured data
- Validating data against expected schemas
- Handling missing or malformed data gracefully

### Severity SLA Reference
| Severity | NIST Risk Level | Typical SLA | FedRAMP POA&M |
|----------|----------------|-------------|---------------|
| Critical | Very High | 7 days | 30 days |
| High | High | 30 days | 90 days |
| Medium | Moderate | 90 days | 180 days |
| Low | Low | 180 days | 365 days |
