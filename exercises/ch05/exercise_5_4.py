mfa_enabled = True
mfa_type = "phishing_resistant"  # options: "phishing_resistant", "sms", "email", "none"
cji_access = True

if cji_access and not mfa_enabled:
    print("CRITICAL: CJI access without MFA violates CJIS IA-2")
elif mfa_enabled and (mfa_type == "sms" or mfa_type == "email"):
    print("WARNING: MFA type does not meet AAL2 requirement")
elif mfa_enabled and mfa_type == "phishing_resistant":
    print("PASS: AAL2 MFA requirement satisfied")
elif not cji_access:
    print("N/A: No CJI access, MFA check not required")
