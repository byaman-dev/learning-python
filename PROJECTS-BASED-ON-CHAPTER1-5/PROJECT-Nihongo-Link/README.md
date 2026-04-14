# ⛩️ Duo-Nihongo: Bi-Directional Translator

A high-performance terminal application that translates between English and Japanese. This project is a comprehensive capstone combining the first five chapters of the **CodeWithHarry Python Masterclass**.

## 🚀 Overview
Most basic translators only work one way. **Duo-Nihongo** uses advanced dictionary logic to automatically generate a reverse-lookup table, allowing for seamless 2-way communication. It handles everything from simple greetings to numbers and common verbs.

## 🛠️ Key Features
* **Bi-Directional Engine:** Switch between English → Japanese and Japanese → English modes.
* **Smart Parsing:** Processes full sentences by breaking strings into lists and reassembling them.
* **Error Tolerance:** Uses safe dictionary lookups to prevent crashes when a word is missing.
* **Dynamic Database:** Automatically creates a reverse dictionary (Jap-Eng) from the source (Eng-Jap) to ensure data consistency.

## 📚 Concepts Applied (Chapters 1-5)
This project serves as a practical implementation of:
1.  **Chapter 1 (Modules & OS):** Using `os` for system-level feedback and `import` for modularity.
2.  **Chapter 2 (Variables & Types):** Managing state with Integers, Floats, and Booleans.
3.  **Chapter 3 (Strings):** Utilizing f-strings, `.lower()`, `.strip()`, `.split()`, and `.join()`.
4.  **Chapter 4 (Lists & Tuples):** Storing and iterating through word collections.
5.  **Chapter 5 (Dictionaries & Sets):** Implementing key-value mapping and using Sets to track unique vocabulary entries.

## 📈 Planned Improvements
- [ ] Add support for Kanji characters.
- [ ] Implement a "Learning Mode" using Tuples.
- [ ] Connect to an external JSON file for a larger word database.

---
