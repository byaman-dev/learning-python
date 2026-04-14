'''
PROJECT: Ultra-Nihongo Translator Pro
EXPANDED DATABASE: 30+ Core Terms
CONCEPTS: Dictionary Comprehension (Ch 5), String formatting (Ch 3), 
          List iteration (Ch 4), and formatted printing.
'''

import os

# --- CHAPTER 5: THE EXPANDED DATA BASE ---
# Organizing by categories for better management
vocabulary = {
    # Greetings & Basics
    "hello": "konnichiwa",
    "goodbye": "sayonara",
    "thanks": "arigato",
    "yes": "hai",
    "no": "iie",
    "please": "onegaishimasu",
    
    # People
    "friend": "tomodachi",
    "teacher": "sensei",
    "student": "gakusei",
    "family": "kazoku",
    "child": "kodomo",
    
    # Places & Things
    "water": "mizu",
    "food": "tabemono",
    "book": "hon",
    "school": "gakko",
    "home": "ie",
    "money": "okane",
    "phone": "denwa",
    
    # Numbers (1-10)
    "one": "ichi",
    "two": "ni",
    "three": "san",
    "four": "yon",
    "five": "go",
    "six": "roku",
    "seven": "nana",
    "eight": "hachi",
    "nine": "kyu",
    "ten": "ju",
    
    # Verbs/Action words
    "eat": "taberu",
    "drink": "nomu",
    "read": "yomu",
    "sleep": "neru"
}

# --- CHAPTER 4 & 5: DYNAMIC REVERSE MAPPING ---
# Create Japanese to English automatically
jap_to_eng = {val: key for key, val in vocabulary.items()}

def run_translator():
    # --- CHAPTER 3: STRING FORMATTING & ESCAPE SEQUENCES ---
    print("\n" + "="*40)
    print("      ULTRA-NIHONGO TRANSLATOR PRO      ")
    print("="*40)
    print("\nModes Available:\n\t[1] English -> Japanese\n\t[2] Japanese -> English")
    
    choice = input("\nSelect Mode (1/2): ").strip()

    # Determine dictionary and language labels
    if choice == "1":
        active_dict = vocabulary
        source_lang, target_lang = "English", "Japanese"
    elif choice == "2":
        active_dict = jap_to_eng
        source_lang, target_lang = "Japanese", "English"
    else:
        print("Invalid choice. Exiting...")
        return

    print(f"\n--- {source_lang} to {target_lang} Mode Active ---")
    query = input(f"Enter {source_lang} text: ").lower().strip()

          
