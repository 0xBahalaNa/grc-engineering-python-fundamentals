# GRC Engineering Python Fundamentals Template

Python fundamentals learned through GRC Engineering problems. Every exercise uses compliance data (controls, findings, evidence records, and framework mappings) instead of generic examples.

## What This Is

A complete set of Python exercises paralleling [Python Crash Course](https://nostarch.com/python-crash-course-3rd-edition) by Eric Matthes, recontextualized for GRC Engineering. The concepts are identical (variables, lists, dictionaries, functions, classes, files, testing). The data is NIST 800-53, FedRAMP High, and CJIS v6.0.

Chapters 1–11 cover fundamentals. Chapters 12–20 replace the book's projects (Alien Invasion, data visualization, Django web app) with three GRC-relevant builds:

- **Project 1:** GRC Audit CLI Tool (Chapters 12–14)
- **Project 2:** Compliance Data Analysis (Chapters 15–17)
- **Project 3:** Compliance API with Flask (Chapters 18–20)

## Differences from Python Crash Course (3rd Edition)

The exercises in Chapters 1–11 follow the book's concept progression closely. The projects diverge intentionally:

- **`argparse`** (Chapters 12–14). Not covered in PCC3E. The CLI audit tool project uses it for command-line argument parsing, which is standard for the type of tools GRC Engineers build. It's part of Python's standard library and straightforward to pick up; the exercise doc provides enough context.
- **Flask** (Chapters 18–20). PCC3E teaches Django. Flask is used here because it's lighter weight and better suited for a small compliance API. If you've completed the Django chapters in the book, the concepts transfer directly.
- **PyYAML** (Exercise 10-7). Not in PCC3E. YAML is the configuration format used by most compliance-as-code tools (Cloud Custodian, Kubernetes, CI/CD pipelines), so it's included as a `pip install pyyaml` exercise.

None of these require the book to complete. The exercise descriptions in `grc_python_crash_course.md` are self-contained.

## Getting Started

1. Clone this repository
2. Open the exercise reference: [`grc_python_crash_course.md`](grc_python_crash_course.md)
3. Start with Chapter 1. Each exercise file has a docstring describing what to build
4. Read the full requirements in `grc_python_crash_course.md` before writing your solution

### Using Claude Code as a Tutor

The [`CLAUDE.md`](CLAUDE.md) file configures Claude Code as a Python tutor that reviews your work, runs your code, and gives hints, but never writes solutions. When you start a new chapter, it will give you a high-level overview of the Python concepts covered and what kinds of problems the exercises will ask you to solve. If you use Claude Code, it will follow these rules automatically.

### Recommended Git Workflow

Create a branch per chapter:
```
git checkout -b ch02-variables
```

Commit after each exercise:
```
git add exercises/ch02/exercise_2_1.py
git commit -m "feat(ch02): complete exercise 2-1 control variables"
```

Merge to main when a chapter is complete:
```
git checkout main
git merge ch02-variables
git branch -d ch02-variables
```

## Repository Structure

```
grc_engineering_python_fundamentals/
├── exercises/
│   ├── ch01/
│   ├── ch02/
│   ├── ...
│   ├── ch11/
│   ├── project1_audit_cli/
│   ├── project2_data_analysis/
│   └── project3_compliance_api/
├── compliance_utils.py          ← you create this in Exercise 8-7
├── grc_python_crash_course.md
├── CLAUDE.md
└── README.md
```

## Progress

| Chapter | Topic | Exercises | Status |
|---------|-------|-----------|--------|
| 1 | Getting Started | 3 | Not Started |
| 2 | Variables and Simple Data Types | 6 | Not Started |
| 3 | Introducing Lists | 5 | Not Started |
| 4 | Working with Lists | 7 | Not Started |
| 5 | if Statements | 6 | Not Started |
| 6 | Dictionaries | 6 | Not Started |
| 7 | User Input and while Loops | 5 | Not Started |
| 8 | Functions | 7 | Not Started |
| 9 | Classes | 6 | Not Started |
| 10 | Files and Exceptions | 7 | Not Started |
| 11 | Testing Your Code | 6 | Not Started |
| 12–14 | Project 1: GRC Audit CLI Tool | n/a | Not Started |
| 15–17 | Project 2: Compliance Data Analysis | n/a | Not Started |
| 18–20 | Project 3: Compliance API | n/a | Not Started |

## Frameworks Referenced

- **NIST 800-53 Rev 5.** Control IDs, families, and baselines used throughout all exercises
- **FedRAMP High.** Baseline selection, evidence collection, and continuous monitoring exercises
- **CJIS v6.0.** MFA validation, FIPS 140-3 encryption checks, and CJI access controls

## License

MIT. Full text in [LICENSE](LICENSE).
