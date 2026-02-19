nist_to_cjis = {
    "AC-2": "AC-2 (Account Management)",
    "IA-2": "IA-2 (AAL2 MFA required for CJI)",
    "AU-2": "AU-2 (CJI access audit logging)",
    "SC-28": "SC-28 (FIPS 140-3 encryption at rest for CJI)",
    "SC-7": "SC-7 (CJI enclave boundary protection)",
}

for key, value in nist_to_cjis.items():
    print(f"NIST {key} -> CJIS: {value}")   

for key in nist_to_cjis.keys():
    print(key)

for value in nist_to_cjis.values():
    print(value)

if "CM-6" not in nist_to_cjis:
    print("CM-6 is not in this NIST to CJIS mapping.")
    nist_to_cjis["CM-6"] = "CM-6 (Configuration Settings)"

print(nist_to_cjis)
