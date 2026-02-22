control_id = "AC-2(3)"

# Split on "-" to separate the family prefix from the rest.
parts = control_id.split("-")
family_prefix = parts[0]        # "AC"

# The rest is "2(3)" - split on "(" to separate base number and enchancement
rest = parts[1]                 # "2(3)"
base_number = rest.split("(")[0]

# For the enhancement, strip the closing paraenthesis

enhancement = rest.split("(")[1].rstrip(")")    # "3"

print(f"The family prefix is {family_prefix}.")
print(f"The base control number is {base_number}.")
print(f"The enhancement number is {enhancement}.")
