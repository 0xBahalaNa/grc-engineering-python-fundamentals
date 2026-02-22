ac_controls = [f"AC-{i}" for i in range(1, 26)]
au_controls = [f"AU-{i}" for i in range(1, 17)]

ac_au_controls = ac_controls + au_controls

print(ac_au_controls)
print(len(ac_au_controls))
