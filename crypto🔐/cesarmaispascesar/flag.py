# Encrypted text
cipher = "$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN"

# Convert text to ASCII values
ascii_cipher = [ord(c) for c in cipher]
print("ASCII values:", ascii_cipher)

# Hypothesis: The flag starts with "Star"
flag = "Star"
ascii_flag = [ord(c) for c in flag]
print("ASCII values of 'Star':", ascii_flag)

# Calculate the difference between ASCII values
start_cipher = "$E2C"
ascii_start = [ord(c) for c in start_cipher]
diff = [f - c for f, c in zip(ascii_flag, ascii_start)]
print("Differences:", diff)
