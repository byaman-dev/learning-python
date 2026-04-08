# Project: Advanced Security & Research Lexicon
# Concept: Multidirectional Mapping & Batch Retrieval

# 1. Expanded Dataset with Technical Context
# Using a Nested Dictionary structure for metadata
lexicon = {
    "madad": {"en": "Help", "type": "Noun/Verb"},
    "kursi": {"en": "Chair", "type": "Noun"},
    "billi": {"en": "Cat", "type": "Noun"},
    "shakti": {"en": "Power", "type": "Energy/Authority"},
    "suraksha": {"en": "Security", "type": "System State"}
}

def translate_batch():
    print("\n--- [Batch Translation Mode] ---")
    print("Enter multiple words separated by spaces (e.g., 'shakti suraksha'):")
    
    user_input = input(">> ").lower().split()
    
    results = []
    for word in user_input:
        # Deep retrieval from nested dictionary
        data = lexicon.get(word)
        if data:
            results.append(f"{word.upper()} -> {data['en']} ({data['type']})")
        else:
            results.append(f"{word.upper()} -> [NOT FOUND]")
    
    print("\nProcessing Results:")
    for res in results:
        print(f"📄 {res}")

def reverse_lookup():
    print("\n--- [Reverse Lookup: English to Hindi] ---")
    search_en = input("Enter English word to find Hindi equivalent: ").capitalize()
    
    # Logic: Finding a key based on a value (Classic Research Task)
    found = False
    for hindi_word, details in lexicon.items():
        if details['en'] == search_en:
            print(f"✅ Found: '{search_en}' in Hindi is '{hindi_word}'")
            found = True
            break
    
    if not found:
        print("❌ No reverse mapping exists for this term.")

# --- Main Execution Flow ---
while True:
    print("\n" + "="*40)
    print("  LEXICON RESEARCH INTERFACE v2.0")
    print("="*40)
    print("1. Batch Translate (Hindi -> English)")
    print("2. Reverse Lookup (English -> Hindi)")
    print("3. Add New Entry")
    print("4. Exit")
    
    choice = input("\nSelect System Action: ")
    
    if choice == '1':
        translate_batch()
    elif choice == '2':
        reverse_lookup()
    elif choice == '3':
        h = input("Enter Hindi word: ").lower()
        e = input("Enter English translation: ").capitalize()
        t = input("Enter context type: ")
        lexicon[h] = {"en": e, "type": t}
        print(f"Successfully integrated '{h}' into system.")
    elif choice == '4':
        break
