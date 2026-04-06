# Chapter 2: Setup Verification
# This script confirms that Python is correctly installed and can access system info.

import sys
import platform

def check_setup():
    print("--- 🛠️ Python Environment Report ---")
    print(f"Python Version: {sys.version}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Status: Local Environment is READY! ✅")
    print("-------------------------------------")

if __name__ == "__main__":
    check_setup()
 
