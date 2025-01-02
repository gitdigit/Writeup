# Decipherium

Category: crypto

## Solution

The given message is a list of periodic table element abbreviations. Here are the decoding steps:
* `TeSbILaTeSnTeNoISn...`
* Replace each element with its atomic number 
* `[52, 51, 53, 57, 52, 50, 52, 102, 53, 50]...`
* Get the ASCII character for each atomic number
* `4359424f52...`
* Two hex digits make one byte. Convert the bytes into their ASCII representations
* `0x43 = C, 0x59 = Y ...`


Below is my decoder script. I used the `periodictable` package to get the atomic numbers for each abbreviation.
```python
from periodictable import elements
import re

ciphertext = open("message.txt").read().strip()
elems = re.split("([A-Z][a-z]*)", ciphertext) # split element abbreviations string into list
atomic_numbers = []
for el in elems:
    try:
        atomic_numbers.append(getattr(elements, el).number) # get the atomic number of an element
    except AttributeError:
        pass
ascii_list = list(map(chr, atomic_numbers)) # atomic number -> ASCII char
hex_list = [i+j for i,j in zip(ascii_list[::2], ascii_list[1::2])] # the ASCII chars are two digit hex numbers
flag = "".join(map(lambda x: chr(int(x, 16)), hex_list)) # hex ints -> ASCII
print(flag)

```

## Flag
````
CYBORG{PERI0DIC_C1PH3R_0F_3LEMENT5}
````