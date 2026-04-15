'''
PROJECT: SecurePass Ultra
DESCRIPTION: Full A-Z Substitution Cipher for maximum password hardening.
CONCEPTS: Exhaustive Dictionary Mapping, String Iteration, and Complexity Analytics.
'''

# --- CHAPTER 5: THE GLOBAL SUBSTITUTION DATABASE ---
# Every letter of the alphabet is mapped to a symbol or number
SECURE_MAP = {
    "a": "@", "b": "8", "c": "(", "d": "|)", "e": "3",
    "f": "#", "g": "9", "h": "#", "i": "!", "j": "]",
    "k": "|<", "l": "1", "m": "/\\/\\", "n": "|\\|", "o": "0",
    "p": "|>", "q": "(,)", "r": "|2", "s": "$", "t": "7",
    "u": "(_)", "v": "\\/", "w": "\\/\\/", "x": "}{", "y": "j",
    "z": "2"
}

def harden_password(text):
    # We convert to lowercase to match our dictionary keys
    text = text.lower()
    
    # --- CHAPTER 3 & 4: TRANSFORMATION LOGIC ---
    # We create an empty list to store our new characters
    secured_chars = []
    
    for char in text:
        # If the character is in our dict, swap it. 
        # If not (like a number or space), keep it as is.
        new_char = SECURE_MAP.get(char, char)
        secured_chars.append(new_char)
    
    # Join the list back into a string (Ch 3)
    return "".join(secured_chars)

# --- EXECUTION ---
print("--- SECUREPASS ULTRA: A-Z HARDENING ---")
raw_pass = input("Enter your base password: ").strip()

if len(raw_pass) > 0:
    encrypted = harden_password(raw_pass)
    
    print("\n" + "="*40)
    print(f"BASE PASSWORD:    {raw_pass}")
    print(f"HARDENED VERSION: {encrypted}")
    print("="*40)
    
    # --- CHAPTER 5: SETS (Security Check) ---
    unique_symbols = set(encrypted)
    print(f"Unique Characters: {len(unique_symbols)}")
    print(f"Security Level: {'HIGH' if len(encrypted) > 8 else 'MEDIUM'}")
else:
    print("Error: Password cannot be empty.")
