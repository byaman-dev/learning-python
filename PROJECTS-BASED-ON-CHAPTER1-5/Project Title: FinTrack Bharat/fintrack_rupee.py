'''
PROJECT: FinTrack Bharat - Daily Expense Manager
LOCALE: India (INR / ₹)
CONCEPTS: Dictionary Lists (Ch 5), Formatting (Ch 3), Input Handling.
'''

import os

# --- CHAPTER 5: INDIAN CONTEXT CATEGORIES ---
# Using a Set for unique, localized categories
categories = {"Kirana", "Chai/Snacks", "UPI/Recharge", "Rent/Bills", "Auto/Metro", "Other"}
expenses = []

print("="*45)
print("      🇮🇳  FIN-TRACK BHARAT: DAILY KHARCHA  🇮🇳      ")
print("="*45)
print(f"Categories: {', '.join(categories)}")

while True:
    # --- CHAPTER 3: INPUT NORMALIZATION ---
    item = input("\nKharcha (Item name) or 'band' to exit: ").strip().title()
    
    if item.lower() == 'band':
        break
        
    try:
        # Chapter 2: Handling Rupee amounts
        amount = float(input(f"Enter amount for {item} (₹): "))
        
        print(f"Select Category: {list(categories)}")
        cat_input = input("Category: ").strip().title()
        
        # Validation
        if cat_input not in categories:
            cat_input = "Other"

        # --- CHAPTER 5: DATA STORAGE ---
        kharcha_entry = {
            "item": item,
            "amount": amount,
            "category": cat_input
        }
        
        expenses.append(kharcha_entry)
        print(f"✅ Noted: ₹{amount} for {item}")
        
    except ValueError:
        print("❌ Please enter a valid number for the price!")

# --- CHAPTER 2 & 4: SUMMARY LOGIC ---
if expenses:
    total = sum(e['amount'] for e in expenses)
    count = len(expenses)

    # --- FINAL REPORT (Professional Table) ---
    print("\n" + "X"*45)
    print("           HISAB-KITAB SUMMARY             ")
    print("X"*45)
    print(f"{'Item':<15} | {'Category':<15} | {'Price':<10}")
    print("-" * 45)
    
    for e in expenses:
        # Using f-strings to format Rupee symbol and alignment
        print(f"{e['item']:<15} | {e['category']:<15} | ₹{e['amount']:<10.2f}")
    
    print("-" * 45)
    print(f"Total Kharcha:  ₹{total:.2f}")
    print(f"Total Items:    {count}")
    print(f"Avg per item:   ₹{total/count:.2f}")
    print("X"*45)
else:
    print("\nNo data entered. Chalo, bye!")
