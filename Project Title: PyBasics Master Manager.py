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

# --- CHAPTER 3: STRINGS ---
# Demonstrating slicing, formatting, and string methods
user_name = input("Enter your name: ").strip().capitalize()
welcome_note = f"Hello {user_name}, welcome to the project!"
print(welcome_note)
print(f"Total characters in your name: {len(user_name)}")
print(f"Lowercase version: {user_name.lower()}")

# --- CHAPTER 4: LISTS & TUPLES ---
# Lists (Mutable) and Tuples (Immutable)
subjects_list = ["Python", "Java", "C++"] # This can be changed
coordinates = (28.6139, 77.2090)          # Location of Delhi (fixed)

print(f"\nDefault Subjects: {subjects_list}")
new_sub = input("Add a new subject to the list: ")
subjects_list.append(new_sub) # Adding to list
print(f"Updated Subject List: {subjects_list}")
