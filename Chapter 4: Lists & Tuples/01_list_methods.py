# --- Practical: Managing a Threat Database with Lists ---

# 1. Create a list of initial threats
threats = ["Malware", "Phishing", "Adware"]
print(f"Initial threats: {threats}")

# 2. A new threat is detected - add it to the end
threats.append("Ransomware")

# 3. An urgent threat is detected - insert it at the beginning (index 0)
threats.insert(0, "Zero-day Exploit")

# 4. Sorting threats alphabetically for a clean report
threats.sort()
print(f"Sorted threat report: {threats}")

# 5. Removing a threat after it has been patched
threats.remove("Adware")
print(f"Remaining threats to fix: {threats}")
