# --- Practical: Using Tuples for Fixed Security Configs ---

# Standard secure ports (cannot be changed by mistake)
secure_ports = (443, 22, 80, 993)

# 1. Counting how many times a port appears
count_80 = secure_ports.count(80)
print(f"Port 80 appears {count_80} time in our config.")

# 2. Finding the index of a specific port
index_of_ssh = secure_ports.index(22)
print(f"SSH (Port 22) is located at index: {index_of_ssh}")

# 3. Demonstration of Immutability (Uncomment to see the error)
# secure_ports[0] = 8080 
# print("This will throw a TypeError because Tuples are immutable!")
