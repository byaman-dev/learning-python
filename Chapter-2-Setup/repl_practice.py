# In Chapter 2, we learned that we don't always need a script.
# We can use the REPL for quick math:

# >>> 5 + 10
# 15
# >>> print("Testing REPL")
# Testing REPL

# 1. Basic Arithmetic (Using Python as a Calculator)
print(f"Addition: 50 + 50 = {50 + 50}")
print(f"Power (Exponent): 2 ** 3 = {2 ** 3}") # 2 to the power of 3

# 2. String Manipulation
# Testing how Python handles text in the REPL
name = "Aman"
print(f"Greeting: Hello " + name)
print(f"Repetition: {name * 3}") # Repeats the string 3 times

# 3. Type Checking (Very important in Chapter 2)
# Using the type() function to see what we are working with
print(f"Type of 100: {type(100)}")
print(f"Type of 99.9: {type(99.9)}")
print(f"Type of 'Python': {type('Python')}")

# 4. Boolean Logic (Quick True/False tests)
print(f"Is 10 > 5? {10 > 5}")
print(f"Is 10 == 9? {10 == 9}")

# 5. Testing the 'len' function
message = "Learning Python with Harry"
print(f"Character count of message: {len(message)}")

