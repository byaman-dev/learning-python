# ==========================================================
# LAB: THE TYPE FLEXIBILITY TEST (HASH INTEGRITY)
# PURPOSE: Distinguishing Between Data Types in a Unique Set
# ==========================================================

# 1. INITIALIZATION PHASE
# We define a set with elements that look similar but have different types.
# In Python, '18' (int) and '18.0' (float) are often treated as equal 
# in value, but "18" (string) is a different object entirely.

identity_set = {18, "18", 18.0}

# 2. ANALYSIS PHASE
# We examine the 'Cardinality' (length) of the set.
# If Python treats all three as unique, the length will be 3.
# If it treats 18 and 18.0 as the same, the length will be 2.

set_length = len(identity_set)

# 3. REPORTING PHASE
# Professional output using f-strings to display the set's behavior.

print(f"--- [SET INTEGRITY ANALYSIS] ---")
print(f"Raw Set Content: {identity_set}")
print(f"Total Unique Elements: {set_length}")

# 4. SCIENTIFIC VERIFICATION (Type Comparison)
# Let's verify why the set contains these specific items.
print("\n[MEMBER TYPE CHECK]")
for item in identity_set:
    print(f"Value: {item} | Type: {type(item)}")

# ==========================================================
# SECURITY & RESEARCH TAKEAWAY:
# Python's Set implementation uses "Value Equality" for numbers. 
# Since 18 == 18.0, only the first one encountered is kept.
# However, "18" (string) is fundamentally different. 
# Understanding this prevents "Type Confusion" attacks in AI.
# ==========================================================
