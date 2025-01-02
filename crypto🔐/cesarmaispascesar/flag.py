# Encrypted text
cipher = "$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN"

# Convert text to ASCII values
ascii_cipher = [ord(c) for c in cipher]
print("ASCII values:", ascii_cipher)

# Hypothesis: The flag starts with "Star"
flag = "Star"
asc