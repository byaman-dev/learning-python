# =================================================================
# CONCEPT: BUILT-IN MODULES (The "Pre-installed" Tools)
# =================================================================

# STEP 1: THE IMPORT
# WHY: 'os' is part of the Python Standard Library. 
# It comes pre-installed so you don't need 'pip'.
# It is used to talk to your computer's File System.

import os

# STEP 2: THE LOGIC
# THE PROCESS:
# We tell the 'os' module to look at the current folder (represented by '.')
# The CPU reads the Hard Drive's index and brings the names into Python.

current_directory_contents = os.listdir('.')

# STEP 3: THE LOOP (Processing Data)
# THE PROCESS: We take the list of files and print them one by one.

print("--- Scanning Local Directory ---")
for item in current_directory_contents:
    print(f"File/Folder Found: {item}")

# SECURITY INSIGHT:
# In AI Security, this 'os' module is used to check if 
# malicious files exist in a system before an AI processes them.
