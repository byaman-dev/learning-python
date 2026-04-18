# 🇮🇳 FinTrack Bharat: Localized Expense Manager

**FinTrack Bharat** is a specialized expense tracking utility designed for the Indian lifestyle. It focuses on high-frequency, low-value transactions typical of the Indian economy (e.g., Chai, Kirana, UPI recharges).

## 🚀 Key Features
* **Localized Categories:** Pre-set categories like *Kirana*, *Chai/Snacks*, and *UPI/Metro* to match daily Indian spending.
* **Currency Formatting:** Precision handling of **INR (₹)** using Python's floating-point math (Ch 2).
* **Hisab-Kitab Ledger:** A clean, tabular summary that mirrors a traditional physical ledger (Bahi-Khata) in a digital CLI format.
* **Smart Filtering:** Automatically categorizes unrecognized inputs into "Other" to maintain data integrity.

## 🏗️ Technical Mastery (Ch 1-5)
* **Data Structuring (Ch 5):** Uses a list of dictionaries to act as a "Temporary Database."
* **Advanced Strings (Ch 3):** Implements localized f-strings and tabular alignment for professional reporting.
* **Input Sanitization:** Uses `.title()` and `.strip()` to ensure that "chai", "CHAI", and " Chai " are all saved as "Chai".
* **Collection Logic (Ch 4):** Efficiently iterates through expense lists to calculate sums and averages.

## 🌍 Real-World Application
This logic is the foundation for:
* **Digital Khata Apps:** Similar to Khatabook or OkCredit for small shopkeepers.
* **UPI Trackers:** Tools that parse SMS/User input to provide a daily spending limit.
* **Personal Finance:** Helping students or bachelors manage their "Monthly Pocket Money" or "Room Expenses."

## 📥 Usage
```bash
python fintrack_india.py
