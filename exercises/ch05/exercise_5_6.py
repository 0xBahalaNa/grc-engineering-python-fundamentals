encryption_at_rest = True
encryption_in_transit = True
fips_validated = False
key_management = True

is_compliant = encryption_at_rest and encryption_in_transit and fips_validated and key_management
print(f"System compliant: {is_compliant}")  # False

requirements = {
    "Encryption at Rest": encryption_at_rest,
    "Encryption in Transit": encryption_in_transit,
    "FIPS Validated": fips_validated,
    "Key Management": key_management,
}

for name, status in requirements.items():
    if not status:
        print(f"FAILED: {name}")

is_compliant = all([encryption_at_rest, encryption_in_transit, fips_validated, key_management])
print(f"System compliant: {is_compliant}")  # False
