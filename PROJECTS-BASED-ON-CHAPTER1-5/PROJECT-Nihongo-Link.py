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
