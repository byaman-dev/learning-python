# =================================================================
# CONCEPT: COMPLEX MODULES (Hardware Control)
# =================================================================

# STEP 1: THE IMPORT
# WHY: 'pyttsx3' is a Text-to-Speech library.
# HOW: It acts as a bridge between Python and your computer's Sound Card.

import pyttsx3

# STEP 2: INITIALIZATION
# THE PROCESS: Python "wakes up" the speech engine in your RAM.

engine = pyttsx3.init()

# STEP 3: THE QUEUE
# THE PROCESS:
# 1. '.say()' puts the text into a "waiting line" (Buffer).
# 2. '.runAndWait()' tells the CPU to process that buffer and play sound.

engine.say("Chapter three modules and pip completed successfully.")
engine.runAndWait()

# SUMMARY: 
# Modules aren't just for math; they can control your 
# screen, your speakers, and even your camera!
