# --- Scenario: Calculating Firewall Rules ---

# Data received from a web form is always a String
input_port = "443" 
input_latency = "0.05"

# 1. Check original types
print(f"Original Port Type: {type(input_port)}")

# 2. Type Casting: Converting String to Integer/Float for logic
actual_port = int(input_port)
actual_latency = float(input_latency)

# 3. Verification
print(f"Converted Port: {actual_port} | Type: {type(actual_port)}")

# 4. Math Operation (Only works after conversion)
next_available_port = actual_port + 1
print(f"Scanning next port: {next_available_port}")
