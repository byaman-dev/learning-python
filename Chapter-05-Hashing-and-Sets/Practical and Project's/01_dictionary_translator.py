# Project: Hindi-to-English Security Lexicon
# Concept: Dictionary Key-Value Mapping & Safe Retrieval

# 1. Define the Dictionary
# In a research context, this acts as your 'Lookup Table'
oxford_hindi = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat",
    "shakti": "Power",
    "suraksha": "Security"
}

print("--- Welcome to the Python Research Translator ---")
print("Options: madad, kursi, billi, shakti, suraksha")

# 2. User Input
word = input("\nEnter the Hindi word you want to translate: ").lower()

# 3. Safe Retrieval Logic
# We use .get() instead of oxford_hindi[word] to prevent a 'KeyError' crash
translation = oxford_hindi.get(word)

# 4. Conditional Output
if translation:
    print(f"✅ The English translation of '{word}' is: {translation}")
else:
    print("❌ Error: Word not found in the current dataset.")

# Research Note: This logic is the foundation for mapping 
# Error Codes to Human-Readable messages in AI Systems.
