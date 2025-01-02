# Caesar, but not Caesar

**Flag:** `StarHack{C3s444r_4u_Myst3r3_d3_l4_S4l4d3}`

## Challenge

**Description:**

> It’s a well-kept secret, but Caesar really loves salads. Who can decrypt it?
>
> `$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN`

## Solution

1. **Analyze the encrypted text:**

   The encrypted text is: `$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN`

2. **Convert to ASCII codes:**

   In Python, we can convert each character to its ASCII code:

   ```python
   encrypted = "$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN"
   ascii_vals = [ord(c) for c in encrypted]
   print("ASCII values:", ascii_vals)
   ```

3. **Hypothesis on the flag's beginning:**

   Knowing that the flag starts with `Star`, we can obtain the corresponding ASCII codes:

   ```python
   flag_start = "Star"
   ascii_flag = [ord(c) for c in flag_start]
   print("ASCII values of 'Star':", ascii_flag)
   ```

4. **Calculate the difference between ASCII values:**

   By comparing the ASCII values of the encrypted text and the assumed start of the flag:

   ```python
   cipher_start = "$E2C"
   ascii_cipher = [ord(c) for c in cipher_start]
   diff = [f - c for f, c in zip(ascii_flag, ascii_cipher)]
   print("Differences:", diff)
   ```

   The difference is a constant offset of 47.

5. **Reverse the shift to decrypt the text:**

   Applying a reverse shift of 47 to each character in the encrypted text:

   ```python
   decrypted = ''.join([chr(ord(c) + 47) for c in encrypted])
   print("Decrypted text:", decrypted)
   ```

   Decrypted text:

   ```
   StarHack{C3s444r_4u_Myst3r3_d3_l4_S4l4d3}
   ```

**Conclusion:**

The flag is `StarHack{C3s444r_4u_Myst3r3_d3_l4_S4l4d3}`.

---
