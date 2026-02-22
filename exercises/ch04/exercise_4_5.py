controls = [
    "AC-2 Account Management",
    "IA-2 Identification and Authentication",
    "SC-7 Boundary Protection",
    "AU-6 Audit Review, Analysis, and Reporting",
    "CM-6 Configuration Settings",
    "IR-4 Incident Handling",
    "RA-5 Vulnerability Scanning",
    "PE-6 Monitoring Physical Access",
    "MP-2 Media Access",
    "SA-9 External System Services",
]

print("Immediate Remediation:")
for a in controls[0:3]:
    print(a)
    
print("\n")

print("30-Day Remediation:")
for b in controls[3:7]:
    print(b)
    
print("\n")
    
print("90-Day Remediation:")
for c in controls[7:]:
    print(c)
