# =================================================================
# CONCEPT: EXTERNAL MODULES (The "Library" Analogy)
# =================================================================

# STEP 1: THE IMPORT
# WHY: We use 'import' to bring in code we didn't write.
# HOW: Python looks in the 'site-packages' folder on your hard drive.
# If you haven't run 'pip install pyjokes', this line will fail.

import pyjokes 

# STEP 2: THE EXECUTION
# THE PROCESS:
# 1. 'pyjokes' is the MODULE (The Toolbox).
# 2. 'get_joke()' is the FUNCTION (The specific tool inside).
# 3. Python sends a request to the module to return a random string.

joke = pyjokes.get_joke()

# STEP 3: THE OUTPUT
# THE PROCESS: The text is sent from your RAM to your Monitor.

print("--- System Humor Generated ---")
print(joke)

# SUMMARY: 
# This shows 'Extensibility'. Python can do anything because 
# you can download "powers" (modules) from the internet using PIP.
