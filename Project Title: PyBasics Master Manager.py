'''
PROJECT: PyBasics Master Manager
AUTHOR: [Your Name]
DESCRIPTION: A comprehensive project combining Chapters 1-5 of CodeWithHarry's Python Course.
CONCEPTS: Modules, Pip, Strings, Lists, Tuples, Dictionaries, and Sets.
'''

# --- CHAPTER 1: MODULES, COMMENTS & PIP ---
# Importing built-in modules (os) and external modules (pyttsx3)
# To run this, install the external module first: pip install pyttsx3
import os 
import pyttsx3 

def welcome_message():
    engine = pyttsx3.init()
    engine.say("Welcome to the Python Master Manager")
    engine.runAndWait()

# --- CHAPTER 2: VARIABLES & DATA TYPES ---
# Using different data types: int, str, and input() function
app_version = 1.0  # Float
is_active = True   # Boolean
print(f"Running App Version: {app_version}")
