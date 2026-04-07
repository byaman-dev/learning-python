# ==========================================================
# LAB: IDENTITY VAULT (DATA TYPE INTEGRITY)
# PURPOSE: Demonstrate Input Handling & Type Casting
# ==========================================================

# 1. DATA ACQUISITION PHASE
# The input() function always captures data as a 'String' (text).
# For security logic, we must transform this raw data into usable types.

# Capture 'name' as a standard String (str)
name = input("Enter Name: ") 

# 'age' must be an Integer (int) for mathematical operations.
# int() is used here to 'Cast' the string input into a whole number.
age = int(input("Enter Age: "))  

# 'clearance' requires precision, so we use a Floating Point (float).
# float() allows for decimal values (e.g., 95.5).
clearance = float(input("Enter Security Clearance (0.0 - 100.0): "))



# 2. LOGICAL PROCESSING PHASE
# Now that 'age' is an integer, we can perform arithmetic.
# If we hadn't cast it to int(), this line would cause a 'TypeError'.
future_age = age + 5

# 3. DATA OUTPUT PHASE (REPORTING)
# We use 'f-strings' (formatted strings) for professional output.
# The { } curly braces allow us to inject variables directly into the text.

print(f"\n--- [SYSTEM ACCESS GRANTED] ---")

# Accessing the string and float variables
print(f"User: {name} | Clearance: {clearance}%")

# Displaying the result of our calculation
print(f"In 5 years, this user will be {future_age} years old.")

# ==========================================================
# SECURITY TAKEAWAY: 
# "Sanitizing" inputs by casting them to specific types (int/float) 
# is the first step in preventing malicious data injection.
# ==========================================================
