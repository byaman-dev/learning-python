# 🐍 Chapter 4: Lists & Tuples
Welcome to the fourth stage of my Python journey! This chapter focuses on how Python stores collections of data. Understanding these structures is the foundation for managing security logs, user databases, and AI model parameters.

## 📚 Key Concepts Learned

### 1. Python Lists `[]`
Lists are **mutable** (changeable) containers used to store a sequence of values.
* **Syntax:** `my_list = [item1, item2, item3]`
* **Key Methods used:**
    * `.append()` – Adds an element at the end.
    * `.sort()` – Updates the list in ascending order.
    * `.reverse()` – Reverses the elements.
    * `.insert(index, value)` – Adds an element at a specific position.
    * `.pop(index)` – Removes an element at a specific position.

### 2. Python Tuples `()`
Tuples are **immutable** (unchangeable) containers. Once created, their elements cannot be modified.
* **Syntax:** `my_tuple = (item1, item2, item3)`
* **Why use Tuples?** They are faster and provide "write-protection" for data that should stay constant.

---

## 🛡️ AI Security Application
In the field of AI Security, we use these structures differently:
* **Lists:** Used to store **Blacklisted IPs** or **Detected Threats**. Since new threats appear every second, the list must be mutable to allow `.append()`.
* **Tuples:** Used to store **Model Metadata** or **Fixed Security Protocols**. For example, a tuple might store the fixed dimensions of an image input for a Computer Vision AI to prevent "Input Injection" attacks.

---

## 🛠️ Practice Set Tasks
In this folder, I have completed the following exercises from the Code with Harry curriculum:
1. **Fruit Store:** A script that stores 7 fruits entered by the user in a list.
2. **Student Marks:** A program that accepts marks of 6 students and displays them in a sorted manner.
3. **Tuple Immutability Test:** A script proving that a tuple cannot be changed after creation.
4. **Sum of List:** A program to sum a list of 4 numbers.
5. **Count Zeros:** A script to count the number of zeros in a specific tuple.

---



**Author:** @byaman-dev  
**Course:** Python 100 Days of Code (Code with Harry)
