# ==========================================================
# LAB: ADVANCED SECURITY LEXICON (MULTI-DIMENSIONAL MAPPING)
# PURPOSE: Implement Nested Lookups & Reverse Search Logic
# ==========================================================

# 1. DATA ARCHITECTURE PHASE
# We use a nested dictionary to store not just a translation, 
# but also 'Risk Level' or 'Context', mimicking a security database.
lexicon = {
    "madad": {"en": "Help", "type": "Urgent", "id": 101},
    "kursi": {"en": "Chair", "type": "Object", "id": 102},
    "billi": {"en": "Cat", "type": "Entity", "id": 103},
    "shakti": {"en": "Power", "type": "System", "id": 104},
    "suraksha": {"en": "Security", "type": "Protocol", "id": 105}
}

print("--- [ADVANCED RESEARCH LEXICON INTERFACE] ---")

# 2. DATA RETRIEVAL PHASE (HINDI TO ENGLISH)
query = input("\nEnter Hindi term to inspect: ").lower().strip()

# Safe retrieval from the nested structure
entry = lexicon.get(query)

if entry:
    # Accessing sub-keys within the dictionary
    print(f"\n✅ DATA FOUND:")
    print(f" > English Mapping: {entry['en']}")
    print(f" > Context Type:    {entry['type']}")
    print(f" > Database ID:     {entry['id']}")
else:
    print(f"❌ ACCESS DENIED: '{query}' is not in the secure database.")

# 3. THE REVERSE LOOKUP (RESEARCH CHALLENGE)
# Dictionaries are optimized for Key -> Value. 
# Searching Value -> Key requires a loop, simulating an "Inverse Attack."
print("\n--- [REVERSE LOOKUP TEST] ---")
search_en = "Security"
found_hindi = None

for hindi_word, details in lexicon.items():
    if details['en'] == search_en:
        found_hindi = hindi_word
        break

print(f"Target 'Security' maps back to Hindi term: {found_hindi}")

# ==========================================================
# SECURITY TAKEAWAY:
# Using nested dictionaries allows us to attach 'Metadata' to 
# simple terms. In AI, this helps the model understand not 
# just the word, but the 'Risk Context' associated with it.
# ==========================================================
