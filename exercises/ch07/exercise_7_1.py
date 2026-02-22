control_families = {
    "AC": "Access Control",
    "AT": "Awareness and Training",
    "AU": "Audit and Accountability",
    "CA": "Assessment, Authorization, and Monitoring",
    "CM": "Configuration Management",
    "CP": "Contingency Planning",
    "IA": "Identification and Authentication",
    "IR": "Incident Response",
    "MA": "Maintenance",
    "MP": "Media Protection",
    "PE": "Physical and Environmental Protection",
    "PL": "Planning",
    "PM": "Program Management",
    "PS": "Personnel Security",
    "PT": "Personally Identifiable Information Processing and Transparency",
    "RA": "Risk Assessment",
    "SA": "System and Services Acquisition",
    "SC": "System and Communications Protection",
    "SI": "System and Information Integrity",
    "SR": "Supply Chain Risk Management",
}

print('=== NIST SP 800-53 Rev. 5 Control Family Lookup ===')
print('Type "quit" to exit.\n')

while True:
    abbreviation = input("Enter a control family abbreviation (e.g., AC): ").strip().upper()

    if abbreviation == "QUIT":
        print("Goodbye!")
        break

    if abbreviation in control_families:
        print(f"  {abbreviation}: {control_families[abbreviation]}\n")
    else:
        print(f"  Error: '{abbreviation}' is not a valid control family abbreviation.")
        valid_abbrs = ""
        for key in sorted(control_families.keys()):
            if valid_abbrs:
                valid_abbrs += ", "
            valid_abbrs += key
        print(f"  Valid abbreviations: {valid_abbrs}\n")
