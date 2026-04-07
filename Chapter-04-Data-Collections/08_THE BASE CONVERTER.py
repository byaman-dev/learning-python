# ==========================================================
# LAB: THE BASE CONVERTER (LOW-LEVEL DATA VISUALIZATION)
# PURPOSE: Understanding Binary (0s and 1s) and Hexadecimal
# ==========================================================

# 1. THE DECIMAL SOURCE
# This is a standard 'Base-10' integer used in everyday math.
secret_key = 255 

# 2. THE TRANSLATION PHASE
# Computers don't understand '255'. They only understand ON/OFF signals.

# bin() converts our integer into 'Base-2' (Binary).
# The output starts with '0b' to tell Python "This is a Binary number."
binary_val = bin(secret_key)

# hex() converts our integer into 'Base-16' (Hexadecimal).
# The output starts with '0x'. This is the standard for Memory Addresses.
hex_val = hex(secret_key)



# 3. ANALYSIS & REPORTING
# We use f-strings to compare how the SAME value looks in different languages.

print(f"--- [NETWORK KEY DECODED] ---")
print(f"Decimal (Human Readable): {secret_key}")

# 255 in Binary is 11111111 (8 bits / 1 Byte).
print(f"Binary (Machine Level)  : {binary_val}")  

# 255 in Hex is 'ff'. This is common in Web Colors and MAC Addresses.
print(f"Hexadecimal (Dev Level) : {hex_val}") 

# ==========================================================
# SECURITY TAKEAWAY: 
# Most encryption keys and malware signatures are written in Hex.
# Mastering these conversions allows you to analyze network packets 
# and binary files at a professional level.
# ==========================================================
