# Compliance requirements — all must be True for the system to pass
encryption_at_rest = True
encryption_in_transit = True
fips_validated = False
key_management = True

# `and` short-circuits: stops at the first False for efficiency
is_compliant = encryption_at_rest and encryption_in_transit and fips_validated and key_management
print(f"System compliant: {is_compliant}")  # False

# Dictionary pairs readable names with statuses for easy failure reporting
requirements = {
    "Encryption at Rest": encryption_at_rest,
    "Encryption in Transit": encryption_in_transit,
    "FIPS Validated": fips_validated,
    "Key Management": key_management,
}

# Loop isolates and prints only the failed requirements
for name, status in requirements.items():
    if not status:
        print(f"FAILED: {name}")

# `all()` replaces the `and` chain — more Pythonic and scales better
is_compliant = all([encryption_at_rest, encryption_in_transit, fips_validated, key_management])
print(f"System compliant: {is_compliant}")  # False