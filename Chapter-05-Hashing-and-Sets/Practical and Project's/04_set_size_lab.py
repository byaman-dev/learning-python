# ==========================================================
# LAB: SET SIZE DYNAMICS (EQUALITY VS. IDENTITY)
# PURPOSE: Analyzing Membership Logic and Numeric Overlap
# ==========================================================

# 1. INITIALIZATION PHASE
# We define an empty set to track how length (cardinality) fluctuates.
s = set()

# 2. DATA INJECTION PHASE
# We add three values that look similar but have different 'Internal Representations'.
s.add(20)      # Integer (int)
s.add(20.0)    # Floating Point (float)
s.add("20")    # String (str)

# 3. ANALYTICAL REPORTING PHASE
# We use f-strings to display the results of the set's internal filtering.
print("--- [SET SIZE DYNAMICS ANALYSIS] ---")
print(f"Final Set Content: {s}")
print(f"Final Set Length:  {len(s)}")



# 4. SCIENTIFIC VERIFICATION
# Proving why the length is 2 and not 3.
print("\n[LOGICAL PROOF]")
print(f"Check: Does 20 == 20.0?  -> {20 == 20.0}")
print(f"Check: Does 20 == '20'?  -> {20 == '20'}")


# ==========================================================
# RESEARCH NOTE:
# Python Sets use a 'Hash Table'. For two items to be unique, 
# they must have different values. Because 20 and 20.0 
# evaluate as equal (True), the Set treats them as the 
# same mathematical entity. The String "20" is a literal 
# text object and is therefore unique.
# ==========================================================
