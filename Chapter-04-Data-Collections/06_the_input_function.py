# --- Scenario: Security System Login ---

name = input("Enter Authorized Username: ")
id_number = input("Enter Employee ID: ") # This will be a String!

# Professional trick: Convert to int immediately if needed
age = int(input("Enter Age for Verification: "))

print(f"--- Access Log ---")
print(f"User: {name}")
print(f"ID Type: {type(id_number)}")
print(f"Age in 5 years: {age + 5}") # Works because we used int()
