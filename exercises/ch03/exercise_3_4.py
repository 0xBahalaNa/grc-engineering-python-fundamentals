audit_scope = []

audit_scope.append("AC-2")
print(audit_scope)
audit_scope.append("IA-2")
print(audit_scope)
audit_scope.append("AU-2")
print(audit_scope)
audit_scope.append("SC-28")
print(audit_scope)

audit_scope.insert(0, "AC-1")

print(audit_scope)

popped_audit_scope = audit_scope.pop()

print(popped_audit_scope)

audit_scope.remove("AU-2")

del audit_scope[0]

print(audit_scope)