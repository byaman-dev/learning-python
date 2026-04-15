'''
PROJECT: SecurePass - Password Resolver
CONCEPTS: Dictionary Mapping (Ch 5), String Replacement (Ch 3), 
          Conditional Logic (Ch 2), and OS interactions (Ch 1).
'''

import os

# --- CHAPTER 5: SUBSTITUTION DATABASE ---
# Defining how characters should be "hardened"
SECURE_MAP = {
    "a": "@",
    "s": "$",
    "i": "1",
    "o": "0",
    "t": "7",
    "e": "3",
    "b": "8",
    "g": "9",
    "h": "#"
}

def encrypt_password(plain_text):
    # --- CHAPTER 3: STRING MANIPULATION ---
    # We start with the original text
    secured_pass = plain_text
    
    # We loop through our dictionary and replace characters
    for key, value in SECURE_MAP.items():
        secured_pass = secured_pass.replace(key, value)
        # Note: .replace() returns a NEW string (Ch 3 concept: Strings are immutable)
        
    return secured_pass

# --- CHAPTER 2: LOGIC & VARIABLES ---
print("--- SECUREPASS PRO: VAULT EDITION ---")
user_input = input("Enter a simple password to harden: ").lower().strip()

# Checking length requirement (Ch 2/3)
if len(user_input) < 6:
    print("⚠️ Warning: Password is too short! Use at least 6 characters.")
else:
    # Processing
    final_password = encrypt_password(user_input)
    
    # --- CHAPTER 1 & 3: FORMATTED OUTPUT ---
    print("\n" + "*"*30)
    print(f"Original: {user_input}")
    print(f"Secured:  {final_password}")
    print("*"*30)
    
    # --- CHAPTER 5: SETS (Analysis) ---
    unique_chars = set(final_password)
    print(f"\nComplexity Score: {len(unique_chars)} unique symbols used.")

print("\n[System]: Encryption cycle complete.")
