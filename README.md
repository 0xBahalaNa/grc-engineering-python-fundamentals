# python-grc-fundamentals

Python fundamentals learned through GRC Engineering problems. Every exercise uses compliance data — controls, findings, evidence records, and framework mappings — instead of generic examples.

## What This Is

A complete set of Python exercises paralleling [Python Crash Course](https://nostarch.com/python-crash-course-3rd-edition) by Eric Matthes, recontextualized for GRC Engineering. The concepts are identical (variables, lists, dictionaries, functions, classes, files, testing). The data is NIST 800-53, FedRAMP High, and CJIS v6.0.

Chapters 1–11 cover fundamentals. Chapters 12–20 replace the book's projects (Alien Invasion, data visualization, Django web app) with three GRC-relevant builds:

- **Project 1:** GRC Audit CLI Tool (Chapters 12–14)
- **Project 2:** Compliance Data Analysis (Chapters 15–17)
- **Project 3:** Compliance API with Flask (Chapters 18–20)

## Repository Structure

```
python-grc-fundamentals/
├── exercises/
│   ├── ch01/
│   ├── ch02/
│   ├── ...
│   ├── ch11/
│   ├── project1_audit_cli/
│   ├── project2_data_analysis/
│   └── project3_compliance_api/
├── compliance_utils.py
├── grc_python_crash_course.md
├── CLAUDE.md
└── README.md
```

## Progress

| Chapter | Topic | Status |
|---------|-------|--------|
| 1 | Getting Started | Complete |
| 2 | Variables and Simple Data Types | In Progress |
| 3 | Introducing Lists | Not Started |
| 4 | Working with Lists | Not Started |
| 5 | if Statements | Not Started |
| 6 | Dictionaries | Not Started |
| 7 | User Input and while Loops | Not Started |
| 8 | Functions | Not Started |
| 9 | Classes | Not Started |
| 10 | Files and Exceptions | Not Started |
| 11 | Testing Your Code | Not Started |
| 12–14 | Project 1: GRC Audit CLI Tool | Not Started |
| 15–17 | Project 2: Compliance Data Analysis | Not Started |
| 18–20 | Project 3: Compliance API | Not Started |

## Frameworks Referenced

- **NIST 800-53 Rev 5** — control IDs, families, and baselines used throughout all exercises
- **FedRAMP High** — baseline selection, evidence collection, and continuous monitoring exercises
- **CJIS v6.0** — MFA validation, FIPS 140-3 encryption checks, and CJI access controls

## How I'm Learning

Exercises are worked through manually with no AI-generated solutions. The [`CLAUDE.md`](CLAUDE.md) file configures Claude Code as a tutor that reviews my work, runs my code, and gives hints — but never writes solutions. The full exercise set is in [`grc_python_crash_course.md`](grc_python_crash_course.md).