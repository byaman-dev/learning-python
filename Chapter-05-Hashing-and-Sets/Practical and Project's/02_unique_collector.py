# ==========================================================
# LAB: THE UNIQUE IDENTITY COLLECTOR (DE-DUPLICATION)
# PURPOSE: Utilizing Set Theory to Filter Redundant Data
# ==========================================================

def run_collector():
    # 1. DATA INITIALIZATION PHASE
    # We initialize an empty set. In memory, this creates a 
    # Hash Table structure that only accepts unique 'hashable' values.
    unique_numbers = set()

    print("--- [SECURITY DATA INTAKE SYSTEM] ---")
    print("Action: Collecting 8 numerical identifiers for de-duplication.")

    # 2. ITERATIVE ACQUISITION PHASE
    # We use a 'for' loop to simulate a batch processing of 8 incoming pings.
    for i in range(1, 9):
        try:
            # Type Casting: Converting the raw string input to an Integer.
            num = int(input(f"[{i}/8] Enter Security ID: "))
            
            # The .add() method handles the logic of checking for duplicates.
            # If the number exists, the set remains unchanged (O(1) complexity).
            unique_numbers.add(num)
            
        except ValueError:
            # Error Handling: Prevents system crash if non-numeric data is entered.
            print("⚠️ ERROR: Non-integer detected. Skipping entry.")

    # 3. ANALYTICAL OUTPUT PHASE
    # We calculate the delta between total inputs (8) and unique outcomes.
    print("\n" + "="*40)
    print(f"ANALYSIS COMPLETE")
    print(f"Total Unique Identities Secured: {len(unique_numbers)}")
    print(f"Final Unique Set: {unique_numbers}")
    print("="*40)

# 4. EXECUTION GATE
if __name__ == "__main__":
    run_collector()

# ==========================================================
# RESEARCH NOTE:
# This script demonstrates "Data Minimization." In AI Security, 
# storing 1,000 duplicate pings is a waste of memory. A 'Set' 
# ensures we only track unique threat actors, optimizing the 
# performance of anomaly detection algorithms.
# ==========================================================
