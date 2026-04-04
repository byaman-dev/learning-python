# Chapter 3: Modules & Pip Practice
# This script uses 'pyttsx3' which must be installed via pip:
# Command: pip install pyttsx3

import pyttsx3

def start_assistant():
    # Initialize the engine
    engine = pyttsx3.init()
    
    # Set properties (Optional: speed and volume)
    engine.setProperty('rate', 150)    
    engine.setProperty('volume', 0.9)  

    text = "Hello Aman. Chapter 3 is complete. You are now tracking your progress on GitHub. Let's move to Strings and Lists."
    
    print(f"Assistant says: {text}")
    engine.say(text)
    
    # Block until speaking is finished
    engine.runAndWait()

if __name__ == "__main__":
    start_assistant()
